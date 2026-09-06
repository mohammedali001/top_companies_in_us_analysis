import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36',
          'accept': 'application/json; charset=utf-8; profile="https://www.mediawiki.org/wiki/Specs/Summary/1.2.0"',
          'accept-encoding': 'gzip, deflate, br, zstd',
          'accept-language': 'en-US,en;q=0.9'
          }

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')


columns = table.find_all('th')
# print(columns)

columns_titles =[title.text.strip() for title in columns]
# print(columns_titles)

df = pd.DataFrame(columns=columns_titles)


columns_data = table.find_all('tr')

for row in columns_data:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    if len(row_data) == len(columns_titles):
        df.loc[len(df)] = row_data

df.to_csv('largest_companies.csv', index=False)