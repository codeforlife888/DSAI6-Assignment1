## 2. Data Handling & Process
Summary:
- Cleaned a dataset of 280MV CSV file.
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
