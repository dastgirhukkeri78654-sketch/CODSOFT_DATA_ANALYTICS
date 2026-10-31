
import pandas as pd
from pathlib import Path

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = Path(__file__).parent / "data" / "Online Retail.xlsx"
df = pd.read_excel(file_path)

print("\n========== DATASET OVERVIEW ==========")

print("\nFirst five records:")
print(df.head())

print("\nDataset shape:", df.shape)

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:", df.duplicated().sum())

print("\nStatistical summary:")
print(df.describe())


# ==========================================
# 2. DATA QUALITY INVESTIGATION
# ==========================================

print("\n========== DATA QUALITY ==========")

is_cancelled = df["InvoiceNo"].astype(str).str.startswith("C")

print("Cancellation-related rows:", is_cancelled.sum())
print("Negative quantity rows:", (df["Quantity"] < 0).sum())
print("Zero price rows:", (df["UnitPrice"] == 0).sum())
print("Negative price rows:", (df["UnitPrice"] < 0).sum())
print("Unique customers:", df["CustomerID"].nunique())
print("Unique products:", df["StockCode"].nunique())

print("\nSample negative price records:")
print(
    df.loc[
        df["UnitPrice"] < 0,
        ["InvoiceNo", "StockCode", "Description", "UnitPrice"]
    ].head()
)


# ==========================================
# 3. SALES ANALYSIS
# ==========================================

print("\n========== SALES ANALYSIS ==========")

# Keep positive sales transactions
sales_df = df[
    (~is_cancelled) &
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

# Calculate transaction-line revenue
sales_df["Revenue"] = (
    sales_df["Quantity"] * sales_df["UnitPrice"]
)

print("Original records:", len(df))
print("Valid sales records:", len(sales_df))
print("Excluded records:", len(df) - len(sales_df))

print("Gross positive sales value:",
      round(sales_df["Revenue"].sum(), 2))

print("Total quantity sold:", sales_df["Quantity"].sum())

print("Average transaction-line revenue:",
      round(sales_df["Revenue"].mean(), 2))

print("Unique customers in sales:",
      sales_df["CustomerID"].nunique())


# ==========================================
# 4. MONTHLY SALES ANALYSIS
# ==========================================

print("\n========== MONTHLY SALES ==========")

sales_df["Month"] = sales_df["InvoiceDate"].dt.to_period("M")

monthly_sales = (
    sales_df.groupby("Month")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(monthly_sales)

print("Best sales month:", monthly_sales.index[0])
print("Highest monthly sales:",
      round(monthly_sales.iloc[0], 2))


# ==========================================
# 5. TOP 10 PRODUCTS
# ==========================================

print("\n========== TOP 10 PRODUCTS ==========")

top_products = (
    sales_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)


# ==========================================
# 6. TOP 10 COUNTRIES
# ==========================================

print("\n========== TOP 10 COUNTRIES ==========")

top_countries = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_countries)


# ==========================================
# 7. SALES BY WEEKDAY
# ==========================================

print("\n========== SALES BY WEEKDAY ==========")

sales_df["Day"] = sales_df["InvoiceDate"].dt.day_name()

day_sales = (
    sales_df.groupby("Day")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print(day_sales)

print("Best sales day:", day_sales.index[0])


# ==========================================
# 8. TOP 10 CUSTOMERS
# ==========================================

print("\n========== TOP 10 CUSTOMERS ==========")

top_customers = (
    sales_df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_customers)


# ==========================================
# 9. OUTLIER INVESTIGATION (IQR METHOD)
# ==========================================

print("\n========== OUTLIER INVESTIGATION ==========")

print(sales_df["Revenue"].describe())

Q1 = sales_df["Revenue"].quantile(0.25)
Q3 = sales_df["Revenue"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - (1.5 * IQR)
upper_limit = Q3 + (1.5 * IQR)

outliers = sales_df[
    (sales_df["Revenue"] < lower_limit) |
    (sales_df["Revenue"] > upper_limit)
]

print("Q1:", round(Q1, 2))
print("Q3:", round(Q3, 2))
print("IQR:", round(IQR, 2))
print("Lower limit:", round(lower_limit, 2))
print("Upper limit:", round(upper_limit, 2))
print("Number of outlier records:", len(outliers))
print("Highest transaction-line revenue:",
      round(sales_df["Revenue"].max(), 2))


print("\n========== EDA COMPLETED SUCCESSFULLY ==========")
