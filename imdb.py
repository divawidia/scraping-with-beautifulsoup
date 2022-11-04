import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.titleColumn a')
csv_data = [['title', 'movie_length', 'plot',
             'rating', 'rating_count', 'cast']]
for link in links:
    website = requests.get('https://www.imdb.com'+link.attrs['href'])
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
    # print(cast[:-2])
    csv_data.append([title, runtime, plot, rating, rating_count, cast[:-2]])

with open('top250_imdb_movie.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
