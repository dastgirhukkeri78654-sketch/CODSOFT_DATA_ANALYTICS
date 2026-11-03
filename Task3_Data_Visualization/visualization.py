
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =========================================
# 1. LOAD AND PREPARE DATASET
# =========================================

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Task2_EDA" / "data" / "Online Retail.xlsx"

# Load dataset
df = pd.read_excel(file_path)

# Apply sales filters
sales_df = df[
    (~df["InvoiceNo"].astype(str).str.startswith("C")) &
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

# Calculate revenue
sales_df["Revenue"] = sales_df["Quantity"] * sales_df["UnitPrice"]

# Convert invoice date
sales_df["InvoiceDate"] = pd.to_datetime(sales_df["InvoiceDate"])

# Output folder
output_folder = Path(__file__).resolve().parent


# =========================================
# 2. MONTHLY SALES TREND - LINE CHART
# =========================================

sales_df["Month"] = sales_df["InvoiceDate"].dt.to_period("M")

monthly_sales = sales_df.groupby("Month")["Revenue"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2,
    label="Monthly Revenue"
)

plt.title("Monthly Sales Trend", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plt.savefig(output_folder / "monthly_sales_trend.png", dpi=300)

print("1. Monthly Sales Trend chart saved successfully!")


# =========================================
# 3. TOP 10 PRODUCTS - BAR CHART
# =========================================

top_products = (
    sales_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

plt.bar(
    top_products.index,
    top_products.values,
    label="Revenue"
)

plt.title("Top 10 Products by Revenue", fontsize=16)
plt.xlabel("Product Name")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45, ha="right")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig(output_folder / "top_10_products.png", dpi=300)

print("2. Top 10 Products Bar Chart saved successfully!")


# =========================================
# 4. COUNTRY-WISE SALES - PIE CHART
# =========================================

country_sales = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

# Select top 5 countries
top_5_countries = country_sales.head(5)

# Combine remaining countries
other_sales = country_sales.iloc[5:].sum()

pie_data = pd.concat([
    top_5_countries,
    pd.Series({"Others": other_sales})
])

plt.figure(figsize=(9, 7))

plt.pie(
    pie_data.values,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=140
)

plt.title("Country-wise Sales Distribution", fontsize=16)
plt.tight_layout()

plt.savefig(output_folder / "country_sales_distribution.png", dpi=300)

print("3. Country-wise Sales Pie Chart saved successfully!")


# =========================================
# 5. REVENUE DISTRIBUTION - HISTOGRAM
# =========================================

plt.figure(figsize=(10, 6))

plt.hist(
    sales_df["Revenue"],
    bins=50,
    edgecolor="black"
)

plt.title("Distribution of Transaction Revenue", fontsize=16)
plt.xlabel("Revenue (£)")
plt.ylabel("Frequency")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig(output_folder / "revenue_distribution.png", dpi=300)

print("4. Revenue Distribution Histogram saved successfully!")


# =========================================
# 6. QUANTITY VS REVENUE - SCATTER PLOT
# =========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    sales_df["Quantity"],
    sales_df["Revenue"],
    alpha=0.3,
    label="Sales Transactions"
)

plt.title("Quantity vs Revenue", fontsize=16)
plt.xlabel("Quantity Sold")
plt.ylabel("Revenue (£)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(output_folder / "quantity_vs_revenue.png", dpi=300)

print("5. Quantity vs Revenue Scatter Plot saved successfully!")

# =========================================
# 7. DISPLAY ALL FOUR CHARTS
# =========================================

plt.show()


# =========================================
# 8. COMPLETION MESSAGE
# =========================================

print("\n========== TASK 3 PROGRESS ==========")
print("All four charts generated successfully!")

print("\nSaved chart files:")
print("1. monthly_sales_trend.png")
print("2. top_10_products.png")
print("3. country_sales_distribution.png")
print("4. revenue_distribution.png")

print("=====================================")

print("\nTop 10 Products by Revenue:")
print(top_products)
