import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# --------------------------------------------------
# Features used for Machine Learning
# --------------------------------------------------

ML_FEATURES = [
    "Total Revenue",
    "Customer Lifetime Value",
    "Orders",
    "Customer Score",
    "Churn Risk",
    "Satisfaction Score",
    "Website Visits",
    "App Sessions",
    "Referral Count",
    "Returns",
]


# --------------------------------------------------
# Data Preparation
# --------------------------------------------------

def prepare_features(df):

    """
    Prepare dataframe for ML.
    """

    data = df[ML_FEATURES].copy()

    data = data.fillna(0)

    scaler = StandardScaler()

    scaled = scaler.fit_transform(data)

    return scaled, scaler


# --------------------------------------------------
# KMeans Segmentation
# --------------------------------------------------

def build_segmentation(df, clusters=5):

    """
    Perform customer segmentation.
    """

    features, scaler = prepare_features(df)

    model = KMeans(

        n_clusters=clusters,

        random_state=42,

        n_init="auto"

    )

    labels = model.fit_predict(features)

    result = df.copy()

    result["AI Segment"] = labels

    return result, model, scaler


# --------------------------------------------------
# Segment Labels
# --------------------------------------------------

SEGMENT_NAMES = {

    0: "High Value",

    1: "Growing",

    2: "At Risk",

    3: "Loyal",

    4: "New Customers"

}


def segment_name(cluster):

    return SEGMENT_NAMES.get(

        cluster,

        "Unknown"

    )


def add_segment_names(df):

    df = df.copy()

    df["AI Segment Name"] = (

        df["AI Segment"]

        .map(segment_name)

    )

    return df


# --------------------------------------------------
# Customer Health Score
# --------------------------------------------------

def health_score(row):

    score = (

        row["Customer Score"] * 0.45

        +

        (100 - row["Churn Risk"]) * 0.30

        +

        row["Satisfaction Score"] * 20 * 0.25

    )

    return round(

        min(score, 100),

        2

    )


def add_health_score(df):

    df = df.copy()

    df["Health Score"] = (

        df.apply(

            health_score,

            axis=1

        )

    )

    return df

# --------------------------------------------------
# AI Recommendation Engine
# --------------------------------------------------

def recommendation(row):

    recommendations = []

    if row["Churn Risk"] >= 70:
        recommendations.append(
            "Launch a retention campaign."
        )

    if row["Customer Score"] >= 90:
        recommendations.append(
            "Offer an exclusive VIP reward."
        )

    if row["Customer Lifetime Value"] >= 300000:
        recommendations.append(
            "Assign a dedicated relationship manager."
        )

    if row["Orders"] <= 5:
        recommendations.append(
            "Recommend best-selling products."
        )

    if row["Referral Count"] >= 10:
        recommendations.append(
            "Invite to referral rewards program."
        )

    if row["Satisfaction Score"] < 3.5:
        recommendations.append(
            "Schedule customer success follow-up."
        )

    if row["Website Visits"] > 150 and row["Orders"] < 10:
        recommendations.append(
            "Send personalized conversion offers."
        )

    if row["Cart Abandonments"] >= 10:
        recommendations.append(
            "Recover abandoned carts with discounts."
        )

    if not recommendations:
        recommendations.append(
            "Maintain regular engagement."
        )

    return " | ".join(recommendations)


def add_recommendations(df):

    df = df.copy()

    df["AI Recommendation"] = df.apply(
        recommendation,
        axis=1
    )

    return df


# --------------------------------------------------
# Customer Priority
# --------------------------------------------------

def customer_priority(row):

    if (
        row["Customer Score"] >= 90
        and row["Churn Risk"] < 30
    ):
        return "Highest"

    if row["Customer Score"] >= 75:
        return "High"

    if row["Customer Score"] >= 55:
        return "Medium"

    return "Low"


def add_priority(df):

    df = df.copy()

    df["Priority"] = df.apply(
        customer_priority,
        axis=1
    )

    return df


# --------------------------------------------------
# Churn Classification
# --------------------------------------------------

def churn_level(value):

    if value >= 80:
        return "Critical"

    if value >= 60:
        return "High"

    if value >= 40:
        return "Moderate"

    return "Low"


def add_churn_levels(df):

    df = df.copy()

    df["Churn Level"] = (
        df["Churn Risk"]
        .apply(churn_level)
    )

    return df


