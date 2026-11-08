# Task 5: Web Data Extraction – Online Book Data

## Project Overview
This project was completed as part of the CodSoft Data Analytics Internship.

The objective was to extract book information from the practice website Books to Scrape using Python web scraping techniques.

Website: https://books.toscrape.com/

## Technologies Used
- Python
- Requests
- BeautifulSoup
- Pandas
- Visual Studio Code

## Data Extracted
The scraper collected the following information:

- Book Title
- Book Price (£)
- Availability
- Star Rating
- Product URL

## Data Collection Process
1. Sent HTTP requests using the Requests library.
2. Retrieved HTML content from the website.
3. Parsed HTML using BeautifulSoup.
4. Extracted information from book product elements.
5. Scraped all 50 catalogue pages.
6. Collected 1,000 book records.
7. Removed duplicate product URLs.
8. Converted book prices into numeric values.
9. Exported the processed data into a CSV file.

## Project Results

- Total pages scraped: 50
- Total books extracted: 1,000
- Average book price: £35.07
- Highest book price: £59.99
- Lowest book price: £10.00

## Rating Distribution

| Rating | Number of Books |
|--------|----------------:|
| One    | 226 |
| Two    | 196 |
| Three  | 203 |
| Four   | 179 |
| Five   | 196 |

## Project Structure

Task5_Web_Extraction/
- web_scraping.py
- extracted_books.csv
- README.md

## How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas