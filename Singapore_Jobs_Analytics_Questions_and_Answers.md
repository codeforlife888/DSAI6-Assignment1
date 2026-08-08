# Module 1 Assignment Project – Singapore Jobs Analytics

## 1. Business Case

- **Business scenario:** A Singapore startup is building its initial Information Technology (IT) team and needs job-market evidence to support its recruitment and manpower-budget decisions.
- **Objective:** The project helps the startup decide which IT roles and experience levels to recruit, how much salary budget to allocate, and whether offering a higher salary is likely to attract more applicants.
- **Target users:** The primary users are startup founders, hiring managers, human-resource professionals, and talent-acquisition teams.
- **Value provided:** The dashboard converts a large Singapore job-posting dataset into understandable salary, experience, demand, and application insights. This reduces reliance on assumptions when planning headcount and recruitment budgets.
- **Main business questions:**
  - Which job categories and IT roles have the strongest hiring demand?
  - What salary range should the startup budget for different IT roles?
  - Does offering a higher salary attract more job applicants?
  - Should the initial IT team consist mainly of junior, mid-level, or senior employees?

---

## 2. Data Handling & Process
Summary:
- Cleaned a dataset of ~280MB CSV file.
- Compared Python/Pandas and SQL (DuckDB) for data cleaning in VS Code using Jupyter Notebook.
- Python/Pandas required more execution time and memory, while SQL with DuckDB processed the data much faster and execute queries directly on the data stored on hard drive
- The cleaned dataset saved as a CSV file was much larger than the same data stored in a DuckDB database file.  

Overall: SQL with DuckDB provided better execution speed, memory efficiency, and storage efficiency for large datasets.


- **Tools used:** Python, Pandas and SQL were used for data loading, cleaning, transformation, grouping, and analysis. Streamlit was used to build the interactive application, while Plotly was used to produce interactive charts.
- **Dataset loading:** The cleaned source file, `output3.csv`, contains approximately 1.77 million rows and 22 columns. It was loaded with `pandas.read_csv()` using a semicolon delimiter. The data-loading function was placed in `config.py` and decorated with `@st.cache_data` so that Streamlit would not reload the full dataset after every interaction.
- **Date preparation:** `New_Post_Date`, `Orig_Post_Date`, and `Expiry_Date` were parsed as date fields. Invalid or missing dates were handled so they would not cause errors in later filtering or trend analysis.
- **Numeric cleaning:** Salary, application, view, vacancy, experience, and repost fields were checked and converted to numeric data types where required. Invalid values were converted to missing values before analysis.
- **Salary cleaning:** Records with impossible or misleading salary values, such as zero, one, negative values, or extremely large values, were investigated. The average salary was calculated from `Salary_Min` and `Salary_Max` where appropriate. The Interquartile Range (IQR) method and percentile checks were used to reduce the effect of extreme salary outliers on charts and correlations.
- **Category standardisation:** Text fields such as `Category` and `Job_Title` were stripped of extra spaces and standardised for consistent filtering. This prevented differences such as capitalisation or spacing from creating separate groups.
- **Job-title grouping:** Raw job titles contained descriptions, technologies, seniority labels, and salary information. A keyword-based mapping function grouped these variations into clearer `Job_Group` categories such as Software Engineer, Data Engineer, Data Analyst, Business Analyst, System Analyst, DevOps Engineer, Cloud Engineer, Security Engineer, IT Manager, Project Manager, and IT Consultant. Titles that did not match a rule were assigned to `Other`.
- **Experience engineering:** `Min_Yrs_Experience` was converted into an `Experience_Level` feature: **Junior (0–2 years), Mid-Level (3–5 years), and Senior (6+ years)**.
- **Aggregated measures:** Grouped dataframes were created to calculate average minimum salary, average maximum salary, average salary, total applications, total vacancies, posting count, and other demand measures by category, experience level, and job group. Aggregating before plotting also improved dashboard performance.
- **EDA findings:** Salary data contained strong outliers, and job-title variation made role-level comparison unreliable until titles were grouped. The analysis also found only a weak relationship between average salary and total applications, indicating that salary alone does not explain applicant interest. These findings led to the use of outlier filtering, job grouping, hover details, and drill-down charts.

