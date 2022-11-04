import requests
from bs4 import BeautifulSoup
import csv

web = requests.get(
    'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(web.text, 'html.parser')
first_table = soup.select_one('.wikitable')
table_rows = first_table.select('tr')[3:]
csv_data = [['rank', 'name', 'population', 'percentage', 'date', 'source']]

for row in table_rows:
    rank = row.find('th').text.strip()
    table_data = row.select('td')
    name = table_data[0].find('a').text
    population = table_data[1].text
    percentage = table_data[2].text.strip()
    date = table_data[3].text.strip()
    source = table_data[4].text.strip().split('[')[0]
    csv_data.append([rank, name, population, percentage, date, source])

# print(csv_data)

with open('countries_poppulation.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
