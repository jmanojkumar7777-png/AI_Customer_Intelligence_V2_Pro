import pandas as pd
import streamlit as st

from utils import (
    save_csv,
    save_excel,
    validate_dataframe,
    clean_dataframe,
    convert_dates,
)


SUPPORTED_TYPES = [
    "csv",
    "xlsx",
]


def upload_dataset():

    st.subheader("📂 Upload Customer Dataset")

    uploaded = st.file_uploader(
        "Choose CSV or Excel File",
        type=SUPPORTED_TYPES
    )

    if uploaded is None:
        return None

    try:

        if uploaded.name.endswith(".csv"):

            df = pd.read_csv(uploaded)

        else:

            df = pd.read_excel(uploaded)

        df = clean_dataframe(df)

        df = convert_dates(df)

        missing = validate_dataframe(df)

        if missing:

            st.error(
                "Missing Required Columns:"
            )

            for column in missing:
                st.write(f"• {column}")

            return None

        st.success("Dataset Loaded Successfully!")

        return df

    except Exception as e:

        st.error(str(e))

        return None


def save_uploaded_dataset(df):

    try:

        save_csv(df)

        save_excel(df)

        st.success(
            "Dataset Saved Successfully!"
        )

    except Exception as e:

        st.error(str(e))


def dataset_preview(df):

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )


def dataset_information(df):

    st.subheader("ℹ Dataset Information")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Rows",
            len(df)
        )

    with c2:

        st.metric(
            "Columns",
            len(df.columns)
        )

    with c3:

        memory = round(
            df.memory_usage(deep=True).sum()
            / 1024 / 1024,
            2
        )

        st.metric(
            "Memory (MB)",
            memory
        )


def show_missing_values(df):

    missing = df.isna().sum()

    missing = missing[
        missing > 0
    ]

    st.subheader("Missing Values")

    if len(missing) == 0:

        st.success(
            "No Missing Values Found."
        )

    else:

        st.dataframe(
            missing.to_frame(
                "Missing"
            )
        )


def data_quality(df):

    st.subheader("Data Quality")

    duplicate_rows = df.duplicated().sum()

    st.metric(
        "Duplicate Rows",
        duplicate_rows
    )

    if duplicate_rows == 0:

        st.success(
            "Dataset looks clean."
        )

    else:

        st.warning(
            "Duplicates detected."
        )


def upload_page():

    df = upload_dataset()

    if df is None:
        return None

    dataset_information(df)

    show_missing_values(df)

    data_quality(df)

    dataset_preview(df)

    if st.button("💾 Save Dataset"):

        save_uploaded_dataset(df)

    return df