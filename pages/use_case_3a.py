# All Content/ Filters / Charts for Use Case 3 goes here :
# Problem Statement: What budgetary salary should our company plan for headcounts and specialists (Industry benchmark)?
# 
# Business Objective
# A startup plan their talent budget for operation based on industry benchmark.
# 
# Dataset Columns
# Category, MinimumYearsExperience, Avg_Salary
# 
# Visualization
# Box Plot #1 - Mean, Max, Min Avg_Salary by Category
# Box Plot #2 - Mean, Max, Min Avg_Salary by Min_Yrs_Experience
# 
# Interactive Filters (Salary Calculator)
# Select Dropdown for filtering the range of Avg_Salary under (1) Category (2) Min_Yrs_Experience (3) Job_Title
# 
# Story
# This establishes a realistic salary budget for Talent Acquisition. Example Insight
# Cybersecurity and Cloud Engineers with 5 years experience. What are the min, 25th percentile, median, 75th percentile and max salary per headcount

import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from plotly.subplots import make_subplots
from pathlib import Path
from config import load_data

df = load_data()

# --- Use Case 3b: Salary benchmark for talent budgeting ---
st.subheader("Salary Benchmark for Talent Acquisition Planning")


data = df.dropna(subset=["Avg_Salary", "Category"])
data = data[data["Avg_Salary"].between(500, 50000)]
data = data[data["Min_Yrs_Experience"] <= 20]  # Filter out extreme outliers in experience

c1, c2, c3 = st.columns(3)
# c1 - Count the number of rows in job postings after filtering
c1.metric("Total Job Postings", f"{len(data):,}")
# c2 - Count the number of unique categories in job postings after filtering
c2.metric("Total Categories", f"{data['Category'].nunique():,}")

years = c3.slider(
    "Min Years Experience",
    int(data["Min_Yrs_Experience"].min()),
    int(data["Min_Yrs_Experience"].max()),
    (int(data["Min_Yrs_Experience"].min()), int(data["Min_Yrs_Experience"].max())),
)

if data.empty:
    st.info("No postings match these filters. Widen the experience range or clear a filter.")
else:
    k1, k2, k3 = st.columns(3)
    k1.metric("Median Salary", f"${data['Avg_Salary'].median():,.0f}")
    k2.metric("Min Salary", f"${data['Avg_Salary'].min():,.0f}")
    k3.metric("Max Salary", f"${data['Avg_Salary'].max():,.0f}")

    # ---------- Salary axis control ----------
    sal_view = st.slider("Salary axis range (SGD)", 0, 50000, (0, 20000), step=1000)

    # ---------- fig1: by Category ----------
    fig1 = px.box(
        data, y="Category", x="Avg_Salary", color="Category",
        orientation="h", points=False,
    )
    fig1.update_traces(boxmean=True)
    fig1.update_layout(
        title=dict(text="Salary Distribution by Category", font=dict(size=22)),
        showlegend=False, yaxis_title=None,
        xaxis_title="Average Salary (SGD)",
        xaxis_range=list(sal_view),
        height=max(500, 22 * data["Category"].nunique()),
    )
    st.plotly_chart(fig1, use_container_width=True)

    # ---------- fig2: by Minimum Years of Experience ----------
    top_experience = data["Min_Yrs_Experience"].value_counts().nlargest(10).index
    exp_data = data[data["Min_Yrs_Experience"].isin(top_experience)].copy()
    exp_data["Years"] = exp_data["Min_Yrs_Experience"].astype(str)

    fig2 = px.box(
        exp_data, y="Years", x="Avg_Salary", color="Years",
        orientation="h", points=False,
    )
    fig2.update_traces(boxmean=True)
    fig2.update_layout(
        title=dict(text="Salary Distribution by Minimum Years of Experience",
                   font=dict(size=22)),
        showlegend=False, yaxis_title="Minimum Years of Experience",
        xaxis_title="Average Salary (SGD)",
        xaxis_range=list(sal_view), height=500,
        yaxis=dict(categoryorder="array",
                   categoryarray=[str(y) for y in sorted(top_experience)]),
    )
    st.plotly_chart(fig2, use_container_width=True)


# ---------- Budget lookup ----------
st.markdown("### Salary Statistics by Selection")

c1, c2, c3 = st.columns(3)

category = c1.selectbox("Category", ["All"] + sorted(data["Category"].dropna().unique()))
pool = data if category == "All" else data[data["Category"] == category]


years = c2.selectbox("Min Years Experience",
                     ["All"] + sorted(pool["Min_Yrs_Experience"].dropna().unique()))
pool = pool if years == "All" else pool[pool["Min_Yrs_Experience"] == years]

role = c3.selectbox("Role", ["All"] + sorted(pool["Job_Title"].dropna().unique()))
pool = pool if role == "All" else pool[pool["Job_Title"] == role]

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

