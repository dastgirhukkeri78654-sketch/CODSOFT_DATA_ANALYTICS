# CodSoft Data Analytics Internship — Task 1

## Data Cleaning and Preprocessing Using Python

### Project Overview
This project demonstrates data cleaning and preprocessing using Python and Pandas. The dataset contains customer information, cities, ages, purchase amounts, and purchase dates.

### Objectives
- Inspect the original dataset.
- Identify duplicate rows and missing values.
- Standardize inconsistent text entries.
- Convert columns to appropriate data types.
- Handle missing and invalid values.
- Export the cleaned dataset as a CSV file.

### Tools and Technologies
- Python
- Pandas
- VS Code

### Data Cleaning Steps
1. Loaded the original CSV file.
2. Identified and removed exact duplicate rows.
3. Standardized customer names and city names.
4. Converted ages and purchase amounts to numeric values.
5. Filled missing or invalid ages and purchase amounts using median-based imputation.
6. Converted purchase dates to datetime format.
7. Validated the cleaned dataset and exported it to CSV.

### Results
- Original records: 10
- Duplicate rows removed: 1
- Final records: 9
- Final columns: 6
- Remaining invalid or missing purchase dates: 1 (`NaT`)

The invalid purchase date was retained as a missing datetime value because the original text did not provide enough information to infer the correct date.

### Project Structure
```text
CODSOFT_TASK1/
├── clean_data.py
├── data/
│   ├── raw_customer_sales.csv
│   └── cleaned_customer_sales.csv
└── README.md
```

### How to Run
1. Install Python.
2. Install Pandas using `pip install pandas`.
3. Run `python clean_data.py` from the project folder.

### Note
The dataset used in this demonstration is a small practice dataset created for learning data cleaning and preprocessing.
    