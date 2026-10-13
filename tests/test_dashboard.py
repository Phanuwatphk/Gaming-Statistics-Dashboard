from pathlib import Path
from datetime import UTC, datetime
import re
from urllib.parse import parse_qs, urlsplit

import pytest
from streamlit.testing.v1 import AppTest

from src.components.dashboard import _display_timestamp
from src.database.database import GameDatabase


PROJECT_ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("navigation_page", "pagination_page"),
    [("players", "players"), ("top_rated", "top-rated"), ("games", "games")],
)
def test_consecutive_pagination_issues_distinct_scroll_resets(
    tmp_path, monkeypatch, navigation_page, pagination_page
):
    database_path = tmp_path / "pagination.db"
    database = GameDatabase(database_path)
    games = [
        {
            "game_id": game_id,
            "name": f"Game {game_id:03d}",
            "rating": 4.0,
            "released": f"{2020 + game_id % 2}-01-01",
            "genres": ["Action"],
            "platforms": ["PC"],
            "metacritic": 80,
            "ratings_count": 10,
            "image": None,
            "steam_app_id": game_id,
            "steam_lookup_status": "found",
            "current_players": 1000 - game_id,
            "live_rank": game_id,
        }
        for game_id in range(1, 101)
    ]
    database.insert_games(games)
    database.save_live_top_games(games, "2026-10-07T10:00:00+07:00")
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")

    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10).run()
    app.button(key=f"navigation-{navigation_page}").click().run()
    assert not app.exception
    previous_script = app.get("html")[-1].proto.body
    previous_request_id = app.session_state["scroll_request_id"]

    for direction, expected_page in [("next", 2), ("previous", 1), ("next", 2), ("previous", 1)]:
        app.button(key=f"pagination-{pagination_page}-{direction}").click().run()
        assert not app.exception
        assert app.session_state[f"pagination-{pagination_page}"] == expected_page
        assert app.session_state["scroll_request_id"] == previous_request_id + 1
        script = app.get("html")[-1].proto.body
        assert script != previous_script
        previous_script = script
        previous_request_id = app.session_state["scroll_request_id"]


def test_genres_page_allows_a_game_in_multiple_genres(tmp_path, monkeypatch):
    """Each game-detail button must stay unique across different genre sections."""
    database_path = tmp_path / "dashboard.db"
    GameDatabase(database_path).insert_games(
        [
            {
                "game_id": 4459,
                "name": "Portal 2",
                "rating": 4.6,
                "released": "2011-04-18",
                "genres": ["Puzzle", "Shooter"],
                "platforms": ["PC"],
                "metacritic": 95,
                "ratings_count": 100,
                "image": None,
            }
        ]
    )
    GameDatabase(database_path).set_metadata("players_last_refresh", datetime.now(UTC).isoformat())
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")

    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10,).run()
    app.button(key="navigation-genres").click().run()

    assert not app.exception


def test_display_timestamp_omits_fractional_seconds():
    assert _display_timestamp("2026-09-22T18:17:06.590359+00:00") == "2026-09-23 01:17:06 UTC+7"


def test_filter_games_combines_genre_platform_rating_and_release_year():
    from src.components.dashboard import _filter_games

    games = [
        {"name": "A", "genres": ["Action"], "platforms": ["PC"], "rating": 4.5, "released": "2020-01-01"},
        {"name": "B", "genres": ["Action"], "platforms": ["PC"], "rating": 3.0, "released": "2021-01-01"},
        {"name": "C", "genres": ["RPG"], "platforms": ["PC"], "rating": 4.8, "released": "2020-01-01"},
    ]

    assert _filter_games(games, ["Action"], ["PC"], 4.0, (2020, 2020)) == [games[0]]


def test_sort_games_orders_values_and_keeps_missing_values_last():
    from src.components.dashboard import _sort_games

    games = [
        {"name": "C", "rating": None, "released": None},
        {"name": "A", "rating": 4.0, "released": "2020-01-01"},
        {"name": "B", "rating": 5.0, "released": "2021-01-01"},
    ]

    assert [game["name"] for game in _sort_games(games, "Rating")] == ["B", "A", "C"]
    assert [game["name"] for game in _sort_games(games, "Release Date", descending=False)] == ["A", "B", "C"]


