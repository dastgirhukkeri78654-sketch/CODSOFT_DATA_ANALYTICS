# Task 4: Customer Behaviour & Segmentation Analysis

## Project Overview

This project analyses customer purchasing behaviour using the Online Retail dataset. It applies RFM (Recency, Frequency, Monetary) analysis to understand customer activity, identify valuable customers, and divide customers into meaningful segments.

## Objectives

- Clean and prepare customer transaction data.
- Calculate customer Recency, Frequency, and Monetary values.
- Assign RFM scores to customers.
- Segment customers based on purchasing behaviour.
- Visualize customer distribution, spending, and recency.
- Generate business insights from customer data.

## Tools and Technologies

- Python
- Pandas
- Matplotlib
- Excel dataset
- Visual Studio Code

## Dataset

**Dataset:** Online Retail

**Original dataset:** 541,909 records and 8 columns.

The dataset contains invoice numbers, product codes, descriptions, quantities, invoice dates, unit prices, customer IDs, and countries.

## Data Cleaning

The following cleaning operations were performed:

1. Removed duplicate records.
2. Removed records with missing Customer IDs.
3. Excluded cancelled invoices.
4. Removed transactions with non-positive quantities or unit prices.
5. Calculated revenue using Quantity × UnitPrice.

After cleaning, the analysis retained **392,692 transaction records** and **4,338 unique customers**.

## RFM Analysis

RFM stands for:

- **Recency:** Number of days since the customer's most recent purchase.
- **Frequency:** Number of distinct invoices associated with the customer.
- **Monetary:** Total spending by the customer.

The reference date was set to one day after the latest transaction date.

Customers were assigned scores from 1 to 4 for each RFM measure. Higher Recency scores represent more recent purchases, while higher Frequency and Monetary scores represent more frequent purchases and higher spending.

## Customer Segmentation Results

| Customer Segment | Number of Customers |
|---|---:|
| Regular Customers | 1,514 |
| Champions | 773 |
| Loyal Customers | 741 |
| At Risk | 655 |
| Recent Customers | 655 |
| **Total** | **4,338** |

### Average Customer Metrics

| Segment | Recency (Days) | Frequency | Monetary (£) |
|---|---:|---:|---:|
| At Risk | 118.26 | 4.18 | 1,606.72 |
| Champions | 7.71 | 11.49 | 6,255.15 |
| Loyal Customers | 27.81 | 5.49 | 2,341.04 |
| Recent Customers | 24.86 | 1.45 | 754.01 |
| Regular Customers | 185.68 | 1.25 | 509.24 |

## Visualizations

The project generates three charts:

1. `customer_segments.png` – Customer distribution across segments.
2. `average_spending.png` – Average spending for each customer segment.
3. `customer_recency.png` – Average days since the last purchase for each segment.

## Key Business Insights

- Champions have the highest average spending and purchase frequency.
- Loyal Customers show repeat purchasing behaviour.
- At Risk customers have relatively high purchase frequency but have not purchased recently.
- Recent Customers have purchased recently but have comparatively low purchase frequency.
- Regular Customers form the largest segment and have the lowest average purchase frequency.

## Business Recommendations

- Reward Champions through loyalty programs and exclusive offers.
- Encourage Loyal Customers with personalized recommendations.
- Re-engage At Risk customers through targeted campaigns.
- Encourage Recent Customers to make repeat purchases.
- Use personalized promotions to increase engagement among Regular Customers.

## Project Files

```text
Task4_Customer_Analysis/
│
├── customer_analysis.py
├── customer_rfm_analysis.csv
├── customer_segments.png
├── average_spending.png
├── customer_recency.png
└── README.md
```

## How to Run

Install the required libraries:

```bash
pip install pandas matplotlib openpyxl
```

Run the program from the repository root:

```bash
python Task4_Customer_Analysis/customer_analysis.py
```

The script reads the Online Retail Excel dataset from the Task 2 folder and generates the RFM CSV file and visualization charts.

## Conclusion

This project demonstrates how Python-based customer analytics can help businesses understand purchasing patterns, identify high-value customers, and develop customer retention strategies using RFM analysis.
