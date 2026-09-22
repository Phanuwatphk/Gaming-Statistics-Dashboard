"""Presentation layer for the Gaming Statistics dashboard."""

from __future__ import annotations

from collections import defaultdict
from html import escape
from typing import Any

import streamlit as st

if __package__ and __package__.startswith("src."):
    from src.api.rawg_api import RawgApiError
    from src.database.database import DatabaseError
    from src.services.game_service import GameService
else:  # Supports imports when Streamlit runs src/app.py as a script.
    from api.rawg_api import RawgApiError
    from database.database import DatabaseError
    from services.game_service import GameService


NAVIGATION = (
    ("home", "Home"),
    ("games", "Game Library"),
    ("search", "Search"),
    ("genres", "Genres"),
    ("top_rated", "Top Rated"),
    ("players", "Live Players"),
)


def render_dashboard(game_service: GameService) -> None:
    """Render dashboard pages using data supplied by GameService."""
    _apply_styles()
    _initialize_navigation_state()
    _render_sidebar()

    page = st.session_state.dashboard_page
    if page == "home":
        _render_home(game_service)
    elif page == "games":
        _render_games_page(game_service)
    elif page == "search":
        _render_search_page(game_service)
    elif page == "genres":
        _render_genres_page(game_service)
    elif page == "top_rated":
        _render_top_rated_page(game_service)
    elif page == "players":
        _render_players_page(game_service)
    elif page == "detail":
        _render_detail_page(game_service)


def _initialize_navigation_state() -> None:
    st.session_state.setdefault("dashboard_page", "home")
    st.session_state.setdefault("selected_game_id", None)


