"""Shared Streamlit visual styling for the dashboard."""

from __future__ import annotations

import streamlit as st


def apply_dashboard_styles() -> None:
    """Apply the dashboard's visual system once per Streamlit run."""
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
