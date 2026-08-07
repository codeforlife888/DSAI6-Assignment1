from pathlib import Path
import pandas as pd
import streamlit as st
from config import load_data

st.set_page_config(page_title="Singapore Job Market Dashboard", layout="wide")



# Navigation
pg = st.navigation(
    [
        st.Page(
            "pages/overview.py",
            title="Overview",
            icon=":material/overview:",
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
            icon=":material/menu_book:"
        ),
        st.Page(
            "pages/use_case_3.py", 
            title="Business Case 3", 
            icon=":material/menu_book:"
        ),
        st.Page(
            "pages/use_case_4.py", 
            title="Business Case 4", 
            icon=":material/menu_book:"
        ),

        st.Page(
            "pages/use_case_5.py", 
            title="Business Case 5", 
            icon=":material/menu_book:"
        ),
    ]
)
pg.run()


# with st.sidebar:
#     st.header("Filters")
#     df = load_data()
#     category_options = sorted(df["Category"].dropna().unique())
#     selected_categories = st.multiselect(
#         "Category", category_options, default=category_options
#     )