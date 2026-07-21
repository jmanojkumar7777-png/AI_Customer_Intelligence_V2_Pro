import io
import os
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


DATA_FOLDER = Path("data")
REPORT_FOLDER = Path("reports")

CSV_FILE = DATA_FOLDER / "customer_data.csv"
EXCEL_FILE = DATA_FOLDER / "customer_data.xlsx"


# ---------------------------------------------------
# Data Loading
# ---------------------------------------------------

@st.cache_data(show_spinner=False)
def load_csv(path=CSV_FILE):
    """
    Load CSV dataset.
    """
    return pd.read_csv(path)


@st.cache_data(show_spinner=False)
def load_excel(path=EXCEL_FILE):
    """
    Load Excel dataset.
    """
    return pd.read_excel(path)


def save_csv(df, path=CSV_FILE):
    """
    Save dataframe to CSV.
    """
    df.to_csv(path, index=False)


def save_excel(df, path=EXCEL_FILE):
    """
    Save dataframe to_excel.
    """
    df.to_excel(
        path,
        index=False,
        engine="openpyxl"
    )


# ---------------------------------------------------
# Formatting
# ---------------------------------------------------

def currency(value):
    return f"₹{value:,.2f}"


def percentage(value):
    return f"{value:.2f}%"


def number(value):
    return f"{value:,}"


# ---------------------------------------------------
# Downloads
# ---------------------------------------------------

def dataframe_to_csv(df):

    return df.to_csv(
        index=False
    ).encode("utf-8")


def dataframe_to_excel(df):

    output = io.BytesIO()

    with pd.ExcelWriter(
        output,
        engine="openpyxl"
    ) as writer:

        df.to_excel(
            writer,
            index=False
        )

    return output.getvalue()


# ---------------------------------------------------
# KPIs
# ---------------------------------------------------

def total_customers(df):

    return len(df)


def total_revenue(df):

    return df["Total Revenue"].sum()


def average_revenue(df):

    return df["Total Revenue"].mean()


def average_clv(df):

    return df["Customer Lifetime Value"].mean()


def average_score(df):

    return df["Customer Score"].mean()


def average_churn(df):

    return df["Churn Risk"].mean()


def vip_customers(df):

    return (
        df["Segment"] == "VIP"
    ).sum()


def premium_members(df):

    return (
        df["Premium Member"] == "Yes"
    ).sum()


def subscribed_users(df):

    return (
        df["Newsletter"] == "Subscribed"
    ).sum()
# ---------------------------------------------------
# Customer Filters
# ---------------------------------------------------

def filter_segment(df, segment):

    if segment == "All":
        return df

    return df[df["Segment"] == segment]


def filter_region(df, region):

    if region == "All":
        return df

    return df[df["Region"] == region]


def filter_loyalty(df, level):

    if level == "All":
        return df

    return df[df["Loyalty Level"] == level]


def filter_category(df, category):

    if category == "All":
        return df

    return df[df["Favorite Category"] == category]


# ---------------------------------------------------
# Customer Search
# ---------------------------------------------------

def search_customer(df, keyword):

    keyword = str(keyword).lower().strip()

    if keyword == "":
        return df

    mask = (
        df["Name"].astype(str).str.lower().str.contains(keyword)
        |
        df["Email"].astype(str).str.lower().str.contains(keyword)
        |
        df["Customer ID"].astype(str).str.contains(keyword)
    )

    return df[mask]


# ---------------------------------------------------
# Dashboard Statistics
# ---------------------------------------------------

def segment_distribution(df):

    return (
        df["Segment"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Segment",
                "Segment": "Customers"
            }
        )
    )


def loyalty_distribution(df):

    return (
        df["Loyalty Level"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Loyalty",
                "Loyalty Level": "Customers"
            }
        )
    )


def region_distribution(df):

    return (
        df["Region"]
        .value_counts()
        .reset_index()
        .rename(
            columns={
                "index": "Region",
                "Region": "Customers"
            }
        )
    )


# ---------------------------------------------------
# Revenue Insights
# ---------------------------------------------------

