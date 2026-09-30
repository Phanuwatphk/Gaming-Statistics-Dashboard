from pathlib import Path
from datetime import UTC, datetime

from streamlit.testing.v1 import AppTest

from src.components.dashboard import _display_timestamp
from src.database.database import GameDatabase


PROJECT_ROOT = Path(__file__).resolve().parents[1]


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
