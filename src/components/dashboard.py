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
    from src.utils.time_utils import format_thailand_timestamp
    from src.components.styles import apply_dashboard_styles
else:  # Supports imports when Streamlit runs src/app.py as a script.
    from api.rawg_api import RawgApiError
    from database.database import DatabaseError
    from services.game_service import GameService
    from utils.time_utils import format_thailand_timestamp
    from components.styles import apply_dashboard_styles


NAVIGATION = (
    ("home", "Home"),
    ("games", "Game Library"),
    ("search", "Search"),
    ("genres", "Genres"),
    ("top_rated", "Top Rated"),
    ("players", "Live Players"),
)
GAMES_PER_PAGE = 100


def render_dashboard(game_service: GameService) -> None:
    """Render dashboard pages using data supplied by GameService."""
    apply_dashboard_styles()
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
    games = game_service.get_popular_games()
    live_games = game_service.get_live_top_games()
    _page_heading("Popular Games", "Popular and widely played games saved from the latest RAWG discovery update.")

    if not games:
        _render_empty_state("Popular games are unavailable", "Refresh the page to request the latest game discovery snapshot.")
        return
    current_players = [game["current_players"] for game in live_games if game["current_players"] is not None]
    latest_update = max((game["players_updated_at"] or "" for game in live_games), default="")
    _render_top_player_stat(sum(current_players), latest_update)
    st.markdown("### Popular games")
    _render_paginated_game_grid(games, page_key="home", columns_per_row=4, key_prefix="home")


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

    st.caption("Sorted by the most recent database update.")
    _render_paginated_game_grid(games, page_key="games", key_prefix="games")


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
    _page_heading("Search Games", "Search your library first; missing games are fetched and saved automatically.")
    with st.form("game-search"):
        search_term = st.text_input(
            "Game title", placeholder="For example: Hades, Portal, or Minecraft"
        )
        submitted = st.form_submit_button("Search", type="primary")
    if not search_term.strip():
        _render_empty_state("Ready to search", "Enter a game title above to see results.")
        return
    if not submitted:
        return

    try:
        with st.spinner("Searching games..."):
            games = game_service.search_or_import_games(search_term)
    except (RawgApiError, DatabaseError, ValueError) as error:
        st.error(str(error))
        return
    if not games:
        _render_empty_state("No matching games", f'No games matched “{search_term.strip()}”.')
        return
    st.caption(f'Results for “{search_term.strip()}” · {len(games)} game(s)')
    _render_paginated_game_grid(
        games, page_key="search-results", columns_per_row=1, key_prefix="search"
    )


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
            _render_paginated_game_grid(
                grouped_games[genre],
                page_key=f"genre-{genre}",
                columns_per_row=3,
                key_prefix=f"genre-{genre}",
            )


def _render_top_rated_page(game_service: GameService) -> None:
    _page_heading("Top Rated Games", "The highest-rated games in your saved library.")
    games = _sort_by_rating(game_service.get_games())
    if not games:
        _render_empty_state("Your library is empty", "Use Search to add games and view their ratings.")
        return
    _render_paginated_game_grid(
        games, page_key="top-rated", key_prefix="top-rated", show_rank=True
    )


def _render_players_page(game_service: GameService) -> None:
    _page_heading("Live Players", "Steam's latest Top 100 games by current active player count.")
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
    _render_paginated_game_grid(games, page_key="players", key_prefix="players", show_rank=True)


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
    games: list[dict[str, Any]],
    columns_per_row: int = 3,
    key_prefix: str = "games",
    show_rank: bool = False,
    rank_start: int = 1,
) -> None:
    for start in range(0, len(games), columns_per_row):
        columns = st.columns(columns_per_row)
        for offset, (column, game) in enumerate(zip(columns, games[start : start + columns_per_row])):
            with column:
                rank = rank_start + start + offset if show_rank else None
                _render_game_card(game, f"{key_prefix}-{start + offset}", rank)


def _render_paginated_game_grid(
    games: list[dict[str, Any]],
    page_key: str,
    columns_per_row: int = 3,
    key_prefix: str = "games",
    show_rank: bool = False,
) -> None:
    """Render exactly up to 100 games and page through the remaining local records."""
    total_pages = max(1, (len(games) + GAMES_PER_PAGE - 1) // GAMES_PER_PAGE)
    state_key = f"pagination-{page_key}"
    current_page = min(st.session_state.get(state_key, 1), total_pages)
    st.session_state[state_key] = current_page
    start = (current_page - 1) * GAMES_PER_PAGE
    _render_game_grid(
        games[start : start + GAMES_PER_PAGE],
        columns_per_row=columns_per_row,
        key_prefix=f"{key_prefix}-page-{current_page}",
        show_rank=show_rank,
        rank_start=start + 1,
    )
    if total_pages == 1:
        return

    previous_column, page_column, next_column = st.columns((1, 2, 1))
    with previous_column:
        if st.button("← Previous", key=f"{state_key}-previous", disabled=current_page == 1):
            st.session_state[state_key] = current_page - 1
            st.rerun()
    with page_column:
        st.markdown(f"<p style='text-align:center'>Page {current_page} of {total_pages}</p>", unsafe_allow_html=True)
    with next_column:
        if st.button("Next →", key=f"{state_key}-next", disabled=current_page == total_pages):
            st.session_state[state_key] = current_page + 1
            st.rerun()


def _render_top_player_stat(total_players: int, latest_update: str) -> None:
    """Render the sole Home KPI: active players across Steam's Top 100."""
    updated_note = (
        f"Last updated {_display_timestamp(latest_update)}" if latest_update else "Update time unavailable"
    )
    st.markdown(
        '<div class="hero-stat">'
        '<div class="hero-stat-label">Players in the Steam Top 100</div>'
        f'<div class="hero-stat-value">{total_players:,}</div>'
        f'<div class="hero-stat-note">{escape(updated_note)}</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def _render_game_card(game: dict[str, Any], key_prefix: str, rank: int | None = None) -> None:
    if game["image"]:
        st.markdown(
            f'<img class="game-cover" src="{escape(str(game["image"]), quote=True)}" '
            f'alt="Cover for {escape(str(game["name"]), quote=True)}">',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="game-cover game-cover--empty">No cover image available</div>',
            unsafe_allow_html=True,
        )

    rank_text = f"#{rank} · " if rank is not None else ""
    rating = f"Rating {game['rating']:.1f}" if game["rating"] is not None else ""
    summary = f"{rank_text}{rating}" or "Steam"
    players = (
        f"{game['current_players']:,} players online"
        if game["current_players"] is not None
        else "Player count unavailable"
    )
    tags = "".join(f'<span class="tag">{escape(genre)}</span>' for genre in game["genres"][:2]) or '<span class="tag">Uncategorized</span>'
    st.markdown(
        f'<div class="game-card"><div class="game-name">{escape(game["name"])}</div>'
        f'<div class="game-meta">{summary}</div>'
        f'<div class="game-meta">{players}</div><div class="game-tags">{tags}</div></div>',
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
    """Display timestamps in Thailand time, to second precision."""
    return format_thailand_timestamp(value)


def _go_to(page: str) -> None:
    st.session_state.dashboard_page = page
    st.rerun()
