import streamlit as st
import plotly.express as px

from utils import (
    executive_metrics,
    revenue_by_segment,
    revenue_by_region,
    revenue_by_category,
    monthly_join_trend,
    monthly_revenue,
)

from theme import (
    section,
)


# --------------------------------------------------
# KPI Dashboard
# --------------------------------------------------

def show_kpis(df):

    metrics = executive_metrics(df)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "👥 Customers",
            f"{metrics['customers']:,}"
        )

    with c2:

        st.metric(
            "💰 Revenue",
            f"₹{metrics['revenue']:,.0f}"
        )

    with c3:

        st.metric(
            "⭐ Avg Score",
            f"{metrics['avg_score']:.2f}"
        )

    with c4:

        st.metric(
            "⚠ Avg Churn",
            f"{metrics['avg_churn']:.2f}%"
        )


# --------------------------------------------------
# Revenue Charts
# --------------------------------------------------

def revenue_dashboard(df):

    section("Revenue Analytics")

    left, right = st.columns(2)

    with left:

        chart = revenue_by_segment(df)

        fig = px.bar(

            chart,

            x="Segment",

            y="Total Revenue",

            text_auto=".2s",

            title="Revenue by Segment"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        chart = revenue_by_region(df)

        fig = px.bar(

            chart,

            x="Region",

            y="Total Revenue",

            text_auto=".2s",

            title="Revenue by Region"

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# --------------------------------------------------
# Product Analytics
# --------------------------------------------------

def category_dashboard(df):

    section("Product Analytics")

    chart = revenue_by_category(df)

    fig = px.pie(

        chart,

        names="Favorite Category",

        values="Total Revenue",

        hole=.45,

        title="Revenue by Category"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )
# --------------------------------------------------
# Monthly Trends
# --------------------------------------------------

def trend_dashboard(df):

    section("Business Trends")

    left, right = st.columns(2)

    with left:

        revenue = monthly_revenue(df)

        fig = px.line(

            revenue,

            x="Purchase Month",

            y="Total Revenue",

            markers=True,

            title="Monthly Revenue"

        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Revenue"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with right:

        joins = monthly_join_trend(df)

        fig = px.area(

            joins,

            x="Join Month",

            y="Customers",

            title="Customer Acquisition"

        )

        fig.update_layout(
            xaxis_title="Month",
            yaxis_title="Customers"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# --------------------------------------------------
# Loyalty Dashboard
# --------------------------------------------------

def loyalty_dashboard(df):

    section("Customer Loyalty")

    left, right = st.columns(2)

    with left:

        loyalty = (

            df["Loyalty Level"]

            .value_counts()

            .reset_index()

        )

        loyalty.columns = [

            "Loyalty",

            "Customers"

        ]

        fig = px.bar(

            loyalty,

            x="Loyalty",

            y="Customers",

            color="Customers",

            title="Loyalty Levels"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        ai = (

            df["AI Segment Name"]

            .value_counts()

            .reset_index()

        )

        ai.columns = [

            "Segment",

            "Customers"

        ]

        fig = px.pie(

            ai,

            names="Segment",

            values="Customers",

            hole=.45,

            title="AI Customer Segments"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )


# --------------------------------------------------
# Health Dashboard
# --------------------------------------------------

def health_dashboard(df):

    section("Customer Health")

    left, right = st.columns(2)

    with left:

        fig = px.histogram(

            df,

            x="Health Score",

            nbins=25,

            title="Health Score Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    with right:

        fig = px.histogram(

            df,

            x="Churn Risk",

            nbins=25,

            title="Churn Risk Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )
from ai_engine import (
    generate_business_insights,
    top_customers,
    risky_customers,
    segment_summary,
)

# --------------------------------------------------
# Executive AI Insights
# --------------------------------------------------

def ai_insights_dashboard(df):

    section("🤖 AI Business Insights")

    insights = generate_business_insights(df)

    for insight in insights:
        st.success(insight)


# --------------------------------------------------
# Executive Tables
# --------------------------------------------------

def executive_tables(df):

    section("Executive Reports")

    left, right = st.columns(2)

    with left:

        st.subheader("👑 Top Customers")

        st.dataframe(

            top_customers(df)[
                [
                    "Customer ID",
                    "Name",
                    "Health Score",
                    "Customer Score",
                    "Customer Lifetime Value",
                    "AI Recommendation"
                ]
            ],

            use_container_width=True,

            hide_index=True

        )

    with right:

        st.subheader("⚠ High Risk Customers")

        st.dataframe(

            risky_customers(df)[
                [
                    "Customer ID",
                    "Name",
                    "Churn Risk",
                    "Health Score",
                    "Priority",
                    "AI Recommendation"
                ]
            ],

            use_container_width=True,

            hide_index=True

        )


# --------------------------------------------------
# AI Segment Summary
# --------------------------------------------------

def ai_segment_summary(df):

    section("AI Segment Performance")

    summary = segment_summary(df)

    st.dataframe(

        summary,

        use_container_width=True,

        hide_index=True

    )


# --------------------------------------------------
# Dashboard
# --------------------------------------------------

def show_dashboard(df):

    show_kpis(df)

    st.divider()

    revenue_dashboard(df)

    st.divider()

    trend_dashboard(df)

    st.divider()

    loyalty_dashboard(df)

    st.divider()

    health_dashboard(df)

    st.divider()

    ai_insights_dashboard(df)

    st.divider()

    ai_segment_summary(df)

    st.divider()

    executive_tables(df)