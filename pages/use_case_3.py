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
from config import load_data

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
    fig1.update_layout(showlegend=False, xaxis_tickangle=-90)
    st.plotly_chart(fig1, use_container_width=True)

    top_roles = data["title"].value_counts().nlargest(30).index
    fig2 = px.box(data[data["title"].isin(top_roles)],
                  x="title", y="Avg_Salary", color="title",
                  title="Salary Distribution by Role (Top 10 Roles)")
    fig2.update_traces(boxmean=True)
    fig2.update_layout(showlegend=False, xaxis_tickangle=-90)
    st.plotly_chart(fig2, use_container_width=True)


# ---------- Budget lookup ----------
st.markdown("### Salary Statistics by Selection")

c1, c2, c3 = st.columns(3)

category = c1.selectbox("Category", ["All"] + sorted(data["Category"].dropna().unique()))
pool = data if category == "All" else data[data["Category"] == category]


years = c2.selectbox("Min Years Experience",
                     ["All"] + sorted(pool["Min_Yrs_Experience"].dropna().unique()))
pool = pool if years == "All" else pool[pool["Min_Yrs_Experience"] == years]

role = c3.selectbox("Role", ["All"] + sorted(pool["title"].dropna().unique()))
pool = pool if role == "All" else pool[pool["title"] == role]

if pool.empty:
    st.info("No postings match this selection. Try a broader filter.")
else:
    s = pool["Avg_Salary"]
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Min", f"${s.min():,.0f}")
    k2.metric("25th Pct", f"${s.quantile(0.25):,.0f}")
    k3.metric("Median", f"${s.median():,.0f}")
    k4.metric("75th Pct", f"${s.quantile(0.75):,.0f}")
    k5.metric("Max", f"${s.max():,.0f}")

    st.caption(f"Based on {len(pool):,} job postings.")
    if len(pool) < 30:
        st.warning(
            f"Only {len(pool)} postings in this slice — treat these figures as "
            "indicative rather than a benchmark."
        )