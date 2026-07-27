\# Superstore Sales \& Profit Dashboard



\*\*By Lakshmishree A/P Balasubramaniam\*\*



An interactive dashboard analyzing sales, profit, and discounting patterns in a retail superstore dataset, built to identify actionable business insights.



\## Dataset

"Superstore Dataset" (Kaggle) — 9,994 orders across 21 columns, covering 2014-2017.

Note: this dataset had no missing values or duplicates; cleaning involved primarily type corrections (date parsing, postal code as categorical).



\## Key Insights

1\. \*\*Discounts of 30% or more are consistently associated with unprofitable orders\*\*, across all product categories — not isolated to any single category or sub-category.

2\. \*\*Sales are strongly seasonal\*\*, peaking in September, November, and December (likely tied to back-to-school and holiday shopping), with January-February consistently the weakest months.

3\. \*\*The Central region's comparatively weak profit margin (\~8% vs West's \~15%) is associated with its notably higher average discount rate (24% vs West's 11%)\*\*, connecting the regional pattern to the broader discount finding.



\## Screenshots

!\[Dashboard Overview](screenshots/overview.png)

\## Tools

Python, Pandas, Matplotlib/Seaborn (EDA), Streamlit + Plotly (dashboard)



\## How to Run

\\`\\`\\`

pip install -r requirements.txt

streamlit run app.py

\\`\\`\\`



\## Limitations

\- Discount-profit relationship is correlational, not causal — other unmeasured factors (e.g., specific product cost structures) may contribute.

\- Seasonality explanation (back-to-school/holiday) is a plausible interpretation, not confirmed by the data itself.

