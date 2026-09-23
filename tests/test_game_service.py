from src.database.database import GameDatabase
from src.services.game_service import GameService


class FakeRawgClient:
    def fetch_games(self, page_size: int):
        assert page_size == 2
        return [
            {
                "id": 1,
                "name": "Portal 2",
                "rating": 4.6,
                "genres": [{"name": "Puzzle"}],
                "platforms": [{"platform": {"name": "PC"}}],
            },
            {
                "id": 2,
                "name": "Hades",
                "rating": 4.8,
                "genres": [{"name": "Action"}],
                "platforms": [{"platform": {"name": "Nintendo Switch"}}],
            },
        ]


def test_service_fetches_processes_stores_and_searches(tmp_path):
    service = GameService(FakeRawgClient(), GameDatabase(tmp_path / "games.db"))

    result = service.sync_games(page_size=2)

    assert result.fetched == 2
    assert result.saved == 2
    assert [game["name"] for game in service.get_games()] == ["Hades", "Portal 2"]
    assert [game["name"] for game in service.search_games("portal")] == ["Portal 2"]
    assert service.search_games("missing") == []


class FakeSteamClient:
    def find_app_id(self, game_name: str):
        return {"Portal 2": 620}.get(game_name)

    def get_current_players(self, app_id: int):
        assert app_id == 620
        return 1234


def test_service_refreshes_and_persists_available_steam_player_counts(tmp_path):
    database = GameDatabase(tmp_path / "games.db")
    database.insert_games(
        [
            {
                "game_id": 1,
                "name": "Portal 2",
                "rating": None,
                "released": None,
                "genres": [],
                "platforms": [],
                "metacritic": None,
                "ratings_count": None,
                "image": None,
            },
            {
                "game_id": 2,
                "name": "Not on Steam",
                "rating": None,
                "released": None,
                "genres": [],
                "platforms": [],
                "metacritic": None,
                "ratings_count": None,
                "image": None,
            },
        ]
    )
    service = GameService(FakeRawgClient(), database, steam_client=FakeSteamClient())

    result = service.refresh_current_players(force=True)
    games = {game["name"]: game for game in service.get_games()}

    assert result.updated == 1
    assert result.unavailable == 1
    assert games["Portal 2"]["current_players"] == 1234
    assert games["Portal 2"]["players_updated_at"].endswith("+07:00")
    assert games["Not on Steam"]["steam_lookup_status"] == "unavailable"


class FakeRawgSearchClient:
    def search_games(self, search_term: str, page_size: int):
        assert search_term == "Minecraft"
        assert page_size == 100
        return [{"id": 70, "name": "Minecraft", "genres": [], "platforms": []}]


def test_service_imports_rawg_search_results_into_the_local_database(tmp_path):
    service = GameService(FakeRawgSearchClient(), GameDatabase(tmp_path / "games.db"))

    games = service.search_and_import_games("Minecraft")

    assert [game["name"] for game in games] == ["Minecraft"]


class FakeSteamTopClient:
    def get_most_played_games(self, limit: int):
        assert limit == 100
        return [
            {
                "game_id": -730,
                "name": "Counter-Strike 2",
                "rating": None,
                "released": None,
                "genres": [],
                "platforms": ["PC (Steam)"],
                "metacritic": None,
                "ratings_count": None,
                "image": None,
                "steam_app_id": 730,
                "steam_lookup_status": "found",
                "current_players": 500,
                "live_rank": 1,
            }
        ]


def test_service_refreshes_the_live_top_games_for_home(tmp_path):
    service = GameService(
        FakeRawgClient(), GameDatabase(tmp_path / "games.db"), steam_client=FakeSteamTopClient()
    )

    result = service.refresh_live_top_games()

    assert result.saved == 1
    assert [game["name"] for game in service.get_live_top_games()] == ["Counter-Strike 2"]


class FakeDiscoveryClient:
    def fetch_games(self, page_size: int, ordering: str | None = None):
        assert page_size == 100
        assert ordering == "-added"
        return [
            {
                "id": 10,
                "name": "Popular game",
                "genres": [{"name": "Adventure"}],
                "platforms": [],
                "ratings_count": 100,
            }
        ]


def test_service_saves_rawg_discoveries_before_home_reads_them(tmp_path):
    service = GameService(FakeDiscoveryClient(), GameDatabase(tmp_path / "games.db"))

    result = service.refresh_catalog()

    assert result.saved == 1
    assert service.get_popular_games()[0]["genres"] == ["Adventure"]
    assert service.get_popular_games()[0]["catalog_updated_at"].endswith("+07:00")
