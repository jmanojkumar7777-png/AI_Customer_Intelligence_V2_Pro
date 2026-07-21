import io
from datetime import datetime

import pandas as pd
import streamlit as st

from ai_engine import executive_summary
from utils import (
    currency,
    dataframe_to_csv,
    dataframe_to_excel,
)


# --------------------------------------------------
# Executive Report
# --------------------------------------------------

def create_report(df):

    summary = executive_summary(df)

    report = pd.DataFrame({

        "Metric": [

            "Total Customers",
            "Average Revenue",
            "Average CLV",
            "Average Customer Score",
            "Average Health Score",
            "Average Churn",
            "Highest Revenue Segment",
            "Most Loyal Segment"

        ],

        "Value": [

            summary["Total Customers"],

            currency(summary["Average Revenue"]),

            currency(summary["Average CLV"]),

            round(
                summary["Average Customer Score"],
                2
            ),

            round(
                summary["Average Health Score"],
                2
            ),

            f"{summary['Average Churn']:.2f}%",

            summary["Highest Revenue Segment"],

            summary["Most Loyal Segment"]

        ]

    })

    return report


# --------------------------------------------------
# Download Report
# --------------------------------------------------

def download_report(df):

    report = create_report(df)

    st.subheader("📄 Executive Report")

    st.dataframe(

        report,

        use_container_width=True,

        hide_index=True

    )

    csv = dataframe_to_csv(report)

    excel = dataframe_to_excel(report)

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(

            "⬇ Download Report (CSV)",

            csv,

            file_name=f"Executive_Report_{datetime.now().date()}.csv",

            mime="text/csv"

        )

    with col2:

        st.download_button(

            "⬇ Download Report (Excel)",

            excel,

            file_name=f"Executive_Report_{datetime.now().date()}.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )


# --------------------------------------------------
# Download Dataset
# --------------------------------------------------

def download_dataset(df):

    st.subheader("📦 Download Dataset")

    csv = dataframe_to_csv(df)

    excel = dataframe_to_excel(df)

    left, right = st.columns(2)

    with left:

        st.download_button(

            "⬇ Download Customer CSV",

            csv,

            file_name="customer_data.csv",

            mime="text/csv"

        )

    with right:

        st.download_button(

            "⬇ Download Customer Excel",

            excel,

            file_name="customer_data.xlsx",

            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        )


# --------------------------------------------------
# Complete Report Page
# --------------------------------------------------

def report_page(df):

    st.header("📊 Reports")

    download_report(df)

    st.divider()

    download_dataset(df)