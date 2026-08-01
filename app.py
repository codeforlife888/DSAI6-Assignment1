from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Singapore Job Market Dashboard", layout="wide")

DATA_PATH = Path(__file__).resolve().parent / "sample_jobs.csv"
df = pd.read_csv(
    DATA_PATH,
    parse_dates=[
        "metadata_newPostingDate",
        "metadata_originalPostingDate",
        "metadata_expiryDate",
    ],
)

st.title("Singapore Job Market Dashboard")

with st.sidebar:
    st.header("Filters")
    category_options = sorted(df["primary_category"].dropna().unique())
    selected_categories = st.multiselect(
        "Category", category_options, default=category_options
    )


