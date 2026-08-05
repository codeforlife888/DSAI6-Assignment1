import streamlit as st
import pandas as pd
import plotly.express as px
from config import load_data

df = load_data()

st.title(":material/attach_money: Higher salary = :material/diversity_3: more job applicants?")
st.write("Business Objective: Should we increase salaries to attract more candidates?")

#created dataframe filter by Category = Information technology, then group by all title under Category = Information Technology. Finally Avg_Salary and Total_Applications for each unique title.
df_filtered = (
    df[df['Category'] == 'Information Technology']
    .groupby('title', as_index=False)
    .agg(
        Avg_Salary=('Avg_Salary', 'mean'),
        Total_Applications=('Total_Applications', 'sum')
    )
)

# Filter out outliers in Avg_Salary using IQR method
Q1 = df_filtered['Avg_Salary'].quantile(0.25)
Q3 = df_filtered['Avg_Salary'].quantile(0.95)
IQR = Q3 - Q1

lower = 1000
upper = Q3 + 1.5 * IQR

df_filtered = df_filtered[
    (df_filtered['Avg_Salary'] >= lower) &
    (df_filtered['Avg_Salary'] <= upper)
]

fig = px.scatter(
    df_filtered,
    x="Avg_Salary",
    y="Total_Applications",
    hover_name="title",  # Shows title prominently
    hover_data={
        "Avg_Salary": ":,.0f",
        "Total_Applications": ":,.0f",
    },
    title="Overview : Average Salary vs Total Applications"
)

fig.update_layout(
    xaxis_title="Average Monthly Salary ($)",
    yaxis_title="Total # of Applications",

)

st.plotly_chart(fig, width='stretch')
