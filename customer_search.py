import streamlit as st
import pandas as pd

from utils import (
    search_customer,
    currency,
    percentage,
)

# -----------------------------------------------------
# Customer Search
# -----------------------------------------------------

def customer_search(df):

    st.subheader("🔍 Customer Search")

    keyword = st.text_input(
        "Search by Name, Email or Customer ID"
    )

    result = search_customer(
        df,
        keyword
    )

    if keyword and result.empty:

        st.warning(
            "No customer found."
        )

    return result


# -----------------------------------------------------
# Customer Selector
# -----------------------------------------------------

def customer_selector(df):

    customers = (
        df["Name"]
        .sort_values()
        .tolist()
    )

    selected = st.selectbox(

        "Select Customer",

        customers

    )

    return df[
        df["Name"] == selected
    ].iloc[0]


# -----------------------------------------------------
# Profile Card
# -----------------------------------------------------

def profile_card(customer):

    st.markdown("---")

    st.subheader("👤 Customer Profile")

    c1, c2 = st.columns(2)

    with c1:

        st.write(
            f"**Customer ID:** {customer['Customer ID']}"
        )

        st.write(
            f"**Name:** {customer['Name']}"
        )

        st.write(
            f"**Email:** {customer['Email']}"
        )

        st.write(
            f"**Phone:** {customer['Phone']}"
        )

        st.write(
            f"**City:** {customer['City']}"
        )

        st.write(
            f"**Region:** {customer['Region']}"
        )

    with c2:

        st.write(
            f"**Segment:** {customer['Segment']}"
        )

        st.write(
            f"**AI Segment:** {customer['AI Segment Name']}"
        )

        st.write(
            f"**Loyalty:** {customer['Loyalty Level']}"
        )

        st.write(
            f"**Priority:** {customer['Priority']}"
        )

        st.write(
            f"**Health Score:** {customer['Health Score']}"
        )

        st.write(
            f"**Churn Level:** {customer['Churn Level']}"
        )

# -----------------------------------------------------
# KPI Cards
# -----------------------------------------------------

def customer_metrics(customer):

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(

            "Revenue",

            currency(
                customer["Total Revenue"]
            )

        )

    with c2:

        st.metric(

            "CLV",

            currency(
                customer["Customer Lifetime Value"]
            )

        )

    with c3:

        st.metric(

            "Customer Score",

            round(
                customer["Customer Score"],
                2
            )

        )

    with c4:

        st.metric(

            "Churn",

            percentage(
                customer["Churn Risk"]
            )

        )


# -----------------------------------------------------
# Purchase Information
# -----------------------------------------------------

def purchase_information(customer):

    st.subheader("🛒 Purchase Summary")

    left, right = st.columns(2)

    with left:

        st.write(
            f"**Orders:** {customer['Orders']}"
        )

        st.write(
            f"**Average Order Value:** {currency(customer['Average Order Value'])}"
        )

        st.write(
            f"**Favorite Category:** {customer['Favorite Category']}"
        )

    with right:

        st.write(
            f"**Payment Method:** {customer['Payment Method']}"
        )

        st.write(
            f"**Referral Count:** {customer['Referral Count']}"
        )

        st.write(
            f"**Returns:** {customer['Returns']}"
        )


# -----------------------------------------------------
# AI Recommendation
# -----------------------------------------------------

def ai_recommendation(customer):

    st.subheader("🤖 AI Recommendation")

    st.info(
        customer["AI Recommendation"]
    )


# -----------------------------------------------------
# Complete Page
# -----------------------------------------------------

def customer_search_page(df):

    results = customer_search(df)

    if results.empty:

        return

    customer = customer_selector(results)

    profile_card(customer)

    customer_metrics(customer)

    purchase_information(customer)

    ai_recommendation(customer)

