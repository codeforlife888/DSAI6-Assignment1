# All Overview page content goes here : 
# - Business Overview
import streamlit as st
import pandas as pd
import plotly.express as px
from config import load_data 

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="IT Department Proposal", layout="wide")

st.title("📄 Proposal: Establishment of a New IT Department")

# -------------------------------
# 1. EXECUTIVE SUMMARY
# -------------------------------
st.header("1. Executive Summary")

st.markdown("""
- **Purpose:** Strengthen digital infrastructure, enhance cybersecurity, and support sustainable business growth.  
- **Outcome:** Establishing a dedicated IT department will reduce operational downtime, improve data security, and enable continuous innovation.
""")

# -------------------------------
# 2. BUSINESS CASE
# -------------------------------
st.header("2. Business Case")

st.markdown("""
- **Current Challenges:**  
  Heavy reliance on outsourced IT services, slow response times, and increasing cybersecurity risks.

- **Opportunities:**  
  Enable digital transformation, drive automation, and leverage data for better decision-making.

- **Strategic Alignment:**  
  Supports organizational goals in operational efficiency, regulatory compliance, and long-term scalability.
""")

# -------------------------------
# 3. IT STRUCTURE
# -------------------------------
st.header("3. Proposed IT Department Structure")

df_structure = pd.DataFrame({
    "Role": [
        "IT Manager",
        "System Administrator",
        "Helpdesk Support",
        "Cybersecurity Specialist",
        "Software Developer",
        "Data Analyst"
    ],
    "Headcount": [1, 2, 2, 1, 2, 1],
    "Key Responsibilities": [
        "IT strategy, governance, vendor management",
        "Server, network, cloud infrastructure",
        "End-user support, troubleshooting",
        "Security monitoring, compliance",
        "Internal tools, automation",
        "Reporting, business intelligence"
    ]
})

st.dataframe(df_structure, use_container_width=True)

total_headcount = df_structure["Headcount"].sum()
st.metric("Total Headcount", total_headcount)

# -------------------------------
# 4. BUDGET
# -------------------------------
st.header("4. Budget Estimate (Annual)")

df_budget = pd.DataFrame({
    "Category": [
        "Salaries",
        "Hardware & Equipment",
        "Software & Licenses",
        "Training & Development",
        "Office Setup",
        "Contingency (10%)"
    ],
    "Cost (SGD)": [
        1080000,
        150000,
        100000,
        50000,
        70000,
        145000
    ],
    "Notes": [
        "Avg. 120K per staff",
        "Laptops, servers, networking gear",
        "Microsoft 365, SAP, security tools",
        "Upskilling, certifications",
        "Workstations, furniture",
        "Risk buffer"
    ]
})

st.dataframe(df_budget, use_container_width=True)

total_budget = df_budget["Cost (SGD)"].sum()
st.metric("Total Estimated Budget (SGD)", f"{total_budget:,.0f}")

# -------------------------------
# OPTIONAL: BUDGET CHART
# -------------------------------
st.subheader("Budget Breakdown")

st.bar_chart(df_budget.set_index("Category")["Cost (SGD)"])

# -------------------------------
# 5. EXPECTED BENEFITS
# -------------------------------
st.header("5. Expected Benefits")

st.markdown("""
- Faster IT support response times (**~30% reduction in downtime**)  
- Stronger cybersecurity posture (ISO / PDPA compliance)  
- Improved productivity through in-house development and automation  
- Long-term cost savings compared to outsourcing  
""")

# -------------------------------
# 6. IMPLEMENTATION TIMELINE
# -------------------------------
st.header("6. Implementation Timeline")

df_timeline = pd.DataFrame({
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Milestone": [
        "Approval, recruitment, procurement",
        "Department setup, infrastructure deployment",
        "Training, process rollout",
        "Full operational readiness"
    ]
})

st.dataframe(df_timeline, use_container_width=True)

# -------------------------------
# OPTIONAL: TIMELINE VISUAL
# -------------------------------
st.subheader("Timeline Overview")

st.line_chart(
    pd.DataFrame({
        "Progress": [1, 2, 3, 4]
    }, index=["Q1", "Q2", "Q3", "Q4"])
)