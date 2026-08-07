# Module 1 Assignment Project – Singapore Jobs Analytics

## Data dictionary

| **Original Data** 	|  	|  	| **Cleaned Data** 	|  	|  	|
|---	|---	|---	|---	|---	|---	|
| **Column** 	| **Type** 	| **Notes** 	| **Actions** 	| Column 	| **Type** 	|
| **categories** 	| str (JSON array) 	| e.g. [{"id":21,"category":"Information Technology"}] — a job can belong to multiple categories. You will need to parse this. 	| Converted to "category" after exploding the JSON array  	| **Category** 	| VARCHAR 	|
| employmentTypes 	| str 	| Permanent, Full Time, Contract, Part Time, Temporary, Internship/Attachment, Freelance, Flexi-work. 	|  	| **Employment_Type** 	| VARCHAR 	|
| metadata_expiryDate 	| date 	| When the posting expires. 	|  	| **Expiry_Date** 	| date 	|
| metadata_isPostedOnBehalf 	| bool 	| True if a recruiter posted on behalf of the hiring company. 	|  	| **Posted_On_Behalf** 	| bool 	|
| **metadata_jobPostId** 	| str 	| Unique ID, e.g. MCF-2023-0252866. 	| Unique ID, Removed null	| **Job_Post_ID** 	| str 	|
| metadata_newPostingDate 	| date 	| Date of the most recent re-post. 	|  	| **New_Post_Date** 	| date 	|
| metadata_originalPostingDate 	| date 	| Date the job was first posted. 	|  	| **Orig_Post_Date** 	| date 	|
| metadata_repostCount 	| int 	| How many times the same job has been re-posted. A signal of hard-to-fill roles. 	|  	| **Repost_Date** 	| int 	|
| metadata_totalNumberJobApplication 	| int 	| Number of applications received. 	|  	| **Total_Applications** 	| int 	|
| metadata_totalNumberOfView 	| int 	| Number of times the post was viewed. 	|  	| **Total_Views** 	| int 	|
| minimumYearsExperience 	| int 	| Years of experience required. 	|  	| **Min_Yrs_Experience** 	| int 	|
| numberOfVacancies 	| int 	| Open headcount. 	|  	| **Vacancies** 	| int 	|
| positionLevels 	| str 	| Fresh/entry, Junior Executive, Executive, Senior Executive, Professional, Manager, Middle Management, Senior Management, Non-executive. 	|  	| **Position_Level** 	| str 	|
| postedCompany_name 	| str 	| The poster (often a recruitment agency, not the hiring employer). 	|  	| **Company_Name** 	| str 	|
| salary_minimum / salary_maximum 	| int 	| Salary band. 	|  	| **Salary_Max / Salary_Min** 	| int 	|
| **salary_type** 	| str 	| Almost all Monthly. 	| drop column as it has only one unique value 	|  	| s  	|
| status_jobStatus 	| str 	| Open, Closed, Re-open. 	|  	| **Job_Status** 	| VARCHAR	|
| title 	| str 	| Free-text job title. 	|  	| **Job_Title** 	| VARCHAR 	|
| average_salary 	| float 	| Pre-computed mean of min/max. 	|  	| **Avg_Salary** 	| INTEGER 	|


----
