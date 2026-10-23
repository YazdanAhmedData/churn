# 📉 Customer Churn Analysis & Intelligence | Python, Pandas, SQL & SQLite

**Portfolio case study · Customer retention · Revenue exposure · Support analytics**

## Executive Summary
This project brings customer, subscription, and support data together to explore churn, retention, plan behaviour, acquisition source, customer tenure, recurring charges, and service escalations. Python and Pandas support preparation and KPI calculations; SQLite/SQL provides structured data access; visualisations make segment differences easier to inspect.

The notebook currently contains **21 subscription records**, so its numerical findings are useful as a demonstration of the analytical workflow, not as statistically reliable company-wide estimates.

## Business Problem
Customer churn reduces recurring revenue and can signal friction in pricing, product fit, onboarding, or support. A business needs more than a single churn percentage: it needs to know **which customer groups are leaving, how much recurring charge is associated with those customers, and which operational signals merit investigation**.

The analysis connects subscription attributes with customer and support information to build a starting point for retention monitoring.

## Dataset & Modelled Fields
The notebook combines three tables:
- **Customer:** customer ID, country/state, gender, date of birth, interests and location fields.
- **Subscription:** start/renewal/cancellation dates, subscription source, plan, contract, cancellation reason, monthly charges, CLTV and churn score.
- **Support:** complaint date, escalation flag, CSAT score and comment.

Engineered fields include `churn_flag`, `churn_risk`, `complaint_count`, `tenure_days`, and cancellation month.

## KPI Scorecard — Results in the Current Notebook
| KPI | Current notebook result | Interpretation |
|---|---:|---|
| Churn rate | **28.57%** | 6 cancellations in a 21-record subscription sample, before any further validation |
| Retention rate | **71.43%** | Complement of the notebook's churn rate |
| Average monthly charge (ARPU proxy) | **18.85** | Mean of the `monthly_charges` field; currency/scale should be documented |
| Average tenure | **1,542 days** | Average calculated tenure; active customers are measured to the notebook's current date |
| Monthly charges associated with churned rows | **73.94** | Sum of monthly charges for rows flagged as churned; not a forecast of lifetime revenue loss |
| Escalation rate | **19.05%** | Share of rows marked escalated in the merged analysis |
| Average complaints per customer | **0.43** | Complaint count divided by unique customer count |

### Segment findings visible in the notebook
- **Basic plan churn: 60.00% (3 of 5 records).**
- **Standard plan churn: 22.22% (2 of 9 records).**
- **Premium plan churn: 14.29% (1 of 7 records).**
- **Referral-source churn: 83.33% (5 of 6 records); paid-source churn: 16.67% (1 of 6); organic-source churn: 0% in the sample.**

**Important:** the segment counts are very small. Treat these as leads for investigation, not proof that a plan or acquisition channel causes churn. The data and joins should be validated before using the values in a business presentation.

## Business Insights & Recommendations
1. **Investigate Basic-plan churn first.** Its observed rate is highest in this small sample. Review cancellation reasons, pricing fit, onboarding and support history before proposing plan changes.
2. **Audit referral-acquired customers.** The notebook shows unusually high churn in this group. Check whether referrals are low-intent, whether source labels are consistent, and whether the cohort has had enough time to renew.
3. **Review customer support friction.** Escalations, CSAT and complaint history can help identify service experiences associated with cancellation. Association does not establish causation.
4. **Prioritise by recurring charge and customer value.** Combine churn status with monthly charges and CLTV so retention effort is not based on churn probability alone.
5. **Track churn by month and contract.** A trend and contract-type comparison can reveal whether the issue is concentrated around renewal or a particular period.

## Analytical Workflow
1. Read customer, subscription and support tables from SQLite.
2. Inspect schemas, types and missing values.
3. Convert subscription and cancellation dates to datetime.
4. Derive churn flag, tenure, complaint counts and risk bands.
5. Merge the datasets and calculate churn, retention, ARPU proxy, tenure, revenue exposure and support KPIs.
6. Compare plan, state and subscription source; visualise patterns and prepare follow-up questions.

## KPI Definitions
- **Churn rate:** cancelled customers ÷ eligible customers in the defined cohort.
- **Retention rate:** 1 − churn rate, using the same cohort and period.
- **ARPU proxy:** mean monthly charges per customer; state the unit and period.
- **Recurring charges at risk:** sum of monthly charges for churned customers. This is not the same as lifetime revenue loss.
- **Escalation rate:** escalated support records ÷ eligible support records. Decide whether the unit is a ticket or a customer.
- **Average tenure:** average days from subscription start to cancellation for churned users, or to a clearly defined as-of date for active users.

## Technical Stack
Python · Pandas · NumPy · SQLite · SQL · Matplotlib · Seaborn · Jupyter Notebook

## Repository Guide
| File | Purpose |
|---|---|
| `churn_analysis.ipynb` | Main analysis, KPI calculations and visualisations |
| `data.csv` | Input data |
| `exported_churn_data.csv` | Exported analysis data |
| `customer_churn.db` | SQLite database |
| `chap*.py`, `project1.py` | Supporting scripts; review each file for its specific role |

## Reproduce the Analysis
1. Clone the repository and create a virtual environment.
2. Install Pandas, NumPy, Matplotlib, Seaborn and Jupyter.
3. Confirm database and CSV paths in the notebook.
4. Run the notebook cells in order and compare the outputs above with your fresh results.
5. Record package versions in a `requirements.txt` for repeatability.

## Data Quality & Limitations
- The subscription sample is only 21 records; segment percentages can move sharply with one additional customer.
- Support data can contain multiple records per customer. Aggregate support to customer-level before joining if the KPI's grain is one customer; otherwise one-to-many joins can duplicate subscriptions and distort churn metrics.
- Define the cohort and reporting date before comparing active and cancelled customers.
- Document the units for monthly charges and CLTV.
- The churn-risk bands are rule-based thresholds on `churn_score`, not a validated predictive model. No predictive performance should be claimed without holdout evaluation.

## Next Steps
- Build a customer-level clean analytical table with documented join grain.
- Add a month-by-month cohort view and cancellation-reason analysis.
- Evaluate churn prediction with a time-aware holdout and appropriate classification metrics if the project is extended into modelling.
- Add a final business findings table after data-quality checks.

## Author
**Yazdan Ahmed** · [GitHub Portfolio](https://github.com/YazdanAhmedData)
