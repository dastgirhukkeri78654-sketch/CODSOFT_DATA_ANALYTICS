# Task 2: Exploratory Data Analysis (EDA)

## 1. Project Overview
This project performs Exploratory Data Analysis (EDA) on the Online Retail dataset using Python and Pandas.

The purpose is to understand sales performance, customer purchasing behaviour, product revenue and business trends.

## 2. Dataset Information
- Dataset: Online Retail
- Source: UCI Machine Learning Repository (downloaded through Kaggle)
- Original records: 541,909
- Columns: 8
- Period: December 2010 – December 2011
- Currency: British Pound (£)

## 3. Tools and Technologies
- Python
- Pandas
- VS Code
- Jupyter-style data analysis using Python scripts

## 4. Data Inspection and Quality
The dataset was checked for missing values, duplicate records and unusual entries.

Findings:
- Missing CustomerID values: 135,080
- Missing Description values: 1,454
- Duplicate records: 5,268
- Cancellation-related records: 9,288
- Negative quantity records: 10,624
- Zero-price records: 2,515
- Negative-price records: 2

## 5. Sales Analysis
For gross positive sales analysis, records with cancellation invoice numbers, non-positive quantities and non-positive unit prices were excluded.

Revenue was calculated as:

`Revenue = Quantity × UnitPrice`

Results:
- Valid sales records: 530,104
- Excluded records: 11,805
- Gross positive sales value: £10,666,684.54
- Total quantity sold: 5,588,376
- Average transaction-line revenue: £20.12
- Unique customers in sales: 4,338

## 6. Key Findings

### Monthly Sales
- Best month: November 2011
- Gross sales value: £1,509,496.33

### Top Countries
- United Kingdom: £9,025,222.08
- Netherlands: £285,446.34
- EIRE: £283,453.96

### Top Products
- DOTCOM POSTAGE: £206,248.77
- REGENCY CAKESTAND 3 TIER: £174,484.74
- PAPER CRAFT, LITTLE BIRDIE: £168,469.60

Note: DOTCOM POSTAGE is a postage-related item.

### Sales by Weekday
- Highest sales: Thursday (£2,203,161.24)
- Second highest: Tuesday (£2,178,632.61)
- Lowest recorded sales: Sunday (£813,827.61)

Saturday had no qualifying sales records in the filtered dataset.

### Top Customers
- Customer 14646: £280,206.02
- Customer 18102: £259,657.30
- Customer 17450: £194,550.79

### Outlier Investigation
The Interquartile Range (IQR) method was used to identify unusual transaction-line revenue values.

- Lower limit: -£17.18
- Upper limit: £38.63
- Outlier records: 42,651
- Highest transaction-line revenue: £168,469.60

Outliers may represent bulk purchases or unusual transactions and are not automatically errors.

## 7. Business Insights
1. The United Kingdom generated the largest share of gross sales value.
2. November 2011 was the strongest sales month.
3. Thursday had the highest recorded weekday sales.
4. A small group of customers contributed substantial revenue.
5. Some transaction lines had unusually high revenue and may require further investigation.

## 8. Conclusion
This EDA project helped identify sales trends, top-performing countries, products and customers, as well as unusual transaction values.

Python and Pandas were used to inspect the dataset, calculate statistics and discover useful business insights.

**Note:** The reported sales value represents filtered positive sales transactions. It is not accounting net revenue after returns, refunds or adjustments.