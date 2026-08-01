from pathlib import Path
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Singapore Job Market Dashboard", layout="wide")


DATA_PATH = Path(__file__).resolve().parent / "output3.csv"

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

st.title("Singapore Job Market Dashboard")

# Navigation
pg = st.navigation(
    [
        st.Page(
            "pages/overview.py",
            title="Overview",
            icon=":material/dashboard:",
            default=True,
        ),
        st.Page(
            "pages/use_case_1.py", 
            title="Business Case 1", 
            icon=":material/menu_book:"
        ),
        st.Page(
            "pages/use_case_2.py", 
            title="Business Case 2", 
            icon=":material/code:"
        ),
    ]
)
#pg.run()


with st.sidebar:
    st.header("Filters")
    df = load_data()
    category_options = sorted(df["Category"].dropna().unique())
    selected_categories = st.multiselect(
        "Category", category_options, default=category_options
    )