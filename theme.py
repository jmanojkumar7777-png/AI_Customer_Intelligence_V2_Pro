from pathlib import Path

import streamlit as st


CSS_FILE = Path("assets/style.css")


def configure_page():

    st.set_page_config(
        page_title="AI Customer Intelligence Platform V2 Pro",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def load_css():

    if CSS_FILE.exists():

        with open(CSS_FILE, encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


def initialize_theme():

    configure_page()

    load_css()


# ----------------------------------------------------
# Headers
# ----------------------------------------------------

def page_title(title, subtitle=""):

    st.markdown(
        f"""
        <div class="glass-card">
            <h1>{title}</h1>
            <p style="color:#cbd5e1;font-size:18px;">
                {subtitle}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


def section(title):

    st.markdown(
        f"""
        <div style="padding-top:20px;">
        <h2>{title}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


# ----------------------------------------------------
# KPI Cards
# ----------------------------------------------------

def metric_card(title, value):

    st.markdown(
        f"""
        <div class="metric-card">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


def info_card(title, value):

    st.markdown(
        f"""
        <div class="glass-card">
            <h3>{title}</h3>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )


# ----------------------------------------------------
# Messages
# ----------------------------------------------------

def success(message):

    st.success(message)


def warning(message):

    st.warning(message)


def error(message):

    st.error(message)


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

def sidebar_title():

    st.sidebar.markdown(
        """
        # 🤖 AI Customer
        ### Intelligence Platform

        ---
        """,
        unsafe_allow_html=True
    )


def sidebar_footer():

    st.sidebar.markdown("---")

    st.sidebar.caption(
        "Version 2 Pro"
    )


# ----------------------------------------------------
# Footer
# ----------------------------------------------------

def footer():
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align:center;
                    padding:20px;
                    color:#B8C1CC;
                    font-size:16px;">
            🤖 <b>AI Customer Intelligence Platform V2 Pro</b><br>
            Created with ❤️ by <span style="color:#4F9DFF;"><b>Manoj Kumar</b></span>
        </div>
        """,
        unsafe_allow_html=True,
    )