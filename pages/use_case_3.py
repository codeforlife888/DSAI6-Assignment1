# All Content/ Filters / Charts for Use Case 3 goes here :
# Question 3b: What budgetary salary should our company plan for headcounts and specialists (Industry benchmark)?
# Business Objective
# A startup plan their talent budget for operation based on industry benchmark.
# Dataset Columns
# Category_single, Employment types, MinimumYearsExperience, average_salary
# Visualization
# Box Plot - Mean, Max, Min average_salary by Category_single, Role and Experience
# Bar Chart (Average Salary by Role)
# Interactive Filters
# Select box for several options under category_single, role; slider for MinimumYearsExperience
# Story
# This establishes a realistic salary budget for operation.
# Example Insight
# Cybersecurity and Cloud Engineers with 5 years experience. What are the median, min or max salary per headcount

import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path


# DATA_PATH = "/home/kyo/DSAI6-Assignment1/output3.csv"
DATA_PATH = Path(__file__).resolve().parent.parent / "output3.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(
        DATA_PATH,
        sep=";",
        parse_dates=["Expiry_Date", "New_Post_Date", "Orig_Post_Date"],
        dayfirst=True,
        encoding="utf-8",
    )
    df["Avg_Salary"] = pd.to_numeric(df["Avg_Salary"], errors="coerce")
    df["Min_Yrs_Experience"] = pd.to_numeric(df["Min_Yrs_Experience"], errors="coerce")
    return df

df = load_data()

# --- Use Case 3b: Salary benchmark for talent budgeting ---
st.subheader("Salary Benchmark for Headcount Planning")

data = df.dropna(subset=["Avg_Salary", "Category"])
data = data[data["Avg_Salary"].between(500, 50000)]

c1, c2, c3 = st.columns(3)
category = c1.multiselect("Category", sorted(data["Category"].dropna().unique()))
emp_type = c2.multiselect("Employment Type", sorted(data["Employment_Types"].dropna().unique()))
years = c3.slider(
    "Min Years Experience",
    int(data["Min_Yrs_Experience"].min()),
    int(data["Min_Yrs_Experience"].max()),
    (int(data["Min_Yrs_Experience"].min()), int(data["Min_Yrs_Experience"].max())),
)

if category:
    data = data[data["Category"].isin(category)]
if emp_type:
    data = data[data["Employment_Types"].isin(emp_type)]
data = data[data["Min_Yrs_Experience"].between(years[0], years[1])]

if data.empty:
    st.info("No postings match these filters. Widen the experience range or clear a filter.")
else:
    k1, k2, k3 = st.columns(3)
    k1.metric("Median Salary", f"${data['Avg_Salary'].median():,.0f}")
    k2.metric("Min Salary", f"${data['Avg_Salary'].min():,.0f}")
    k3.metric("Max Salary", f"${data['Avg_Salary'].max():,.0f}")

    # Box plot by Category
    fig1 = px.box(data, x="Category", y="Avg_Salary", color="Category",
                  title="Salary Distribution by Category")
    fig1.update_traces(boxmean=True)
    fig1.update_layout(showlegend=False, xaxis_tickangle=-80)
    st.plotly_chart(fig1, use_container_width=True)

    top_roles = data["title"].value_counts().nlargest(10).index
    fig2 = px.box(data[data["title"].isin(top_roles)],
                  x="title", y="Avg_Salary", color="title",
                  title="Salary Distribution by Role (Top 10 Roles)")
    fig2.update_traces(boxmean=True)
    fig2.update_layout(showlegend=False, xaxis_tickangle=-30)
    st.plotly_chart(fig2, use_container_width=True)


# st.title("Business Case 3: Salary Budget Benchmark")
# st.markdown(
#     """
#     ### Business objective
#     Help a startup plan its talent budget using industry salary benchmarks for headcount and specialist roles.
#     """
# )
# st.markdown(
#     """
#     **Dataset fields used**
#     - `Category`
#     - `Employment_Types`
#     - `Min_Yrs_Experience`
#     - `Avg_Salary`
#     - `Position_Level`
#     """
# )

