import streamlit as st
import pandas as pd1
import plotly.express as px
from config import load_data


st.title(
    ":material/compare_arrows: Business Case 2: Competition Analysis")
st.markdown(
    "Is there more supply than demand for the IT sector?")

df = load_data()

#itdf = df[df["Category"] == "Information Technology"]


# Create scatter plot
fig = px.scatter(
    df,
    x="Vacancies",        # x-axis: number of vacancies
    y="Total_Applications",     # y-axis: number of applications
    color="Category", # optional: color points by job category
    size="Total_Applications",  # optional: bubble size reflects applications
    hover_name="Total_Applications",  # optional: show job category on hover
    title="Vacancies vs Applications by Job Category"
)

# Improve layout
fig.update_layout(
    xaxis_title="Number of Vacancies",
    yaxis_title="Number of Applications",
    template="plotly_white"
)

# Show the figure
st.plotly_chart(fig)
