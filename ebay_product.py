import requests
import csv
from bs4 import BeautifulSoup

query = input('Enter product name: ')
free_shipping = input('Enter free shipping (y/n): ')
for i in range(1, 5):
    website = requests.get(
        'https://www.ebay.com/sch/i.html?_from=R40&_nkw=' + query + '&_sacat=0&_pgn=' + str(i)).text
    soup = BeautifulSoup(website, 'html.parser')
    items = soup.select('.s-item__info')
    for item in items:
        title = item.select_one('.s-item__title').text
        price = item.select_one('.s-item__price').text
        try:
            shipping = item.select_one('.s-item__shipping').text
        except AttributeError as error:
            shipping = None
        if free_shipping == 'y':
            if 'Free' in shipping:
                print(f'{title}\n{price}\n{shipping}')
        else:
            print(f'{title}\n{price}\n{shipping}')
