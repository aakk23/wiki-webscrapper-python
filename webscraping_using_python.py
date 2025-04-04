# Importing required libraries
from bs4 import BeautifulSoup  # For parsing HTML content
import pandas as pd            # For working with tabular data and exporting to CSV
import requests                # For sending HTTP requests

# URL of the Wikipedia page to scrape
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

print("Sending request...")

# Sending a GET request to the Wikipedia page
page = requests.get(url)

# Parsing the page content using BeautifulSoup
soup = BeautifulSoup(page.text, features="html.parser")

# Finding all table elements and selecting the first one (contains the list of companies)
table = soup.find_all('table')[0]

# Extracting the table headers (column names)
table_title = table.find_all('th')
table_heading = [title.text.strip() for title in table_title]

# Creating an empty DataFrame with the extracted headers
df = pd.DataFrame(columns=table_heading)

# Finding all rows in the table
table_data = table.find_all('tr')

# Iterating through each row (excluding the header row)
for data in table_data[1:]:
    r_data = data.find_all('td')                    # Extracting each cell in the row
    row_data = [r.text.strip() for r in r_data]     # Removing whitespace and extracting text
    length = len(df)                                # Finding current length of the DataFrame
    df.loc[length] = row_data                       # Appending the row to the DataFrame

# Saving the DataFrame to a CSV file (modify the path as needed)
df.to_csv('/Users/aakk/Documents/Projects/Python/Scraping Output/List_of_largest_companies_in_the_United_States_by_revenue.csv', index=False)