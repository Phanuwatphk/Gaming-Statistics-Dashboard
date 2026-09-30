from analysis.statistics import (
    comparison_dataframe,
    frequency_with_proportion,
    numeric_values,
    top_current_players,
    descriptive_statistics,
    genre_frequency,
    genre_rating_mean,
    platform_frequency,
    release_year_frequency,
)

import altair as alt
import pandas as pd
import streamlit as st
from typing import Any


def render_statistics_page(games: list[dict[str, Any]]) -> None:
    """Render the statistics route using already-loaded game records."""
    st.title("Statistics")
    st.caption("Explore descriptive statistics, distributions, and game comparisons.")

    if not games:
        st.info("No data available. Add games through Search before viewing statistics.")
        return

    stats = descriptive_statistics(games)

    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Rated games", stats["count"])
    c2.metric("Average Rating", f'{stats["mean"]:.2f}' if stats["mean"] is not None else "N/A")
    c3.metric("Median Rating", f'{stats["median"]:.2f}' if stats["median"] is not None else "N/A")
    c4.metric("Highest Rating", f'{stats["max"]:.2f}' if stats["max"] is not None else "N/A")
    c5.metric("Lowest Rating", f'{stats["min"]:.2f}' if stats["min"] is not None else "N/A")

    st.subheader("Genre Distribution")
    genre_data = genre_frequency(games)
    if not genre_data.empty:
        genre_df = frequency_with_proportion(genre_data).head(10).rename(
            columns={"label": "Genre", "count": "Count", "proportion": "Share"}
        )

        genre_chart = (
            alt.Chart(genre_df)
            .mark_bar()
            .encode(
                x=alt.X("Genre:N", sort="-y"),
                y=alt.Y(
                    "Count:Q",
                    title="Games",
                ),
                tooltip=["Genre", "Count", alt.Tooltip("Share:Q", format=".1%")],
            )
        )

        st.altair_chart(genre_chart, width="stretch")
    else:
        st.info("No genre data available.")


    st.subheader("Platform Distribution")

    platform_data = platform_frequency(games)

    if not platform_data.empty:
        platform_df = frequency_with_proportion(platform_data).head(10).rename(
            columns={"label": "Platform", "count": "Count", "proportion": "Share"}
        )

        platform_chart = (
            alt.Chart(platform_df)
            .mark_bar()
            .encode(
                x=alt.X("Platform:N", sort="-y"),
                y=alt.Y(
                    "Count:Q",
                    title="Games",
                ),
                tooltip=["Platform", "Count", alt.Tooltip("Share:Q", format=".1%")] ,
            )
        )

        st.altair_chart(platform_chart, width="stretch")
    else:
        st.info("No platform data available.")


    st.subheader("Rating by Genre")

    rating_data = genre_rating_mean(games).head(10)

    if not rating_data.empty:
        rating_df = rating_data.rename("Average Rating").reset_index()
        rating_df.columns = ["Genre", "Average Rating"]

        rating_chart = (
            alt.Chart(rating_df)
            .mark_bar()
            .encode(
                x=alt.X("Genre:N", sort="-y"),
                y=alt.Y(
                    "Average Rating:Q",
                    scale=alt.Scale(domain=[0, 5]),
                    title="Rating",
                ),
                tooltip=["Genre", "Average Rating"],
            )
        )

        st.altair_chart(rating_chart, width="stretch")
    else:
        st.info("No rating-by-genre data available.")


    st.subheader("Release Year Distribution")

    year_data = release_year_frequency(games)

    if not year_data.empty:
        year_df = year_data.rename("Games").reset_index()
        year_df.columns = ["Year", "Games"]

        year_chart = (
            alt.Chart(year_df)
            .mark_line(point=True)
            .encode(
                x=alt.X("Year:O", title="Release Year"),
                y=alt.Y(
                    "Games:Q",
                    title="Games",
                ),
                tooltip=["Year", "Games"],
            )
        )

        st.altair_chart(year_chart, width="stretch")
    else:
        st.info("No release-year data available.")

    _render_metacritic_distribution(games)
    _render_live_player_chart(games)

    game_names = sorted(game["name"] for game in games)

    col1, col2 = st.columns(2)
    with col1:
        game_a = st.selectbox("Game A", game_names, key="comparison-game-a")
    with col2:
        game_b = st.selectbox(
            "Game B",
            game_names,
            index=1 if len(game_names) > 1 else 0,
            key="comparison-game-b",
        )

    a = next(game for game in games if game["name"] == game_a)
    b = next(game for game in games if game["name"] == game_b)

    comparison = comparison_dataframe(a, b)

    st.dataframe(comparison, hide_index=True, width="stretch")



def _render_metacritic_distribution(games: list[dict[str, Any]]) -> None:
    st.subheader("Metacritic score distribution")
    scores = numeric_values(games, "metacritic")
    if scores.empty:
        st.info("No Metacritic data available.")
        return
    data = pd.DataFrame({"Metacritic score": scores})
    chart = (
        alt.Chart(data)
        .mark_bar(color="#845ec2")
        .encode(
            x=alt.X("Metacritic score:Q", bin=alt.Bin(maxbins=10), title="Metacritic score"),
            y=alt.Y("count():Q", title="Games"),
            tooltip=[alt.Tooltip("count():Q", title="Games")],
        )
    )
    st.altair_chart(chart, width="stretch")


def _render_live_player_chart(games: list[dict[str, Any]]) -> None:
    st.subheader("Top live Steam players")
    data = top_current_players(games)
    if data.empty:
        st.info("No live Steam-player data available.")
        return
    chart = (
        alt.Chart(data)
        .mark_bar(color="#00a6a6")
        .encode(
            x=alt.X("Game:N", sort="-y", title=None, axis=alt.Axis(labelAngle=-35)),
            y=alt.Y("Current Players:Q", title="Players"),
            tooltip=["Game", alt.Tooltip("Current Players:Q", format=",")],
        )
    )
    st.altair_chart(chart, width="stretch")