# filter_df = df.groupby("Category").agg({"Vacancies": "sum"}).reset_index()
# # Create bar chart
# fig = px.bar(
#     filter_df,
#     x="Category",   # categories on x-axis
#     y="Vacancies",      # number of vacancies on y-axis
#     title="Job Vacancies by Category",
#     text="Vacancies"    # show vacancy numbers on bars
# )
# # Improve layout
# fig.update_layout(
#     xaxis_title="Job Category",
#     yaxis_title="Number of Vacancies",
#     template="plotly_white"
# )
# # Show the figure
# #fig.show()
# st.plotly_chart(fig)

# Filters
# categories = sorted(df["Category"].dropna().unique())
# employment_types = sorted(df["Employment_Types"].dropna().unique())

# selected_categories = st.multiselect(
#     "Select category",
#     categories,
#     default=categories,
# )

# selected_employment = st.multiselect(
#     "Select employment type",
#     employment_types,
#     default=employment_types,
# )

# min_exp = int(df["Min_Yrs_Experience"].min())
# max_exp = int(df["Min_Yrs_Experience"].max())
# selected_experience = st.slider(
#     "Minimum years experience",
#     min_value=min_exp,
#     max_value=max_exp,
#     value=(min_exp, max_exp),
# )

# filtered = df[
#     df["Category"].isin(selected_categories)
#     & df["Employment_Types"].isin(selected_employment)
#     & df["Min_Yrs_Experience"].between(*selected_experience)
# ].copy()

# if filtered.empty:
#     st.warning("No records match the selected filters. Try widening the selection.")
# else:
#     st.subheader("Salary benchmark summary")
#     overall_metrics = filtered["Avg_Salary"].agg(["mean", "median", "min", "max"]).round(0)
#     st.metric("Mean benchmark salary", f"${overall_metrics['mean']:,}")
#     st.metric("Median benchmark salary", f"${overall_metrics['median']:,}")
#     st.metric("Min benchmark salary", f"${overall_metrics['min']:,}")
#     st.metric("Max benchmark salary", f"${overall_metrics['max']:,}")

#     st.markdown("### Salary distribution by category and role")
#     boxplot = (
#         alt.Chart(filtered)
#         .mark_boxplot(extent="min-max")
#         .encode(
#             x=alt.X("Category:N", title="Category"),
#             y=alt.Y("Avg_Salary:Q", title="Average salary"),
#             color=alt.Color("Position_Level:N", title="Role level"),
#             tooltip=[
#                 "Category",
#                 "Position_Level",
#                 "Employment_Types",
#                 "Min_Yrs_Experience",
#                 "Avg_Salary",
#             ],
#         )
#         .properties(height=420, width=900)
#     )
#     st.altair_chart(boxplot, use_container_width=True)

#     st.markdown("### Average salary by role level")
#     role_avg = (
#         filtered.groupby("Position_Level", as_index=False)["Avg_Salary"]
#         .mean()
#         .sort_values("Avg_Salary", ascending=False)
#     )
#     bar_chart = (
#         alt.Chart(role_avg)
#         .mark_bar()
#         .encode(
#             x=alt.X("Avg_Salary:Q", title="Mean average salary"),
#             y=alt.Y("Position_Level:N", sort="-x", title="Role level"),
#             tooltip=["Position_Level", alt.Tooltip("Avg_Salary:Q", format="$,.0f")],
#         )
#         .properties(height=420, width=900)
#     )
#     st.altair_chart(bar_chart, use_container_width=True)

#     st.markdown("### Example insight")
#     example = filtered[
#         filtered["Min_Yrs_Experience"] == min(selected_experience)
#     ].copy()
#     if not example.empty:
#         example_summary = (
#             example.groupby(["Category", "Position_Level"], as_index=False)["Avg_Salary"]
#             .agg(["median", "min", "max"])
#             .reset_index()
#             .round(0)
#         )
#         st.dataframe(example_summary.rename(columns={"median": "Median", "min": "Min", "max": "Max"}))
#     else:
#         st.info("No example row for the selected exact experience range.")