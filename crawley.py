#!/usr/bin/env python3.5
import requests
from bs4 import BeautifulSoup
"""Works with 100% Hardcore!"""


#url = str(input("URL: "))

def menus():
    url = 'http://100procenthardcore.nl/'
    try:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.find_all('ul', {'class': 'children'}):
            for a in link.find_all('a'):
                link = a.get('href')
                crawl(link)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")


def crawl(url):
    try:
        page = 1
        item = 0
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class': 'product-title-link'}):
            href = link.get('href')
            title = link.string
            print(title)
            print(href)
            for test in soup.findAll('div', {'class': 'product_infos'}):
                
                #print(price.text.strip())
                print(reduced)
            price = soup.findAll('span', {'class': 'woocommerce-Price-amount'})
            print(price[item].text.strip())
            item += 1
        item = 0
    except KeyboardInterrupt:
        print('interrupted....')


menus()
#crawl(1)
