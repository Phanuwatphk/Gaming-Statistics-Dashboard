"""Convert nested RAWG records into the application's predictable game shape."""

from __future__ import annotations

from typing import Any


def process_games(raw_games: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Normalize valid RAWG records and skip records without a usable game ID."""
    processed_games = []
    for raw_game in raw_games:
        game = process_game(raw_game)
        if game is not None:
            processed_games.append(game)
    return processed_games


def process_game(raw_game: dict[str, Any]) -> dict[str, Any] | None:
    """Normalize one RAWG game while preserving missing optional fields as None."""
    game_id = _as_int(raw_game.get("id"))
    if game_id is None:
        return None

    return {
        "game_id": game_id,
        "name": _text_or_default(raw_game.get("name"), "Unknown game"),
        "rating": _as_float(raw_game.get("rating")),
        "released": _text_or_none(raw_game.get("released")),
        "genres": _nested_names(raw_game.get("genres")),
        "platforms": _platform_names(raw_game.get("platforms")),
        "metacritic": _as_int(raw_game.get("metacritic")),
        "ratings_count": _as_int(raw_game.get("ratings_count")),
        "image": _text_or_none(raw_game.get("background_image")),
    }


def _nested_names(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    return _unique_names(item.get("name") for item in items if isinstance(item, dict))


def _platform_names(items: Any) -> list[str]:
    if not isinstance(items, list):
        return []
    names = []
    for item in items:
        platform = item.get("platform") if isinstance(item, dict) else None
        if isinstance(platform, dict):
            names.append(platform.get("name"))
    return _unique_names(names)


def _unique_names(names: Any) -> list[str]:
    result: list[str] = []
    for name in names:
        cleaned = _text_or_none(name)
        if cleaned and cleaned not in result:
            result.append(cleaned)
    return result


def _text_or_none(value: Any) -> str | None:
    text = str(value).strip() if value is not None else ""
    return text or None


def _text_or_default(value: Any, default: str) -> str:
    return _text_or_none(value) or default


def _as_int(value: Any) -> int | None:
    try:
        return int(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def _as_float(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None
