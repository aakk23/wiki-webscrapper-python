# 📊 Wikipedia Scraper: Largest U.S. Companies by Revenue

This project is a simple Python script that scrapes a Wikipedia page to extract a list of the largest companies in the United States by revenue. The data is then stored in a structured CSV format for further analysis or reference.

---

## 🧰 Tech Stack

- **Python**
- **BeautifulSoup (bs4)** – For HTML parsing and web scraping
- **Pandas** – For data manipulation and exporting to CSV
- **Requests** – For sending HTTP requests

---

## 🔍 What It Does

- Sends a request to the Wikipedia page:  
  [List of largest companies in the United States by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)
- Parses the first HTML table on the page
- Extracts all rows and cleans the data
- Saves the result as a CSV file locally

---

## 📁 Output

The scraped data is saved to: local storage


You can modify this path as needed for your environment.

---
## 📌 Notes
This script assumes the target table is the first one on the page. If Wikipedia changes the structure, the script may need to be updated.

Always follow Wikipedia's Terms of Use when scraping.

## 📌 Author: Aakkash Aswin
This project is a part of my data analytics portfolio and highlights my Python proficiency relevant to data analyst roles.
### Connect with me on [LinkedIn](http://www.linkedin.com/in/aakkash-aswin)


