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

    app = AppTest.from_file(str(PROJECT_ROOT / "src" / "app.py")).run()
    app.button(key="navigation-genres").click().run()

    assert not app.exception


def test_display_timestamp_omits_fractional_seconds():
    assert _display_timestamp("2026-09-22T18:17:06.590359+00:00") == "2026-09-22 18:17:06 UTC"
