import streamlit as st

from theme import (
    initialize_theme,
    sidebar_title,
    sidebar_footer,
    page_title,
)

from utils import (
    load_default_data,
)

from upload_data import (
    upload_page,
)

from ai_engine import (
    run_ai_pipeline,
)

from dashboard import (
    show_dashboard,
)

from customer_search import (
    customer_search_page,
)

from executive_summary import (
    show_executive_summary,
)

from report_generator import (
    report_page,
)


# ---------------------------------------------
# Initialize
# ---------------------------------------------

initialize_theme()

sidebar_title()

page_title(

    "🤖 AI Customer Intelligence Platform V2 Pro",

    "Production-ready AI Analytics Platform"

)


# ---------------------------------------------
# Sidebar Navigation
# ---------------------------------------------

menu = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Dashboard",

        "🔍 Customer Search",

        "📂 Upload Dataset",

        "📋 Executive Summary",

        "📄 Reports"

    ]

)


# ---------------------------------------------
# Load Default Dataset
# ---------------------------------------------

if "customer_df" not in st.session_state:

    df = load_default_data()

    if not df.empty:

        df = run_ai_pipeline(df)

    st.session_state.customer_df = df


df = st.session_state.customer_df

# ---------------------------------------------
# Dashboard
# ---------------------------------------------

if menu == "🏠 Dashboard":

    if df.empty:

        st.warning(
            "No dataset found. Please upload a dataset first."
        )

    else:

        show_dashboard(df)


# ---------------------------------------------
# Customer Search
# ---------------------------------------------

elif menu == "🔍 Customer Search":

    if df.empty:

        st.warning(
            "No dataset available."
        )

    else:

        customer_search_page(df)


# ---------------------------------------------
# Upload Dataset
# ---------------------------------------------

elif menu == "📂 Upload Dataset":

    uploaded_df = upload_page()

    if uploaded_df is not None:

        with st.spinner("Running AI Analysis..."):

            uploaded_df = run_ai_pipeline(uploaded_df)

        st.session_state.customer_df = uploaded_df

        df = uploaded_df

        st.success(
            "AI Analysis Completed Successfully!"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

        st.info(
            "Your uploaded dataset is now being used throughout the application."
        )

# ---------------------------------------------
# Executive Summary
# ---------------------------------------------

elif menu == "📋 Executive Summary":

    if df.empty:

        st.warning(
            "No dataset available."
        )

    else:

        show_executive_summary(df)


# ---------------------------------------------
# Reports
# ---------------------------------------------

elif menu == "📄 Reports":

    if df.empty:

        st.warning(
            "No dataset available."
        )

    else:

        report_page(df)


# ---------------------------------------------
# Footer
# ---------------------------------------------

st.sidebar.markdown("---")

st.sidebar.success("🟢 System Status: Online")

st.sidebar.caption(
    "AI Customer Intelligence Platform V2 Pro"
)

st.sidebar.caption(
    "Version 2.0"
)

sidebar_footer()