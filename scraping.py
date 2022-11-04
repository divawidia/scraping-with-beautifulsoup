import requests
from bs4 import BeautifulSoup

page = 1
next_button = True
while next_button:
    r = requests.get('https://quotes.toscrape.com/page/' + str(page))
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('title')
    next_button = soup.select_one('.next > a')

    #link = soup.find('a')
    # quotes = soup.find_all(class_='text')
    # links = soup.find_all('a')
    # login_link = soup.find(href='/login')
    # print(login_link)
    # for quote in quotes:
    #     print(quote.text)

    # quote = soup.find(class_='quote')
    # quote_text = quote.find(class_='text')
    # quote_author = quote.find(class_='author')
    # print(quote_text.text)
    # print(quote_author.text)

    quotes = soup.select('.quote')
    for quote in quotes:
        text = quote.select_one('.text')
        author = quote.select_one('.author')
        tags = quote.select('.tags')
        print(text.text)
        print(author.text)
        for tag in tags:
            print(tag.text)
    print('scrapped page' + str(page))
    page += 1
