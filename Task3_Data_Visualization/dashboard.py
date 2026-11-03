
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# =========================================
# 1. LOAD AND PREPARE DATA
# =========================================

project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "Task2_EDA" / "data" / "Online Retail.xlsx"

df = pd.read_excel(file_path)

sales_df = df[
    (~df["InvoiceNo"].astype(str).str.startswith("C")) &
    (df["Quantity"] > 0) &
    (df["UnitPrice"] > 0)
].copy()

sales_df["Revenue"] = sales_df["Quantity"] * sales_df["UnitPrice"]
sales_df["InvoiceDate"] = pd.to_datetime(sales_df["InvoiceDate"])

output_folder = Path(__file__).resolve().parent

# =========================================
# 2. PREPARE CHART DATA
# =========================================

# Monthly sales
sales_df["Month"] = sales_df["InvoiceDate"].dt.to_period("M")

monthly_sales = sales_df.groupby("Month")["Revenue"].sum()
monthly_sales.index = monthly_sales.index.astype(str)

# Top 10 products
top_products = (
    sales_df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# Country sales
country_sales = (
    sales_df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

top_5 = country_sales.head(5)
other_sales = country_sales.iloc[5:].sum()

pie_data = pd.concat([
    top_5,
    pd.Series({"Others": other_sales})
])

# =========================================
# 3. CREATE DASHBOARD
# =========================================

fig, axes = plt.subplots(2, 3, figsize=(20, 12))

fig.suptitle(
    "ONLINE RETAIL SALES ANALYSIS DASHBOARD",
    fontsize=22,
    fontweight="bold"
)

# -----------------------------------------
# CHART 1: MONTHLY SALES TREND
# -----------------------------------------

axes[0, 0].plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2
)

axes[0, 0].set_title("Monthly Sales Trend")
axes[0, 0].set_xlabel("Month")
axes[0, 0].set_ylabel("Revenue (£)")
axes[0, 0].tick_params(axis="x", rotation=45)
axes[0, 0].grid(True, alpha=0.3)

# -----------------------------------------
# CHART 2: TOP 10 PRODUCTS
# -----------------------------------------

axes[0, 1].barh(
    top_products.index[::-1],
    top_products.values[::-1]
)

axes[0, 1].set_title("Top 10 Products by Revenue")
axes[0, 1].set_xlabel("Revenue (£)")
axes[0, 1].grid(axis="x", alpha=0.3)

# -----------------------------------------
# CHART 3: COUNTRY-WISE SALES
# -----------------------------------------

wedges, texts, autotexts = axes[0, 2].pie(
    pie_data.values,
    labels=None,
    autopct="%1.1f%%",
    startangle=140,
    pctdistance=0.75
)

axes[0, 2].set_title("Country-wise Sales Distribution")

axes[0, 2].legend(
    wedges,
    pie_data.index,
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)

# -----------------------------------------
# CHART 4: REVENUE DISTRIBUTION
# -----------------------------------------

min_revenue = sales_df["Revenue"].min()
max_revenue = sales_df["Revenue"].max()

log_bins = np.logspace(
    np.log10(min_revenue),
    np.log10(max_revenue),
    50
)

axes[1, 0].hist(
    sales_df["Revenue"],
    bins=log_bins,
    edgecolor="black"
)

axes[1, 0].set_xscale("log")
axes[1, 0].set_title("Revenue Distribution (Log Scale)")
axes[1, 0].set_xlabel("Revenue (£) - Log Scale")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].grid(True, alpha=0.3)

# -----------------------------------------
# CHART 5: QUANTITY VS REVENUE
# -----------------------------------------

axes[1, 1].scatter(
    sales_df["Quantity"],
    sales_df["Revenue"],
    alpha=0.25,
    s=12
)

axes[1, 1].set_xscale("log")
axes[1, 1].set_yscale("log")

axes[1, 1].set_title("Quantity vs Revenue (Log Scale)")
axes[1, 1].set_xlabel("Quantity Sold - Log Scale")
axes[1, 1].set_ylabel("Revenue (£) - Log Scale")
axes[1, 1].grid(True, alpha=0.3)

# -----------------------------------------
# CHART 6: KEY BUSINESS METRICS
# -----------------------------------------

axes[1, 2].axis("off")

total_revenue = sales_df["Revenue"].sum()
total_quantity = sales_df["Quantity"].sum()
total_transactions = sales_df["InvoiceNo"].nunique()
total_customers = sales_df["CustomerID"].nunique()

kpi_text = (
    "KEY BUSINESS METRICS\n\n"
    f"Total Gross Sales:\n£{total_revenue:,.2f}\n\n"
    f"Total Quantity Sold:\n{total_quantity:,.0f}\n\n"
    f"Unique Invoices:\n{total_transactions:,}\n\n"
    f"Unique Customers:\n{total_customers:,}"
)

axes[1, 2].text(
    0.05,
    0.95,
    kpi_text,
    fontsize=14,
    verticalalignment="top"
)

# =========================================
# 4. SAVE FINAL DASHBOARD
# =========================================

plt.tight_layout(rect=[0, 0, 1, 0.95])

dashboard_path = output_folder / "sales_dashboard.png"

plt.savefig(
    dashboard_path,
    dpi=300,
    bbox_inches="tight"
)

print("\n======================================")
print("SALES DASHBOARD CREATED SUCCESSFULLY!")
print("======================================")
print(f"Dashboard saved at: {dashboard_path}")

plt.show()
