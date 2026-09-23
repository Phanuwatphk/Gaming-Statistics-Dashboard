"""Service layer coordinating RAWG, data processing, and SQLite."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from typing import Any

if __package__ and __package__.startswith("src."):
    from src.api.rawg_api import RawgApiClient
    from src.api.steam_api import SteamApiClient, SteamApiError, SteamConnectionError
    from src.database.database import GameDatabase
    from src.utils.data_processing import process_games
    from src.utils.time_utils import thailand_now
else:  # Supports imports when Streamlit runs src/app.py as a script.
    from api.rawg_api import RawgApiClient
    from api.steam_api import SteamApiClient, SteamApiError, SteamConnectionError
    from database.database import GameDatabase
    from utils.data_processing import process_games
    from utils.time_utils import thailand_now

PAGE_SIZE = 100
LIVE_TOP_GAMES_LIMIT = PAGE_SIZE


@dataclass(frozen=True)
class SyncResult:
    """A concise result for the dashboard after synchronizing RAWG data."""

    fetched: int
    saved: int


@dataclass(frozen=True)
class PlayerRefreshResult:
    """Outcome of one refresh pass over Steam-compatible games."""

    updated: int
    unavailable: int
    failed: int
    skipped: bool = False


@dataclass(frozen=True)
class LiveTopRefreshResult:
    """Outcome of refreshing the Steam-ranked games used on the Home page."""

    saved: int
    skipped: bool = False


@dataclass(frozen=True)
class CatalogRefreshResult:
    """Outcome of refreshing the locally stored RAWG discovery catalogue."""

    saved: int
    skipped: bool = False


class GameService:
    """Provide dashboard-ready game data without exposing API or SQL details."""

    def __init__(
        self,
        api_client: RawgApiClient,
        database: GameDatabase,
        steam_client: SteamApiClient | None = None,
    ) -> None:
        self.api_client = api_client
        self.database = database
        self.steam_client = steam_client or SteamApiClient()
        self.database.initialize()

    def sync_games(self, page_size: int = PAGE_SIZE) -> SyncResult:
        """Fetch RAWG data, normalize it, and save it to SQLite."""
        raw_games = self.api_client.fetch_games(page_size)
        games = process_games(raw_games)
        saved = self.database.insert_games(games, updated_at=thailand_now().isoformat())
        return SyncResult(fetched=len(raw_games), saved=saved)

    def get_games(self) -> list[dict[str, Any]]:
        """Retrieve all games currently saved in SQLite."""
        return self.database.get_games()

    def get_live_top_games(self) -> list[dict[str, Any]]:
        """Retrieve the current Home-page ranking from SQLite."""
        return self.database.get_live_top_games()

    def get_popular_games(self) -> list[dict[str, Any]]:
        """Retrieve locally stored popular RAWG games for the Home page."""
        return self.database.get_popular_games()

    def search_games(self, search_term: str) -> list[dict[str, Any]]:
        """Find games from SQLite; a blank search deliberately returns no results."""
        return self.database.search_games(search_term)

    def search_or_import_games(
        self, search_term: str, page_size: int = PAGE_SIZE
    ) -> list[dict[str, Any]]:
        """Search SQLite first, fetching and saving RAWG results only on a miss."""
        local_games = self.database.search_games(search_term)
        if local_games:
            return local_games
        return self.search_and_import_games(search_term, page_size)

    def search_and_import_games(self, search_term: str, page_size: int = PAGE_SIZE) -> list[dict[str, Any]]:
        """Find titles in RAWG and make their normalized data available locally."""
        raw_games = self.api_client.search_games(search_term, page_size)
        games = process_games(raw_games)
        self.database.insert_games(games, updated_at=thailand_now().isoformat())
        return self.database.search_games(search_term)

    def refresh_current_players(
        self,
        minimum_interval: timedelta = timedelta(minutes=15),
        force: bool = False,
        game_ids: set[int] | None = None,
    ) -> PlayerRefreshResult:
        """Refresh Steam counts, using a short shared cache to protect both APIs."""
        now = thailand_now()
        last_refresh = self.database.get_metadata("players_last_refresh")
        if game_ids is None and not force and _is_fresh(last_refresh, now, minimum_interval):
            return PlayerRefreshResult(0, 0, 0, skipped=True)

        updated = unavailable = failed = 0
        readings: list[tuple[int, int | None]] = []
        for game in self.database.get_games():
            if game_ids is not None and game["game_id"] not in game_ids:
                continue
            steam_app_id = game["steam_app_id"]
            if game["steam_lookup_status"] == "unavailable":
                unavailable += 1
                continue
            try:
                if steam_app_id is None:
                    steam_app_id = self.steam_client.find_app_id(game["name"])
                    self.database.set_steam_mapping(game["game_id"], steam_app_id)
                if steam_app_id is None:
                    unavailable += 1
                    continue
                current_players = self.steam_client.get_current_players(steam_app_id)
                readings.append((game["game_id"], current_players))
                updated += 1
            except SteamConnectionError:
                # A network failure will affect every following request too.
                failed += 1
                break
            except SteamApiError:
                failed += 1

        self.database.update_current_players_bulk(readings, now.isoformat())

        if game_ids is None:
            self.database.set_metadata("players_last_refresh", now.isoformat())
        return PlayerRefreshResult(updated, unavailable, failed)

    def refresh_catalog(
        self, minimum_interval: timedelta = timedelta(minutes=15), force: bool = False
    ) -> CatalogRefreshResult:
        """Fetch up to 100 RAWG discoveries, save them, then let the UI read SQLite."""
        now = thailand_now()
        last_refresh = self.database.get_metadata("catalog_last_refresh")
        if not force and _is_fresh(last_refresh, now, minimum_interval):
            return CatalogRefreshResult(0, skipped=True)

        # ``-added`` is RAWG's popularity signal (how often a game is added
        # to player collections), making Home a discovery feed rather than a
        # duplicate of Steam's live-player chart.
        raw_games = self.api_client.fetch_games(PAGE_SIZE, ordering="-added")
        games = process_games(raw_games)
        saved = self.database.insert_games(games, updated_at=now.isoformat())
        self.database.set_metadata("catalog_last_refresh", now.isoformat())
        return CatalogRefreshResult(saved)

    def refresh_live_top_games(
        self, minimum_interval: timedelta = timedelta(minutes=15), force: bool = False
    ) -> LiveTopRefreshResult:
        """Refresh Steam's Top 100 once per shared interval and persist the result."""
        now = thailand_now()
        last_refresh = self.database.get_metadata("live_top_last_refresh")
        saved_games = self.database.get_live_top_games(limit=LIVE_TOP_GAMES_LIMIT)
        if (
            not force
            and len(saved_games) >= LIVE_TOP_GAMES_LIMIT
            and _is_fresh(last_refresh, now, minimum_interval)
        ):
            return LiveTopRefreshResult(len(saved_games), skipped=True)

        games = self.steam_client.get_most_played_games(limit=PAGE_SIZE)
        saved = self.database.save_live_top_games(games, now.isoformat())
        self.database.set_metadata("live_top_last_refresh", now.isoformat())
        return LiveTopRefreshResult(saved)


def _is_fresh(value: str | None, now: datetime, interval: timedelta) -> bool:
    if not value:
        return False
    try:
        last_refresh = datetime.fromisoformat(value)
    except ValueError:
        return False
    if last_refresh.tzinfo is None:
        last_refresh = last_refresh.replace(tzinfo=UTC)
    return now - last_refresh < interval
