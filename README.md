# 📊 Churn Analysis & Customer Intelligence

An end-to-end **Customer Churn Analysis and Customer Intelligence project** built using Python, Pandas, NumPy, SQL, SQLite, Matplotlib, Seaborn, and Jupyter Notebook.

The project focuses on transforming raw customer, subscription, and support data into meaningful business insights around **customer churn, retention, revenue at risk, customer complaints, escalation rates, subscription behavior, and churn risk**.

---

## 🎯 Project Objective

Customer churn directly impacts recurring revenue and long-term business growth.

The objective of this project is to analyze customer and subscription data to:

- Measure overall customer churn and retention
- Identify churn patterns across different plans and states
- Analyze subscription behavior
- Measure revenue at risk from churned customers
- Understand customer complaint patterns
- Analyze escalation rates
- Calculate customer tenure and ARPU
- Categorize customers based on churn risk
- Create visualizations for business decision-making
- Work with SQL and SQLite databases alongside Python

---

## 🧠 Project Workflow

```text
Customer Database
       ↓
Data Extraction using SQLite
       ↓
Data Cleaning & Standardization
       ↓
Feature Engineering
       ↓
Data Integration / Merging
       ↓
Business KPI Analysis
       ↓
Churn Risk Classification
       ↓
Data Visualization
       ↓
SQL Analysis
       ↓
Business Insights

🗄️ Data Extraction
The project begins by connecting to a SQLite customer database using Python.
The database tables are identified dynamically using SQLite metadata and loaded into Pandas DataFrames.
The analysis works with multiple data sources including:
- Customer information
- Subscription information
- Customer support information
🧹 Data Cleaning & Preparation
Several data-cleaning and standardization operations were performed before analysis.
Customer Data
The customer dataset was cleaned by:
- Renaming name to customer_name
- Removing unnecessary columns such as interests and pincode
- Converting dob into a datetime format
- Standardizing gender values
- Handling missing country values using state-to-country mapping
Subscription Data
Subscription date columns were converted into proper datetime format:
- subscription_start_date
- renewal_date
- cancellation_date
Support Data
The support dataset was cleaned by:
- Removing unnecessary columns
- Converting complaint_date to datetime
- Calculating customer complaint counts
- Keeping the latest support record for each customer
⚙️ Feature Engineering
Several useful business features were created from the existing data.
Churn Flag
A churn_flag was created based on whether a customer had a cancellation date.
df_db_subscription['churn_flag'] = np.where(    df_db_subscription['cancellation_date'].notna(),    1,    0)


Where:
1 → Customer churned
0 → Customer retained

Complaint Count
The number of complaints associated with each customer was calculated using customer-level grouping.
Customer Tenure
Customer tenure was calculated in days using subscription start and cancellation dates.
For active customers, the current date was used to calculate the duration.
Churn Risk
Customers were categorized using their churn score:
Churn Score	Risk Level
< 50	Low
50 – 69	Medium
≥ 70	High


This creates a new:
churn_risk

feature.
🔗 Data Integration
The customer, subscription, and support datasets were merged using:
customerid

The final analytical dataset combines information from all three sources.
df = (    df_db_subscription    .merge(df_db_customer, on='customerid', how='left')    .merge(df_db_support, on='customerid', how='left'))


The resulting dataset was exported as:
exported_churn_data.csv

📈 Business KPIs
The project calculates several important customer and business metrics.
Churn Rate
Measures the percentage of customers who have churned.
churn_rate = df['churn_flag'].mean() * 100


Retention Rate
Calculated as:
Retention Rate = 100 - Churn Rate

ARPU
Average Revenue Per User (ARPU) is calculated using average monthly charges.
arpu = df['monthly_charges'].mean()


Average Customer Tenure
Measures the average number of days customers have remained subscribed.
Average Tenure = Average Customer Lifetime

Revenue at Risk
The project estimates monthly revenue associated with churned customers.
revenue_at_risk = df.loc[    df['churn_flag'] == 1,    'monthly_charges'].sum()


This provides an indication of the revenue exposure associated with customer churn.
Escalation Rate
Measures the percentage of customers with escalated support cases.
escalation_rate = (    df['escalations'] == 'Y').mean() * 100


Average Complaints per User
Calculates the average number of complaints per unique customer.
avg_complaints = (    df['complaint_count'].sum()    / df['customerid'].nunique())


🔎 Churn Analysis
The project analyzes churn across multiple dimensions.
Churn by Plan Type
Churn rates are calculated for each:
plan_type

This helps identify whether particular plans experience higher customer churn.
Churn by State
Customer churn is also analyzed geographically using:
state

Churn by Subscription Type
Churn rates are calculated across:
subscription_type

This helps compare customer retention across different subscription structures.
📊 Data Visualization
The project uses Matplotlib and Seaborn to visualize customer churn patterns.
Monthly Churn Trend
A monthly trend is created using customer cancellation dates.
Cancellation Month
        ↓
Number of Churned Customers

This helps identify changes in churn volume over time.
Churn Rate by Plan
A bar chart compares churn rates across different plan types.
Churn by State
A geographical comparison is created to identify differences in churn rates between states.
Correlation Heatmap
A correlation heatmap is created using:
plan_type
contract_type
churn_score
churn_flag
churn_risk
escalations

Categorical variables are encoded before calculating correlations.
📋 Pivot Table Analysis
The project also uses Pandas pivot tables to summarize customer and churn information.
Examples include:
- Churn rate by plan
- Total monthly charges by plan
- Number of unique customers by plan
- Average churn by plan
This allows the analysis to move from raw records to summarized business metrics.
🗃️ SQL Analysis with Python
The project also demonstrates working with SQL directly from Python.
SQLite is used to create and query databases using:
sqlite3


The project demonstrates:
- Inserting records into SQL tables
- Selecting data using SQL
- Loading SQL results into Pandas
- Aggregating data using SQL
- Using GROUP BY
- Using SUM()
- Combining SQL with Python data analysis
Example aggregation:
SELECT country,
       SUM(budget) AS total_budget
FROM users
GROUP BY country;

This demonstrates how SQL and Python/Pandas can be used together in a data analytics workflow.
🛠️ Technologies Used
Technology	Purpose
Python	Data analysis and programming
Pandas	Data manipulation and analysis
NumPy	Numerical operations and feature engineering
SQLite	Database management
SQL	Data querying and aggregation
Matplotlib	Data visualization
Seaborn	Statistical visualization
Jupyter Notebook	Analysis and documentation
Git & GitHub	Version control


📁 Project Structure
churn/
│
├── churn_analysis.ipynb
│
├── data.csv
├── exported_churn_data.csv
│
├── customer_churn.db
├── customer_churn.db copy
├── test_database.sqlite
│
├── chap2.py
├── chap3.py
├── chap4.py
├── chap5.py
├── chap6.py
├── chap7.py
├── chap8.py
├── chap9.py
│
├── project1.py
├── poems.txt
├── question
│
└── README.md

⚙️ Installation
1. Clone the repository
git clone https://github.com/YazdanAhmedData/churn.git

2. Navigate to the project
cd churn

3. Create a virtual environment
python -m venv .venv

4. Activate the environment
macOS / Linux
source .venv/bin/activate

Windows
.venv\Scripts\activate

5. Install the required libraries
pip install pandas numpy matplotlib seaborn jupyter

▶️ Running the Project
Launch Jupyter Notebook:
jupyter notebook

Then open:
churn_analysis.ipynb

Run the notebook cells sequentially to reproduce the analysis.
💡 Business Applications
The analysis can help businesses understand:
- Customer retention performance
- High-churn customer segments
- Revenue exposed to churn
- Customer complaint behavior
- Support escalation patterns
- Subscription-level churn
- Geographic differences in churn
- Potential high-risk customers
These insights can support targeted customer-retention strategies and data-driven business decisions.
🚀 Future Improvements
Potential extensions to the project include:
- Building a machine learning churn prediction model
- Predicting individual customer churn probability
- Developing a Power BI churn dashboard
- Adding automated KPI reporting
- Performing customer segmentation
- Building a customer lifetime value model
- Performing feature importance analysis
- Creating an interactive Streamlit application
- Deploying the analysis as a web application
- Automating the data pipeline
📚 Skills Demonstrated
This project demonstrates practical experience in:
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Customer Churn Analysis
- Business KPI Development
- Customer Intelligence
- SQL
- SQLite
- Pandas
- NumPy
- Data Visualization
- Python
- Jupyter Notebook
- Git & GitHub
👨‍💻 Author
Yazdan Ahmed
Data Analytics & Machine Learning Enthusiast
GitHub:
https://github.com/YazdanAhmedData
⭐ Project
If you found this project useful, consider giving the repository a ⭐ on GitHub.
