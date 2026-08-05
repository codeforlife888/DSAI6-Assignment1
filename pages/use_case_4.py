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
    .groupby('Job_Group', as_index=False)
    .agg(
        Avg_Salary=('Avg_Salary', 'mean'),
        Total_Applications=('Total_Applications', 'sum')
    )
)
#exlcude rows with job_group = 'Other'
df_filtered = df_filtered[df_filtered['Job_Group'] != 'Other']

# Filter out outliers in Avg_Salary using IQR method
Q1 = df_filtered['Avg_Salary'].quantile(0.25)
Q3 = df_filtered['Avg_Salary'].quantile(0.75)
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
    trendline="ols",
    log_y=True,  # Log scale for y-axis
    hover_name="Job_Group",  # Shows title prominently
    hover_data={
        "Avg_Salary": ":,.0f",
        "Total_Applications": ":,.0f",
    },
    title="# of Applications vs Average Salary by Job Title"
)

fig.update_layout(
    xaxis_title="Average Monthly Salary ($)",
    yaxis_title="Total # of Applications",

)

st.plotly_chart(fig, width='stretch')

#calculate Pearson correlation coefficient between Avg_Salary and Total_Applications
correlation = df_filtered["Avg_Salary"].corr(
    df_filtered["Total_Applications"]
)

if abs(correlation) >= 0.8:
    strength = "Very Strong"
elif abs(correlation) >= 0.6:
    strength = "Strong"
elif abs(correlation) >= 0.4:
    strength = "Moderate"
elif abs(correlation) >= 0.2:
    strength = "Weak"
else:
    strength = "Very Weak"

st.metric("Pearson Correlation", f"{correlation:.3f}")

st.write(f"**Relationship:** {strength}")

st.title("Business Insight")
st.write("There is a weak negative correlation (-0.214) between salary and the number of applications, suggesting that increasing salary alone is unlikely to significantly increase applicant volume.")