def test_statistics_page_renders_charts_and_game_comparison(tmp_path, monkeypatch):
    database_path = tmp_path / "statistics-dashboard.db"
    database = GameDatabase(database_path)
    database.insert_games(
        [
            {
                "game_id": 1,
                "name": "Game A",
                "rating": 4.0,
                "released": "2020-01-01",
                "genres": ["Action"],
                "platforms": ["PC"],
                "metacritic": 80,
                "ratings_count": 10,
                "image": None,
            },
            {
                "game_id": 2,
                "name": "Game B",
                "rating": 5.0,
                "released": "2021-01-01",
                "genres": ["RPG"],
                "platforms": ["PC"],
                "metacritic": 90,
                "ratings_count": 20,
                "image": None,
            },
        ]
    )
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")

    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10).run()
    app.button(key="navigation-statistics").click().run()

    assert not app.exception
    assert len(app.subheader) == 6
    assert len(app.dataframe) == 1


def test_statistics_page_handles_an_empty_library(tmp_path, monkeypatch):
    database_path = tmp_path / "empty-statistics-dashboard.db"
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")

    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10).run()
    app.button(key="navigation-statistics").click().run()

    assert not app.exception
    assert any("No data available" in info.value for info in app.info)


@pytest.mark.parametrize("released", ["2020-01-01", None])
def test_library_handles_a_single_or_missing_release_year(tmp_path, monkeypatch, released):
    database_path = tmp_path / "library-years.db"
    GameDatabase(database_path).insert_games([
        {
            "game_id": 1, "name": "Game A", "rating": None,
            "released": released, "genres": [], "platforms": [],
            "metacritic": None, "ratings_count": 0, "image": None,
        }
    ])
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10).run()
    app.button(key="navigation-games").click().run()

    assert not app.exception
    year_field = next(field for field in app.text_input if field.label == "Release year")
    assert year_field.disabled
    assert year_field.value == ("2020" if released else "Unavailable")
    assert any(button.label == "View Details" for button in app.button)


@pytest.mark.parametrize("source_page", ["home", "games", "top_rated", "players", "genres", "search", "detail"])
def test_genre_links_open_the_selected_group_from_every_game_view(tmp_path, monkeypatch, source_page):
    database_path = tmp_path / "genre-links.db"
    database = GameDatabase(database_path)
    game = {
        "game_id": 1, "name": "Game A", "rating": 4.0,
        "released": "2020-01-01", "genres": ["Action", "Role & Play"],
        "platforms": ["PC"], "metacritic": 80, "ratings_count": 10,
        "image": None, "steam_app_id": 1, "steam_lookup_status": "found",
        "current_players": 100, "live_rank": 1,
    }
    database.save_catalog_games([game], updated_at="2026-10-08T10:00:00+07:00")
    database.save_live_top_games([game], "2026-10-08T10:00:00+07:00")
    monkeypatch.setenv("GAMING_DASHBOARD_DB", str(database_path))
    monkeypatch.setenv("GAMING_DASHBOARD_SKIP_REFRESH", "1")
    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py"), default_timeout=10).run()
    if source_page == "search":
        app.session_state["search_results_term"] = "Game A"
        app.session_state["search_results_games"] = database.get_games()
    app.button(key=f"navigation-{'games' if source_page == 'detail' else source_page}").click().run()
    if source_page == "detail":
        next(button for button in app.button if button.label == "View Details").click().run()
    assert not app.exception

    rendered_html = "".join(markdown.value for markdown in app.markdown)
    hrefs = re.findall(r'class="tag genre-link" href="([^"]+)"', rendered_html)
    target = next(href for href in hrefs if parse_qs(urlsplit(href).query)["genre"] == ["Role & Play"])
    # Follow the actual rendered link, including decoding spaces and ampersands.
    app.query_params["genre"] = parse_qs(urlsplit(target).query)["genre"][0]
    app.run()

    assert not app.exception
    assert app.session_state["dashboard_page"] == "genres"
    assert app.expander[0].label == "Role & Play · 1 game(s)"
    assert app.expander[0].proto.expanded
    assert app.session_state["pagination-genre-Role & Play"] == 1
    app.button(key="navigation-games").click().run()
    assert not app.exception
    assert app.session_state["dashboard_page"] == "games"
