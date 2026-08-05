from pathlib import Path
import streamlit as st
import pandas as pd1
import plotly.express as px
from plotly.subplots import make_subplots
from config  import load_data


st.title(
    ":material/work: Business Case 1: Top roles by vacancies")

st.markdown(
    "Which are the top 10 categories?")

df = load_data()
filter_df = df.groupby("Category").agg({"Vacancies": "sum"}).reset_index()
order_df = filter_df.sort_values(by="Vacancies", ascending=False).head(15)
# Create bar chart
fig = px.bar(
    order_df,
    x="Category",   # categories on x-axis
    y="Vacancies",      # number of vacancies on y-axis
    title="Job Vacancies by Category",
    text="Vacancies"    # show vacancy numbers on bars
)

# Improve layout
fig.update_layout(
    xaxis_title="Job Category",
    yaxis_title="Number of Vacancies",
    template="plotly_white"
)

# Show the figure
st.plotly_chart(fig)
