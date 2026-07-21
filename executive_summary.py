import streamlit as st

from ai_engine import (
    executive_summary,
    generate_business_insights
)

from utils import currency


# --------------------------------------------------
# Executive Summary Page
# --------------------------------------------------

def show_executive_summary(df):

    st.header("📋 Executive Summary")

    summary = executive_summary(df)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Customers",
            f"{summary['Total Customers']:,}"
        )

        st.metric(
            "Average Revenue",
            currency(
                summary["Average Revenue"]
            )
        )

    with c2:

        st.metric(
            "Average CLV",
            currency(
                summary["Average CLV"]
            )
        )

        st.metric(
            "Average Customer Score",
            f"{summary['Average Customer Score']:.2f}"
        )

    with c3:

        st.metric(
            "Average Health Score",
            f"{summary['Average Health Score']:.2f}"
        )

        st.metric(
            "Average Churn",
            f"{summary['Average Churn']:.2f}%"
        )

    st.divider()

    st.subheader("🏆 Business Highlights")

    st.success(
        f"Highest Revenue Segment : {summary['Highest Revenue Segment']}"
    )

    st.success(
        f"Most Loyal Segment : {summary['Most Loyal Segment']}"
    )

    st.divider()

    st.subheader("🤖 AI Recommendations")

    insights = generate_business_insights(df)

    for insight in insights:

        st.info(insight)

    st.divider()

    st.subheader("📌 Executive Notes")

    st.markdown("""
### Key Takeaways

- Continue investing in the highest-performing customer segment.
- Focus retention campaigns on customers with elevated churn risk.
- Increase personalized offers for high-value customers.
- Expand marketing in the best-performing region.
- Reward loyal customers through VIP and referral programs.
- Monitor customer health score weekly for early intervention.
""")