
# ==================================================
# CODSOFT TASK 5: WEB DATA EXTRACTION
# Project: Online Book Data Extraction
# ==================================================

import os
import time
import requests
import pandas as pd

from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Step 1: Project directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

# Step 2: Website request settings
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; CodSoftStudentProject/1.0)"
}

# Step 3: Store extracted information
books_data = []

print("\n========== WEB DATA EXTRACTION STARTED ==========")

# Step 4: Extract data from all 50 pages
for page in range(1, 51):

    url = BASE_URL.format(page)

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")

        if not books:
            print(f"No books found on page {page}.")
            continue

        for book in books:

            # Extract title
            title = book.h3.a["title"]

            # Extract price
            price = book.select_one(".price_color").get_text(strip=True)

            # Extract availability
            availability = book.select_one(
                ".availability"
            ).get_text(" ", strip=True)

            # Extract star rating
            rating_element = book.select_one(".star-rating")
            rating = rating_element["class"][1]

            # Extract product URL
            relative_url = book.h3.a["href"]
            product_url = urljoin(url, relative_url)

            # Store information
            books_data.append({
                "Title": title,
                "Price": price,
                "Availability": availability,
                "Rating": rating,
                "Product_URL": product_url
            })

        print(
            f"Page {page}/50 completed | "
            f"Books collected: {len(books_data)}"
        )

        # Small delay between requests
        time.sleep(0.2)

    except requests.exceptions.RequestException as error:
        print(f"Error on page {page}: {error}")

# ==================================================
# STEP 5: CONVERT DATA INTO DATAFRAME
# ==================================================

print("\n========== DATA PROCESSING ==========")

df = pd.DataFrame(books_data)

# Remove duplicate records
df = df.drop_duplicates(subset=["Product_URL"])

# Convert price into numeric values
df["Price"] = (
    df["Price"]
    .str.replace(r"[^\d.]", "", regex=True)
    .astype(float)
)

# ==================================================
# STEP 6: SAVE EXTRACTED DATA
# ==================================================

output_file = os.path.join(
    BASE_DIR,
    "extracted_books.csv"
)

df.to_csv(output_file, index=False, encoding="utf-8-sig")

# ==================================================
# STEP 7: DISPLAY RESULTS
# ==================================================

print("\n========== EXTRACTION SUMMARY ==========")

print("Total Books Extracted:", len(df))

print("\nFirst 10 Books:")
print(df.head(10).to_string(index=False))

print("\nAverage Book Price: £", round(df["Price"].mean(), 2))

print("Highest Book Price: £", df["Price"].max())

print("Lowest Book Price: £", df["Price"].min())

print("\nRating Distribution:")
print(df["Rating"].value_counts())

print("\nCSV File Saved:", output_file)

print("\n========== TASK 5 COMPLETED ==========")
