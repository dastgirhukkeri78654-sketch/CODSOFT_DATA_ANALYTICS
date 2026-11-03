# Task 3 – Data Visualization Dashboard

## CodSoft Data Analytics Internship

### Project Overview
This project focuses on visualizing and analyzing an Online Retail dataset using Python. The objective is to transform raw sales data into meaningful charts and business insights.

### Dataset
- Dataset: Online Retail Dataset
- Source: UCI Online Retail Dataset (downloaded through Kaggle)
- Total original records: 541,909
- Columns: 8
- Period: December 2010 – December 2011
- Currency: GBP (£)

### Tools and Technologies
- Python
- Pandas
- Matplotlib
- NumPy
- VS Code
- Jupyter/Python environment

### Data Preparation
The dataset was filtered to exclude:
- Cancelled invoices (invoice numbers beginning with C)
- Transactions with zero or negative quantities
- Transactions with zero or negative unit prices

Revenue was calculated using:

`Revenue = Quantity × UnitPrice`

The analysis represents gross positive sales value, not net accounting revenue after returns or adjustments.

### Visualizations Created

1. **Monthly Sales Trend – Line Chart**  
   Shows how sales revenue changes over time and identifies monthly sales patterns.

2. **Top 10 Products – Bar Chart**  
   Identifies the ten product descriptions with the highest total revenue.

3. **Country-wise Sales Distribution – Pie Chart**  
   Shows the revenue contribution of the top five countries and combines the remaining countries into Others.

4. **Revenue Distribution – Histogram**  
   Shows the distribution of transaction-line revenue. A logarithmic horizontal scale helps display highly skewed values.

5. **Quantity vs Revenue – Scatter Plot**  
   Examines the relationship between quantity sold and transaction-line revenue using logarithmic axes.

### Dashboard
A combined dashboard was created containing all five visualizations and four key business metrics:
- Total gross sales
- Total quantity sold
- Unique invoices
- Unique customers

### Key Business Insights
- November 2011 recorded the highest monthly gross positive sales value.
- February 2011 recorded the lowest monthly gross positive sales value.
- The United Kingdom contributed approximately 84.6% of gross positive sales value.
- DOTCOM POSTAGE was the highest-revenue transaction description.
- Revenue values are highly skewed, with a small number of unusually large transactions.
- Quantity and revenue generally show a positive relationship, although product prices and order sizes vary.

### Project Files
- `visualization.py` – Generates the five individual charts.
- `dashboard.py` – Creates the combined sales dashboard.
- `monthly_sales_trend.png`
- `top_10_products.png`
- `country_sales_distribution.png`
- `revenue_distribution.png`
- `quantity_vs_revenue.png`
- `sales_dashboard.png`

### Conclusion
This project demonstrates how Python-based data visualization can help identify sales trends, understand product performance, compare country-wise contributions, and explore transaction patterns.

The dashboard converts a large retail dataset into visual information that can support business analysis and decision-making.

**Internship:** CodSoft Data Analytics Internship  
**Task:** Task 3 – Data Visualization Dashboard