---

## 3. Dashboard / App

Describe and demonstrate the solution, including:

- **Solution type:** The solution is a multipage interactive dashboard built with Streamlit. Pandas prepares the data, and Plotly produces the visualisations.
- **Navigation:** The application is divided into an overview, data-handling information, and individual use-case pages. This allows users to move from high-level market information to a focused business question.
- **Overview view:** The overview presents important measures such as job-posting volume, vacancies, applications, common job categories, and salary ranges. It gives hiring managers a quick summary of the Singapore employment market before they explore IT-specific findings.
- **Salary and applicant view:** A scatter plot compares average salary with total applications for grouped IT roles. Job-group names are included in the tooltips, and outliers are filtered to keep the chart readable. A correlation measure and trendline help users interpret the overall relationship.
- **Insight from salary and applications:** The observed correlation is weak. Therefore, increasing salary alone may not generate a proportionate increase in applications. Job type, required skills, experience level, employer reputation, and employment conditions may also affect applicant interest.
- **Experience-level view:** A horizontal floating-bar or dumbbell-style chart compares the average minimum and maximum salaries for Junior, Mid-Level, and Senior IT positions. The horizontal salary axis makes the numerical ranges easier to compare.
- **Role drill-down:** Selecting an experience level reveals salary ranges for the job groups within that level. The summary and drill-down charts can be displayed side by side, allowing users to compare the broad experience category with its underlying roles.
- **Interactivity:** The dashboard uses filters, Plotly hover tooltips, selection-based drill-downs, and chart-specific Streamlit keys. These features let users explore relevant subsets without displaying all 1.77 million records at once.
- **Performance choices:** The dataset is cached, filtering is performed before expensive transformations, only required columns are selected, and charts use aggregated data rather than raw records. These choices reduce repeated processing and improve page-loading speed.
- **Visual design:** Clear titles and business objectives are placed above each visual. Charts use readable labels, consistent salary formatting, horizontal axes where long role names are present, and restrained colours so comparisons remain easy to understand.
- **Business value:** The overview identifies the scale and structure of the market; the salary-versus-applications analysis prevents the startup from assuming that pay is the only attraction factor; and the experience drill-down supports a realistic hiring mix and salary budget for the initial IT team.

---

## 4. Key Insights and Story

What conclusions can users draw from the analysis, and how do these findings support the business decision?

- The dataset shows that IT salaries vary meaningfully by both experience level and job group. The startup should therefore create a role-specific budget instead of applying one salary estimate to the whole IT team.
- Senior employees require a higher salary range, while junior employees provide a lower-cost way to expand the team. However, experience level should be selected according to the responsibility and complexity of each role rather than salary alone.
- A practical initial hiring approach is a balanced team: a smaller number of mid-level or senior employees for technical leadership and critical decisions, supported by junior employees for operational and development work.
- The weak salary–application correlation suggests that simply raising advertised pay may not be an efficient recruitment strategy. Clear job descriptions, realistic requirements, career-development opportunities, flexible work arrangements, and an efficient hiring process may also improve candidate interest.
- Clean job grouping is essential. Without standardising the many variations of job titles, demand and salary figures for the same underlying occupation would be divided across multiple labels and could lead to misleading conclusions.
- Overall, the dashboard gives founders and hiring managers an evidence-based starting point for deciding **who to hire, what experience mix to target, and how much salary budget to prepare**.

---

## Final Project Summary

This project transforms approximately 1.77 million Singapore job-market records into an interactive Streamlit dashboard for startup workforce planning. The application combines cleaned and grouped job titles, salary analysis, applicant-demand analysis, and experience-level drill-downs. Its main recommendation is to use a balanced, role-specific hiring strategy instead of assuming that higher salaries alone will attract more candidates. The dashboard supports this decision by making salary ranges, experience requirements, and recruitment patterns easier to compare and explain.