def revenue_by_segment(df):

    return (
        df.groupby("Segment")["Total Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def revenue_by_region(df):

    return (
        df.groupby("Region")["Total Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def revenue_by_category(df):

    return (
        df.groupby("Favorite Category")["Total Revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


# ---------------------------------------------------
# Top Customers
# ---------------------------------------------------

def top_customers(df, n=10):

    return (
        df.sort_values(
            "Customer Lifetime Value",
            ascending=False
        )
        .head(n)
    )


def highest_revenue_customers(df, n=10):

    return (
        df.sort_values(
            "Total Revenue",
            ascending=False
        )
        .head(n)
    )


# ---------------------------------------------------
# Churn Analysis
# ---------------------------------------------------

def high_churn_customers(df, threshold=70):

    return df[
        df["Churn Risk"] >= threshold
    ]


def low_churn_customers(df):

    return df[
        df["Churn Risk"] < 30
    ]


# ---------------------------------------------------
# Customer Health
# ---------------------------------------------------

def healthy_customers(df):

    return df[
        df["Customer Score"] >= 80
    ]


def unhealthy_customers(df):

    return df[
        df["Customer Score"] < 50
    ]
# ---------------------------------------------------
# Executive Dashboard Metrics
# ---------------------------------------------------

def executive_metrics(df):

    return {
        "customers": total_customers(df),
        "revenue": total_revenue(df),
        "avg_revenue": average_revenue(df),
        "avg_clv": average_clv(df),
        "avg_score": average_score(df),
        "avg_churn": average_churn(df),
        "vip": vip_customers(df),
        "premium": premium_members(df),
        "newsletter": subscribed_users(df)
    }


# ---------------------------------------------------
# Dataset Validation
# ---------------------------------------------------

def validate_dataframe(df):

    required_columns = [
        "Customer ID",
        "Name",
        "Total Revenue",
        "Customer Lifetime Value",
        "Customer Score",
        "Churn Risk",
        "Segment",
        "Region",
        "Loyalty Level"
    ]

    missing = []

    for column in required_columns:

        if column not in df.columns:
            missing.append(column)

    return missing


def clean_dataframe(df):

    df = df.copy()

    df.drop_duplicates(inplace=True)

    df.fillna(0, inplace=True)

    return df


# ---------------------------------------------------
# Date Helpers
# ---------------------------------------------------

def convert_dates(df):

    date_columns = [
        "Join Date",
        "Last Purchase"
    ]

    for column in date_columns:

        if column in df.columns:

            df[column] = pd.to_datetime(
                df[column],
                errors="coerce"
            )

    return df


# ---------------------------------------------------
# Summary Statistics
# ---------------------------------------------------

def dataset_summary(df):

    return {

        "rows": len(df),

        "columns": len(df.columns),

        "missing_values":
            int(df.isna().sum().sum()),

        "duplicate_rows":
            int(df.duplicated().sum()),

        "memory_usage_mb":
            round(
                df.memory_usage(deep=True).sum()
                / 1024 / 1024,
                2
            )

    }


# ---------------------------------------------------
# AI Insight Helpers
# ---------------------------------------------------

def best_segment(df):

    revenue = (
        df.groupby("Segment")["Total Revenue"]
        .sum()
    )

    return revenue.idxmax()


def weakest_segment(df):

    revenue = (
        df.groupby("Segment")["Total Revenue"]
        .sum()
    )

    return revenue.idxmin()


def highest_region(df):

    revenue = (
        df.groupby("Region")["Total Revenue"]
        .sum()
    )

    return revenue.idxmax()


def most_popular_category(df):

    return (
        df["Favorite Category"]
        .value_counts()
        .idxmax()
    )


# ---------------------------------------------------
# Chart Helpers
# ---------------------------------------------------

def monthly_join_trend(df):

    temp = df.copy()

    temp["Join Month"] = (
        pd.to_datetime(
            temp["Join Date"]
        )
        .dt.to_period("M")
        .astype(str)
    )

    return (
        temp.groupby("Join Month")
        .size()
        .reset_index(name="Customers")
    )


def monthly_revenue(df):

    temp = df.copy()

    temp["Purchase Month"] = (
        pd.to_datetime(
            temp["Last Purchase"]
        )
        .dt.to_period("M")
        .astype(str)
    )

    return (
        temp.groupby("Purchase Month")["Total Revenue"]
        .sum()
        .reset_index()
    )


# ---------------------------------------------------
# Miscellaneous
# ---------------------------------------------------

def ensure_directories():

    DATA_FOLDER.mkdir(
        exist_ok=True
    )

    REPORT_FOLDER.mkdir(
        exist_ok=True
    )


def load_default_data():

    ensure_directories()

    if CSV_FILE.exists():

        return load_csv()

    return pd.DataFrame()
    