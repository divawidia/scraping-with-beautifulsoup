import requests
from bs4 import BeautifulSoup
import csv

website = requests.get(
    'https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text, 'html.parser')
links = soup.select('.topic-list .md-crosslink')
for link in links[:8]:
    try:
        web = requests.get(
            link.attrs['href'])
        soup = BeautifulSoup(web.text, 'html.parser')
        name = soup.select_one('h1').text
        description = soup.select_one('.topic-identifier').text
        summary = soup.select_one('.topic-paragraph').text
        try:
            image = soup.select_one('.card img').attrs['src']
        except AttributeError as error:
            image = None
        birth = soup.select_one(
            '.js-fact').get_text(separator=',').split(',')[4:6]
        birth_date = birth[0]+","+birth[1]
        died = soup.find_all(
            'dd', class_='d-inline')[1].text.strip().split(',')[0:2]
        died_date = died[0]+","+died[1]
        try:
            subject_of_study = soup.find_all(
                'dd', class_='d-inline')[3].text.strip()
        except AttributeError as error:
            subject_of_study = None
        print(
            f'{name}\n{description}\n{image}\n{summary}\n{birth_date}\n{died_date}\n{subject_of_study}')
    except:
        print('something went wrong')
