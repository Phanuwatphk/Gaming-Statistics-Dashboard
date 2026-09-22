from src.utils.data_processing import process_game, process_games


def test_process_game_normalizes_nested_rawg_fields():
    game = process_game(
        {
            "id": 42,
            "name": "Hades",
            "rating": "4.8",
            "released": "2020-09-17",
            "genres": [{"name": "Action"}, {"name": "Roguelike"}, {"name": "Action"}],
            "platforms": [
                {"platform": {"name": "PC"}},
                {"platform": {"name": "Nintendo Switch"}},
                {"platform": {"name": "PC"}},
            ],
            "metacritic": 93,
            "ratings_count": 1200,
            "background_image": "https://example.test/hades.jpg",
        }
    )

    assert game == {
        "game_id": 42,
        "name": "Hades",
        "rating": 4.8,
        "released": "2020-09-17",
        "genres": ["Action", "Roguelike"],
        "platforms": ["PC", "Nintendo Switch"],
        "metacritic": 93,
        "ratings_count": 1200,
        "image": "https://example.test/hades.jpg",
    }


def test_process_game_handles_missing_optional_values_safely():
    game = process_game({"id": "7", "name": None, "genres": None, "platforms": []})

    assert game is not None
    assert game["game_id"] == 7
    assert game["name"] == "Unknown game"
    assert game["genres"] == []
    assert game["platforms"] == []
    assert game["rating"] is None


def test_process_games_skips_records_without_a_game_id():
    assert process_games([{"name": "Missing ID"}, {"id": 3, "name": "Valid"}]) == [
        {
            "game_id": 3,
            "name": "Valid",
            "rating": None,
            "released": None,
            "genres": [],
            "platforms": [],
            "metacritic": None,
            "ratings_count": None,
            "image": None,
        }
    ]