# --------------------------------------------------
# Loyalty Intelligence
# --------------------------------------------------

def loyalty_index(row):

    score = (
        row["Orders"] * 2
        +
        row["Referral Count"] * 4
        +
        row["Satisfaction Score"] * 10
        -
        row["Returns"] * 2
    )

    return round(
        max(0, min(score, 100)),
        2
    )


def add_loyalty_index(df):

    df = df.copy()

    df["Loyalty Index"] = df.apply(
        loyalty_index,
        axis=1
    )

    return df

# --------------------------------------------------
# Executive AI Insights
# --------------------------------------------------

def executive_summary(df):

    summary = {}

    summary["Total Customers"] = len(df)

    summary["Average Revenue"] = round(
        df["Total Revenue"].mean(),
        2
    )

    summary["Average CLV"] = round(
        df["Customer Lifetime Value"].mean(),
        2
    )

    summary["Average Customer Score"] = round(
        df["Customer Score"].mean(),
        2
    )

    summary["Average Health Score"] = round(
        df["Health Score"].mean(),
        2
    )

    summary["Average Churn"] = round(
        df["Churn Risk"].mean(),
        2
    )

    summary["Highest Revenue Segment"] = (
        df.groupby("Segment")["Total Revenue"]
        .sum()
        .idxmax()
    )

    summary["Most Loyal Segment"] = (
        df.groupby("Segment")["Loyalty Index"]
        .mean()
        .idxmax()
    )

    return summary


# --------------------------------------------------
# AI Insights
# --------------------------------------------------

def generate_business_insights(df):

    insights = []

    churn = df["Churn Risk"].mean()

    if churn > 50:
        insights.append(
            "⚠ High churn detected. Increase customer retention campaigns."
        )
    else:
        insights.append(
            "✅ Customer churn is under control."
        )

    vip = (df["Segment"] == "VIP").sum()

    insights.append(
        f"👑 VIP Customers: {vip}"
    )

    premium = (
        df["Premium Member"] == "Yes"
    ).sum()

    insights.append(
        f"⭐ Premium Members: {premium}"
    )

    highest_region = (
        df.groupby("Region")["Total Revenue"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"📍 Best Performing Region: {highest_region}"
    )

    category = (
        df.groupby("Favorite Category")["Total Revenue"]
        .sum()
        .idxmax()
    )

    insights.append(
        f"🛍 Top Category: {category}"
    )

    return insights


# --------------------------------------------------
# Segment Summary
# --------------------------------------------------

def segment_summary(df):

    return (
        df.groupby("AI Segment Name")
        .agg(
            Customers=("Customer ID", "count"),
            Revenue=("Total Revenue", "sum"),
            AvgScore=("Customer Score", "mean"),
            AvgHealth=("Health Score", "mean"),
            AvgChurn=("Churn Risk", "mean")
        )
        .reset_index()
    )


# --------------------------------------------------
# AI Pipeline
# --------------------------------------------------

def run_ai_pipeline(df):

    df, model, scaler = build_segmentation(df)

    df = add_segment_names(df)

    df = add_health_score(df)

    df = add_recommendations(df)

    df = add_priority(df)

    df = add_churn_levels(df)

    df = add_loyalty_index(df)

    return df


# --------------------------------------------------
# Top Customers
# --------------------------------------------------

def top_customers(df, n=10):

    return (
        df.sort_values(
            "Health Score",
            ascending=False
        )
        .head(n)
    )


def risky_customers(df, n=10):

    return (
        df.sort_values(
            "Churn Risk",
            ascending=False
        )
        .head(n)
    )


# --------------------------------------------------
# Dashboard Metrics
# --------------------------------------------------

def dashboard_metrics(df):

    return {

        "customers": len(df),

        "revenue": float(
            df["Total Revenue"].sum()
        ),

        "clv": float(
            df["Customer Lifetime Value"].mean()
        ),

        "score": float(
            df["Customer Score"].mean()
        ),

        "health": float(
            df["Health Score"].mean()
        ),

        "churn": float(
            df["Churn Risk"].mean()
        ),

        "vip": int(
            (df["Segment"] == "VIP").sum()
        ),

        "premium": int(
            (df["Premium Member"] == "Yes").sum()
        )

    }
