import streamlit as st
import streamlit.components.v1 as components


GAME_URL = (
    "https://demetriusww.github.io/tcm-ancient-book-puzzle/"
    "?v=streamlit-20261116"
)

st.set_page_config(
    page_title="古籍解谜·中医传承",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
        .stApp {
            background: #23201b;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        footer {
            display: none;
        }

        .block-container {
            max-width: 100%;
            padding: 0;
        }

        iframe {
            display: block;
            border: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

components.iframe(GAME_URL, height=820, scrolling=False)
