from pathlib import Path
import pandas as pd
import streamlit as st

DATA_PATH = Path(__file__).resolve().parent / "output4.csv"

@st.cache_data
def load_data():
    return pd.read_csv(
        DATA_PATH,
        parse_dates=[
            "New_Post_Date",
            "Orig_Post_Date",
            "Expiry_Date",
        ],
        sep=";"
    )