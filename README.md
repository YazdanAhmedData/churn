# Customer Churn Analysis & Intelligence | Python, SQL and SQLite

An end-to-end customer analytics project focused on understanding churn, retention, subscription behaviour, customer support signals, and revenue exposure. The project combines Python-based data preparation and analysis with SQL/SQLite data handling and visual exploration.

## Business Problem

Customer churn can reduce recurring revenue and increase the cost of replacing customers. This project organizes customer, subscription, and support-related data to help investigate where churn is concentrated, which customer segments may need attention, and what operational signals may be associated with cancellation.

## Questions Explored

- What does churn look like across customer and subscription segments?
- How do plan and contract types relate to churn patterns?
- What revenue may be exposed to cancellation?
- How do complaints and escalations vary across customers or churn groups?
- Which segments could be prioritized for further retention analysis?

## Technology Stack

- **Python:** data processing and analysis
- **Pandas / NumPy:** transformation, feature engineering, and calculations
- **SQLite / SQL:** structured data storage and querying
- **Matplotlib / Seaborn:** visual analysis
- **Jupyter Notebook:** exploratory workflow

## Analytical Workflow

1. Load and inspect the source data.
2. Prepare customer and subscription fields for analysis.
3. Create analysis-ready churn and customer-risk fields.
4. Use SQL/SQLite and Python to examine customer, plan, contract, and support patterns.
5. Visualize the results and identify areas for follow-up investigation.

## KPI Framework

The project README and analysis cover business measures such as:

- **Churn rate and retention** — customer loss and continuation patterns
- **Revenue at risk** — revenue associated with customers flagged for churn analysis
- **ARPU** — average revenue per user, where the required revenue fields are available
- **Support signals** — complaints and escalations
- **Segment comparisons** — churn patterns by plan and contract type

Use the notebook and queries as the source of truth for definitions and calculated values. A risk flag or score should not be interpreted as a validated predictive model unless it has been evaluated against an appropriate holdout dataset.

## Repository Contents

| File or folder | Purpose |
|---|---|
| `churn_analysis.ipynb` | Main notebook for analysis |
| `data.csv` | Input data |
| `exported_churn_data.csv` | Exported analysis data |
| `customer_churn.db` | SQLite database |
| `chap*.py`, `project1.py` | Supporting Python scripts; inspect each script for its specific role |

The repository also contains local-development and temporary files. These are not required for understanding the core analytical workflow and can be removed or excluded in a future cleanup.

## How to Run

1. Clone or download the repository.
2. Create and activate a Python virtual environment.
3. Install the required packages used by the notebook, including Pandas, NumPy, Matplotlib, Seaborn, and the Jupyter environment.
4. Open `churn_analysis.ipynb` and run the cells in order.
5. Check file paths and database locations if running on a different machine.

Exact dependency versions and a pinned `requirements.txt` should be added to make the workflow fully reproducible.

## Business Takeaways

The intended output is a more structured view of churn and potential retention priorities. A production-ready follow-up would validate the KPI definitions, quantify the highest-risk segments, test whether support signals are associated with churn, and estimate the financial impact of specific retention actions.

## Skills Demonstrated

Data cleaning · Feature engineering · Python analytics · SQL · SQLite · KPI design · Exploratory data analysis · Data visualization · Business problem framing

## Author

**Yazdan Ahmed**  
[GitHub Portfolio](https://github.com/YazdanAhmedData)
