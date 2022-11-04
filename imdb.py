import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.imdb.com/title/tt0770828/')
soup = BeautifulSoup(website.text, 'html.parser')
title = soup.select_one('.sc-80d4314-1 > h1').text
runtime = soup.select_one('.sc-8c396aa2-0').contents[2].text
plot = soup.select_one('.sc-16ede01-6').text
rating = soup.select_one('.sc-7ab21ed2-2').text
rating_count = soup.select_one('.sc-7ab21ed2-3').text
cast_list = soup.select('.sc-bfec09a1-1')
cast = ''
for item in cast_list:
    cast += item.text.strip()+', '
print(cast[:-2])
