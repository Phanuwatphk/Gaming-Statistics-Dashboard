"""Streamlit entry point for the Gaming Statistics Dashboard."""

from __future__ import annotations

import os
from pathlib import Path
from datetime import timedelta

import streamlit as st

if __package__:
    from .api.rawg_api import RawgApiClient, RawgApiError
    from .api.steam_api import SteamApiError
    from .components.dashboard import render_dashboard
    from .database.database import DatabaseError, GameDatabase
    from .services.game_service import GameService
else:  # `streamlit run src/app.py` executes this module as a script.
    from api.rawg_api import RawgApiClient, RawgApiError
    from api.steam_api import SteamApiError
    from components.dashboard import render_dashboard
    from database.database import DatabaseError, GameDatabase
    from services.game_service import GameService


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE_PATH = PROJECT_ROOT / "data" / "gaming_statistics.db"


def build_game_service() -> GameService:
    """Create the dependencies used by the dashboard for this application run."""
    database_path = Path(os.getenv("GAMING_DASHBOARD_DB", DEFAULT_DATABASE_PATH))
    return GameService(RawgApiClient(), GameDatabase(database_path))


def _live_refresh_interval() -> timedelta:
    """Read the shared Home ranking refresh interval, defaulting to 15 minutes."""
    try:
        minutes = max(0, int(os.getenv("PLAYER_REFRESH_MINUTES", "15")))
    except ValueError:
        minutes = 15
    return timedelta(minutes=minutes)


def _refresh_dashboard_data(game_service: GameService, refresh_interval: timedelta) -> None:
    """Refresh shared RAWG and Steam snapshots once per visitor session."""
    if st.session_state.get("home_refresh_checked"):
        return
    st.session_state.home_refresh_checked = True
    try:
        with st.spinner("Updating game discoveries and Steam live players..."):
            st.session_state.catalog_refresh_result = game_service.refresh_catalog(refresh_interval)
    except RawgApiError as error:
        st.session_state.catalog_refresh_error = str(error)
    try:
        with st.spinner("Updating game discoveries and Steam live players..."):
            st.session_state.home_refresh_result = game_service.refresh_live_top_games(refresh_interval)
    except SteamApiError as error:
        # Preserve the last successful SQLite snapshot if Steam is temporarily unavailable.
        st.session_state.home_refresh_error = str(error)


def main() -> None:
    """Configure Streamlit and render the dashboard."""
    st.set_page_config(page_title="Gaming Statistics", layout="wide")
    try:
        game_service = build_game_service()
        _refresh_dashboard_data(game_service, _live_refresh_interval())
        if error := st.session_state.get("home_refresh_error"):
            st.warning(f"Showing the last saved Steam ranking: {error}")
        if error := st.session_state.get("catalog_refresh_error"):
            st.warning(f"Showing the last saved game catalogue: {error}")
        render_dashboard(game_service)
    except DatabaseError as error:
        st.error(str(error))


if __name__ == "__main__":
    main()
