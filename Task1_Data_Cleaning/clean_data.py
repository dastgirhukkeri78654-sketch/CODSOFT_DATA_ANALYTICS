
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# 1. Load the original dataset
# --------------------------------------------------
data_folder = Path("data")
raw_file = data_folder / "raw_customer_sales.csv"
clean_file = data_folder / "cleaned_customer_sales.csv"

df = pd.read_csv(raw_file)

print("ORIGINAL DATASET SHAPE:", df.shape)

# --------------------------------------------------
# 2. Remove exact duplicate rows
# --------------------------------------------------
duplicate_count = df.duplicated().sum()
print("Exact duplicate rows found:", duplicate_count)

df = df.drop_duplicates().copy()

# --------------------------------------------------
# 3. Clean text columns
# --------------------------------------------------
df["Name"] = df["Name"].str.strip()

df["City"] = (
    df["City"]
    .str.strip()
    .str.title()
    .fillna("Unknown")
)

# --------------------------------------------------
# 4. Correct and convert Age
# --------------------------------------------------
df["Age"] = df["Age"].replace({
    "thirty": "30",
    "THIRTY": "30",
    "Thirty": "30"
})

df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

missing_age = df["Age"].isna().sum()
print("Missing/invalid ages before filling:", missing_age)

age_median = df["Age"].median()

# Ages should be whole numbers in this dataset
df["Age"] = df["Age"].fillna(round(age_median)).astype("Int64")

# --------------------------------------------------
# 5. Correct and convert Purchase_Amount
# --------------------------------------------------
df["Purchase_Amount"] = pd.to_numeric(
    df["Purchase_Amount"], errors="coerce"
)

missing_amount = df["Purchase_Amount"].isna().sum()
print("Missing/invalid purchase amounts before filling:",
      missing_amount)

amount_median = df["Purchase_Amount"].median()

df["Purchase_Amount"] = df["Purchase_Amount"].fillna(amount_median)

# --------------------------------------------------
# 6. Convert Purchase_Date to datetime
# --------------------------------------------------
df["Purchase_Date"] = pd.to_datetime(
    df["Purchase_Date"], errors="coerce"
)

print("Missing/invalid dates after conversion:",
      df["Purchase_Date"].isna().sum())

# --------------------------------------------------
# 7. Validate the cleaned dataset
# --------------------------------------------------
print("\n--- CLEANED DATASET ---")
print(df.to_string(index=False))

print("\n--- CLEANED DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES AFTER CLEANING ---")
print(df.isna().sum())

print("\n--- DUPLICATES AFTER CLEANING ---")
print(df.duplicated().sum())

# --------------------------------------------------
# 8. Save cleaned dataset
# --------------------------------------------------
df.to_csv(clean_file, index=False)

print("\nOriginal rows after loading:", 10)
print("Final rows:", len(df))
print("Cleaned file saved to:", clean_file)
print("\nTask 1 cleaning completed successfully!")
