
# ============================================
# CODSOFT TASK 4: CUSTOMER DATA ANALYSIS
# Customer Behaviour & RFM Segmentation
# ============================================

import os
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load dataset
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    BASE_DIR, "..", "Task2_EDA", "data", "Online Retail.xlsx"
)

df = pd.read_excel(file_path)

print("\n========== DATA CLEANING ==========")

# Step 2: Remove duplicate records
df = df.drop_duplicates()

# Step 3: Remove missing Customer IDs
df = df.dropna(subset=["CustomerID"])

# Step 4: Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Step 5: Keep only valid sales
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# Step 6: Calculate revenue
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("Cleaned Records:", len(df))
print("Unique Customers:", df["CustomerID"].nunique())
print("Total Revenue: £", round(df["Revenue"].sum(), 2))

# ============================================
# RFM ANALYSIS
# ============================================

print("\n========== RFM CUSTOMER ANALYSIS ==========")

# Reference date: one day after the last transaction
reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Calculate RFM values for each customer
rfm = df.groupby("CustomerID").agg({
    "InvoiceDate": lambda x: (reference_date - x.max()).days,
    "InvoiceNo": "nunique",
    "Revenue": "sum"
})

# Rename columns
rfm = rfm.rename(columns={
    "InvoiceDate": "Recency",
    "InvoiceNo": "Frequency",
    "Revenue": "Monetary"
})

print("\nFirst 5 RFM Records:")
print(rfm.head())

# ============================================
# RFM SCORING
# ============================================

# Rank first to handle customers with equal values
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    4,
    labels=[4, 3, 2, 1]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    4,
    labels=[1, 2, 3, 4]
).astype(int)

rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

# ============================================
# CUSTOMER SEGMENTATION
# ============================================

def segment_customer(row):

    if row["RFM_Score"] in ["444", "443", "434", "433"]:
        return "Champions"

    elif row["R_Score"] >= 3 and row["F_Score"] >= 3:
        return "Loyal Customers"

    elif row["R_Score"] >= 3:
        return "Recent Customers"

    elif row["R_Score"] <= 2 and row["F_Score"] >= 3:
        return "At Risk"

    else:
        return "Regular Customers"


rfm["Segment"] = rfm.apply(segment_customer, axis=1)

# ============================================
# DISPLAY RESULTS
# ============================================

print("\n========== CUSTOMER SEGMENTS ==========")

print(rfm["Segment"].value_counts())

print("\nAverage RFM Values:")
print(rfm.groupby("Segment")[
    ["Recency", "Frequency", "Monetary"]
].mean().round(2))

# ============================================
# VISUALIZATION 1: CUSTOMER SEGMENTS
# ============================================

segment_counts = rfm["Segment"].value_counts()

plt.figure(figsize=(10, 6))
segment_counts.plot(kind="bar")

plt.title("Customer Distribution by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "customer_segments.png"),
    dpi=300
)
plt.close()

# ============================================
# VISUALIZATION 2: AVERAGE SPENDING
# ============================================

segment_revenue = rfm.groupby("Segment")["Monetary"].mean().sort_values(
    ascending=False
)

plt.figure(figsize=(10, 6))
segment_revenue.plot(kind="bar")

plt.title("Average Customer Spending by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Spending (£)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "average_spending.png"),
    dpi=300
)
plt.close()

# ============================================
# VISUALIZATION 3: CUSTOMER RECENCY
# ============================================

segment_recency = rfm.groupby("Segment")["Recency"].mean().sort_values()

plt.figure(figsize=(10, 6))
segment_recency.plot(kind="bar")

plt.title("Average Days Since Last Purchase")
plt.xlabel("Customer Segment")
plt.ylabel("Average Recency (Days)")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "customer_recency.png"),
    dpi=300
)
plt.close()

print("\nThree customer analysis charts saved successfully!")

# ============================================
# SAVE CUSTOMER ANALYSIS
# ============================================

output_file = os.path.join(BASE_DIR, "customer_rfm_analysis.csv")

rfm.to_csv(output_file)

print("\nRFM Analysis saved to:", output_file)

print("\n========== TASK 4 ANALYSIS COMPLETED ==========")