def _apply_styles() -> None:
    """Apply a clear, consistent visual system across the dashboard."""
    st.markdown(
        """
        <style>
        .stApp { --primary-color: #2563eb; --text-color: #132542; background: #f6f8fc; color: #132542; }
        [data-testid="stHeader"] { background: transparent; }
        [data-testid="stMain"] { color: #132542; }
        [data-testid="stMain"] [data-testid="stMetricLabel"] *,
        [data-testid="stMain"] [data-testid="stMetricValue"],
        [data-testid="stMain"] [data-testid="stMetricDelta"],
        [data-testid="stMain"] label,
        [data-testid="stMain"] [data-testid="stSelectbox"] *,
        [data-testid="stMain"] [data-testid="stTextInput"] * { color: #132542 !important; }
        [data-testid="stMain"] input, [data-testid="stMain"] [data-baseweb="select"] > div {
            background: #ffffff !important; color: #132542 !important; border-color: #c9d8ec !important;
        }
        [data-testid="stMain"] input::placeholder { color: #71819a !important; opacity: 1; }
        [data-testid="stMain"] .stButton > button { background: #2563eb; border: 1px solid #2563eb; color: #ffffff !important; }
        [data-testid="stMain"] .stButton > button:hover { background: #1d4ed8; border-color: #1d4ed8; color: #ffffff !important; }
        [data-testid="stMain"] .stButton > button * { color: #ffffff !important; }
        [data-testid="stSidebar"] { background: linear-gradient(180deg, #102947 0%, #071526 100%); }
        [data-testid="stSidebarUserContent"] { padding-top: .75rem; }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p { color: #eef5ff !important; }
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] * { color: #a8bed7 !important; }
        [data-testid="stSidebar"] .stButton > button {
            justify-content: flex-start; min-height: 2.75rem; padding: 0 .85rem; border: 1px solid transparent;
            border-radius: .55rem; background: transparent !important; color: #eef5ff !important;
            font-size: .94rem; transition: background .15s ease, border-color .15s ease;
        }
        [data-testid="stSidebar"] .stButton > button:hover,
        [data-testid="stSidebar"] .stButton > button:focus-visible {
            background: rgba(255, 255, 255, .16) !important; border-color: rgba(255, 255, 255, .18) !important;
            color: #ffffff !important;
        }
        [data-testid="stSidebar"] .stButton > button[kind="primary"] { background: #2563eb; color: #ffffff !important; }
        [data-testid="stSidebar"] .stButton > button[kind="primary"]:hover { background: #1d4ed8 !important; }
        [data-testid="stSidebar"] .stButton > button[kind="secondary"] { color: #eef5ff !important; }
        [data-testid="stSidebar"] .stButton > button * { color: inherit !important; }
        .block-container { max-width: 1400px; padding-top: 2.5rem; padding-bottom: 3rem; }
        .page-kicker { color: #2563eb; font-size: .75rem; font-weight: 750; letter-spacing: .1em; text-transform: uppercase; }
        .page-title { margin: .18rem 0 .35rem; color: #102542; font-size: 2.15rem; font-weight: 750; letter-spacing: -.03em; }
        .page-subtitle { color: #63738c; margin-bottom: 1.75rem; font-size: 1rem; }
        .sidebar-brand { color: #f6f9ff; font-size: 1.28rem; font-weight: 750; letter-spacing: -.02em; text-align: center; }
        .sidebar-label { color: #9db3cd; font-size: .82rem; margin-top: .25rem; text-align: center; }
        .hero-stat { background: linear-gradient(130deg, #102947, #1d4f8f); border-radius: 1rem; padding: 1.5rem 1.65rem; color: #f8fbff; margin: 0 0 1.75rem; box-shadow: 0 12px 28px rgba(16, 41, 71, .16); }
        .hero-stat-label { color: #bcd4f4; font-size: .82rem; font-weight: 700; letter-spacing: .07em; text-transform: uppercase; }
        .hero-stat-value { color: #ffffff; font-size: 2.35rem; font-weight: 760; letter-spacing: -.04em; line-height: 1.2; margin-top: .35rem; }
        .hero-stat-note { color: #d4e4f8; font-size: .88rem; margin-top: .35rem; }
        .game-card { background: #ffffff; border: 1px solid #dce7f5; border-radius: .8rem; padding: .9rem; min-height: 128px; box-shadow: 0 3px 12px rgba(28, 62, 106, .06); }
        .game-name { color: #142644; font-weight: 700; font-size: 1rem; margin-top: .25rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
        .game-meta { color: #60718a; font-size: .84rem; margin-top: .35rem; }
        .tag { display: inline-block; background: #edf4ff; color: #3264aa; border-radius: 999px; font-size: .72rem; padding: .18rem .48rem; margin: .45rem .18rem 0 0; }
        .empty-state { background: #ffffff; border: 1px dashed #b7c9e2; border-radius: 14px; padding: 3.5rem 1rem; text-align: center; color: #5c6f8a; }
        .detail-panel { background: #ffffff; border: 1px solid #dce7f5; border-radius: 12px; padding: 1.2rem; }
        .detail-label { color: #71819a; font-size: .78rem; margin-bottom: .15rem; }
        .detail-value { color: #142644; font-weight: 650; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def _render_sidebar() -> None:
    with st.sidebar:
        st.markdown('<div class="sidebar-brand">Gaming Statistics</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-label">Game discovery dashboard</div>', unsafe_allow_html=True)
        st.divider()

        for page, label in NAVIGATION:
            if st.button(
                label,
                key=f"navigation-{page}",
                type="primary" if st.session_state.dashboard_page == page else "secondary",
                width="stretch",
            ):
                _go_to(page)


def _render_home(game_service: GameService) -> None:
    games = game_service.get_live_top_games()
    _page_heading("Most Played on Steam", "A live snapshot of the 50 games with the most active players.")

    if not games:
        _render_empty_state("Live rankings are unavailable", "Refresh the page to request the latest Steam snapshot.")
        return
    current_players = [game["current_players"] for game in games if game["current_players"] is not None]
    latest_update = max(game["players_updated_at"] or "" for game in games)
    _render_top_player_stat(sum(current_players), latest_update)
    st.markdown("### Top 50 games by current players")
    _render_game_grid(games, columns_per_row=4, key_prefix="home-top")


def _render_games_page(game_service: GameService) -> None:
    games = game_service.get_games()
    _page_heading("Game Library", "Browse, filter, and compare your saved games.")
    if not games:
        _render_empty_state("Your library is empty", "Use Search to add games and build your collection.")
        return

    games = _render_collection_filters(games)
    if not games:
        _render_empty_state("No matching games", "Try broadening the genre, platform, or rating filters.")
        return

    sort_option = st.selectbox("Sort by", ("Highest rating", "Name: A–Z"))
    if sort_option == "Highest rating":
        games = _sort_by_rating(games)
    else:
        games = sorted(games, key=lambda game: game["name"].casefold())
    _render_game_grid(games, key_prefix="games")


def _render_collection_filters(games: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Render collection filters and return games matching every selected value."""
    genre_options = sorted({genre for game in games for genre in game["genres"]})
    platform_options = sorted({platform for game in games for platform in game["platforms"]})
    ratings = [game["rating"] for game in games if game["rating"] is not None]

    genre_column, platform_column, rating_column = st.columns(3)
    with genre_column:
        selected_genres = st.multiselect("Genre", genre_options, placeholder="All genres")
    with platform_column:
        selected_platforms = st.multiselect("Platform", platform_options, placeholder="All platforms")
    with rating_column:
        minimum_rating = st.number_input(
            "Minimum rating",
            min_value=0.0,
            max_value=5.0,
            value=0.0,
            step=0.1,
            disabled=not ratings,
        )

    return [
        game
        for game in games
        if (not selected_genres or set(selected_genres).intersection(game["genres"]))
        and (not selected_platforms or set(selected_platforms).intersection(game["platforms"]))
        and (
            minimum_rating == 0
            or (game["rating"] is not None and game["rating"] >= minimum_rating)
        )
    ]


def _render_search_page(game_service: GameService) -> None:
    _page_heading("Search Games", "Find games in RAWG and save them to your library.")
    search_term = st.text_input("Game title", placeholder="For example: Hades, Portal, or Minecraft")
    if not search_term.strip():
        _render_empty_state("Ready to search", "Enter a game title above to see results.")
        return

    games = game_service.search_games(search_term)
    if not games:
        st.info("This game is not in your library yet. Search RAWG to add it.")
    if st.button("Search and add to library", key="catalog-search", type="primary"):
        try:
            with st.spinner("Searching and adding game data..."):
                games = game_service.search_and_import_games(search_term)
                if games:
                    game_service.refresh_current_players(
                        force=True, game_ids={game["game_id"] for game in games}
                    )
            if games:
                st.success(f"Added {len(games)} game(s) to your library.")
            else:
                st.warning(f'No games matched “{search_term.strip()}”.')
        except (RawgApiError, DatabaseError, ValueError) as error:
            st.error(str(error))
    if not games:
        return
    st.caption(f'Results for “{search_term.strip()}” · {len(games)} game(s)')
    _render_game_grid(games, columns_per_row=1, key_prefix="search")


def _render_genres_page(game_service: GameService) -> None:
    _page_heading("Genres", "Explore the games in your library by genre.")
    grouped_games: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for game in game_service.get_games():
        for genre in game["genres"]:
            grouped_games[genre].append(game)

    if not grouped_games:
        _render_empty_state("No genre data yet", "Add games through Search to start exploring genres.")
        return
    for genre in sorted(grouped_games):
        with st.expander(f"{genre} · {len(grouped_games[genre])} game(s)"):
            _render_game_grid(grouped_games[genre], columns_per_row=3, key_prefix=f"genre-{genre}")


def _render_top_rated_page(game_service: GameService) -> None:
    _page_heading("Top Rated Games", "The highest-rated games in your saved library.")
    games = _sort_by_rating(game_service.get_games())
    if not games:
        _render_empty_state("Your library is empty", "Use Search to add games and view their ratings.")
        return
    _render_game_grid(games, key_prefix="top-rated")


def _render_players_page(game_service: GameService) -> None:
    _page_heading("Live Players", "Steam's latest Top 50 games by active player count.")
    games = game_service.get_live_top_games()
    if not games:
        _render_empty_state(
            "Live Steam data is unavailable",
            "Refresh the page to request the latest ranking snapshot.",
        )
        return
    latest_update = max(game["players_updated_at"] or "" for game in games)
    if latest_update:
        st.caption(f"Last updated: {_display_timestamp(latest_update)}")
    _render_game_grid(games, key_prefix="players")


def _render_detail_page(game_service: GameService) -> None:
    game_id = st.session_state.selected_game_id
    game = next((item for item in game_service.get_games() if item["game_id"] == game_id), None)
    if game is None:
        _render_empty_state("Game not found", "This game may have been removed from the library.")
        if st.button("Back to Game Library"):
            _go_to("games")
        return

    if st.button("← Back to Games"):
        _go_to("games")
    _page_heading(game["name"], "Everything you need to know at a glance.")

    if game["image"]:
        st.image(game["image"], width="stretch")

    st.markdown("### Game Information")
    fields = (
        ("Rating", game["rating"] if game["rating"] is not None else "–"),
        ("Steam players now", f'{game["current_players"]:,}' if game["current_players"] is not None else "N/A"),
        ("Release date", game["released"] or "–"),
        ("Platforms", ", ".join(game["platforms"]) or "–"),
        ("Metacritic", game["metacritic"] if game["metacritic"] is not None else "–"),
    )
    columns = st.columns(len(fields))
    for column, (label, value) in zip(columns, fields):
        with column:
            st.markdown(
                f'<div class="detail-panel"><div class="detail-label">{escape(str(label))}</div>'
                f'<div class="detail-value">{escape(str(value))}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("### Genres")
    if game["genres"]:
        tags = " ".join(f'<span class="tag">{escape(genre)}</span>' for genre in game["genres"])
        st.markdown(tags, unsafe_allow_html=True)
    else:
        st.caption("No genre data available.")


def _render_game_grid(
    games: list[dict[str, Any]], columns_per_row: int = 3, key_prefix: str = "games"
) -> None:
    for start in range(0, len(games), columns_per_row):
        columns = st.columns(columns_per_row)
        for offset, (column, game) in enumerate(zip(columns, games[start : start + columns_per_row])):
            with column:
                _render_game_card(game, f"{key_prefix}-{start + offset}")


def _render_top_player_stat(total_players: int, latest_update: str) -> None:
    """Render the sole Home KPI: active players across Steam's Top 50."""
    updated_note = (
        f"Last updated {_display_timestamp(latest_update)}" if latest_update else "Update time unavailable"
    )
    st.markdown(
        '<div class="hero-stat">'
        '<div class="hero-stat-label">Players in the Steam Top 50</div>'
        f'<div class="hero-stat-value">{total_players:,}</div>'
        f'<div class="hero-stat-note">{escape(updated_note)}</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def _render_game_card(game: dict[str, Any], key_prefix: str) -> None:
    if game["image"]:
        st.image(game["image"], width="stretch")
    else:
        st.markdown('<div class="game-card">No cover image available</div>', unsafe_allow_html=True)

    rank = f"#{game['live_rank']} · " if game.get("live_rank") else ""
    rating = f"Rating {game['rating']:.1f}" if game["rating"] is not None else ""
    summary = f"{rank}{rating}" or "Steam"
    players = (
        f"{game['current_players']:,} players online"
        if game["current_players"] is not None
        else "Player count unavailable"
    )
    tags = "".join(f'<span class="tag">{escape(genre)}</span>' for genre in game["genres"][:2]) or '<span class="tag">Uncategorized</span>'
    st.markdown(
        f'<div class="game-card"><div class="game-name">{escape(game["name"])}</div>'
        f'<div class="game-meta">{summary}</div>'
        f'<div class="game-meta">{players}</div>{tags}</div>',
        unsafe_allow_html=True,
    )
    if st.button("View Details", key=f"detail-{key_prefix}-{game['game_id']}", width="stretch"):
        st.session_state.selected_game_id = game["game_id"]
        _go_to("detail")


def _render_empty_state(title: str, message: str) -> None:
    st.markdown(
        f'<div class="empty-state"><h3>{escape(title)}</h3><p>{escape(message)}</p></div>',
        unsafe_allow_html=True,
    )


def _page_heading(title: str, subtitle: str) -> None:
    st.markdown('<div class="page-kicker">Gaming Statistics</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-title">{escape(title)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="page-subtitle">{escape(subtitle)}</div>', unsafe_allow_html=True)


def _sort_by_rating(games: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(games, key=lambda game: game["rating"] if game["rating"] is not None else -1, reverse=True)


def _display_timestamp(value: str) -> str:
    """Display UTC timestamps to seconds, without noisy fractional seconds."""
    timestamp = value.replace("T", " ").replace("+00:00", " UTC")
    date_time, separator, timezone = timestamp.partition(" UTC")
    return f"{date_time.split('.', maxsplit=1)[0]}{separator}{timezone}"


def _go_to(page: str) -> None:
    st.session_state.dashboard_page = page
    st.rerun()
