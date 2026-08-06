# All Content/ Filters / Charts for Use Case 5 goes here :
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from config import load_data

df = load_data()

st.title("What level of experience should we target for our initial IT team?")
st.write("Business Objective: As a startup, should we recruit junior, mid-level, or senior professionals?")

# Create a dataframe filtered by Category = Information Technology, then group by Min_Yrs_Experience by folloing conditions: 
# 1. For Min_Yrs_Experience = 0-2, label as 'Junior'
# 2. For Min_Yrs_Experience = 3-5, label as 'Mid-Level'
# 3. For Min_Yrs_Experience = 6+, label as 'Senior'
# For each group above, calculate the Salary_Min and Salary_Max.
df['Experience_Level'] = pd.cut(
    df['Min_Yrs_Experience'],
    bins=[-1, 2, 5, float('inf')],
    labels=['Junior', 'Mid-Level', 'Senior']
)   

df_filtered_experience_level = (
    df[df['Category'] == 'Information Technology']
    .groupby('Experience_Level', as_index=False)
    .agg(
        # agg functions to calculate the mean of Salary_Min and Salary_Max, rounded to 2 decimal places
        Salary_Min=('Salary_Min', 'mean'),
        Salary_Max=('Salary_Max', 'mean')
    )
    .round(2)  # Round the results to 2 decimal places
)           

df_filtered_experience_jobgroup_level = (
    df[df['Category'] == 'Information Technology']
    .groupby(['Experience_Level', 'Job_Group'], as_index=False)
    .agg(
        Salary_Min=('Salary_Min', 'mean'),
        Salary_Max=('Salary_Max', 'mean')
    )
    .round(2)
)

df_filtered_experience_jobgroup_level = df_filtered_experience_jobgroup_level[df_filtered_experience_jobgroup_level['Job_Group'] != 'Other']

# --------------------------
# Chart 1
# --------------------------

fig = go.Figure()

fig.add_trace(
    go.Bar(
        y=df_filtered_experience_level["Experience_Level"],
        x=df_filtered_experience_level["Salary_Max"] -
          df_filtered_experience_level["Salary_Min"],
        base=df_filtered_experience_level["Salary_Min"],
        orientation="h",
        customdata=df_filtered_experience_level["Experience_Level"],
        text=[
            f"${a:,.0f} - ${b:,.0f}"
            for a, b in zip(
                df_filtered_experience_level["Salary_Min"],
                df_filtered_experience_level["Salary_Max"]
            )
        ],
        textposition="inside",
        hovertemplate="<b>%{y}</b><br>%{text}<extra></extra>",
    )
)

fig.update_layout(
    title="Average Salary Range by Experience Level",
    template="plotly_white",
    xaxis_title="Monthly Salary (SGD)",
    yaxis_title="Experience Level"
)

fig.update_xaxes(
    tickprefix="$",
    separatethousands=True
)

fig.update_yaxes(autorange="reversed")

# --------------------------
# 2-Column Layout
# --------------------------
col1, col2 = st.columns([4, 4], gap="small")

with col1:
    with st.container(border=True):
        st.subheader("Experience Level")
        event = st.plotly_chart(
            fig,
            key="experience_chart",
            use_container_width=True,
            on_select="rerun"
        )

with col2:
    with st.container(border=True):
        st.subheader("Job Title Breakdown")

        if event.selection.points:

            selected_level = event.selection.points[0]["y"]

            df_drill = df_filtered_experience_jobgroup_level[
                df_filtered_experience_jobgroup_level["Experience_Level"] == selected_level
            ]

            fig2 = go.Figure()

            fig2.add_trace(
                go.Bar(
                    y=df_drill["Job_Group"],
                    x=df_drill["Salary_Max"] - df_drill["Salary_Min"],
                    base=df_drill["Salary_Min"],
                    orientation="h",
                    text=[
                        f"${a:,.0f} - ${b:,.0f}"
                        for a, b in zip(
                            df_drill["Salary_Min"],
                            df_drill["Salary_Max"]
                        )
                    ],
                    textposition="inside",
                    hovertemplate="<b>%{y}</b><br>%{text}<extra></extra>",
                )
            )

            fig2.update_layout(
                template="plotly_white",
                title=f"{selected_level} Salary Range by Job Title",
                xaxis_title="Monthly Salary (SGD)",
                yaxis_title="Job Title",
                height=max(500, len(df_drill) * 40)
            )

            fig2.update_xaxes(
                tickprefix="$",
                separatethousands=True
            )

            fig2.update_yaxes(autorange="reversed")

            st.plotly_chart(fig2, use_container_width=True)

        else:
            st.info("Select an experience level from the left chart.")


st.success(
    " **Conclusion** \n"

    "\nThe analysis suggests that mid-level professionals offer the best balance between hiring cost and experience for a startup. While junior employees are cheaper, they may require additional training, and senior professionals command substantially higher salaries. Therefore, startups should prioritize recruiting mid-level talent, supplementing with senior specialists only where advanced expertise is required and junior hires for long-term talent development.",
    icon=":material/done_all:",
)