#!/usr/bin/env python3
import requests
import re
import sys
from bs4 import BeautifulSoup
"""Works with 100% Hardcore!"""


#url = str(input("URL: "))
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def menus():
    url = 'http://100procenthardcore.nl/'
    try:
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        categorys = []
        categorytitle = []
        #for link in soup.find_all('ul', {'class': 'children'}):
        for link in soup.find_all('ul', {'class': 'product-categories'}):
            category = soup.find_all('a')
            for a in link.find_all('a'):
                link = a.get('href')
                title = a.string
                categorys.append(link)
                categorytitle.append(title)
        i = 0
        for title in categorytitle:
            print("["+ str(i) +"] " + bcolors.OKGREEN + title + bcolors.ENDC)
            i += 1
        choise = int(input(">> "))
        crawl(categorys[choise])

    except KeyboardInterrupt:
        sys.exit("EXIT")

def crawl(url):
    try:
        page = 1
        item = 0
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('a', {'class': 'product-title-link'}):
            itemlist = []
            href = link.get('href')
            title = link.string
            print(bcolors.WARNING + "[+] " + title + bcolors.ENDC)
            print(bcolors.OKGREEN + "[+] " + href +  bcolors.ENDC)
            itemlist.append(title)
            product_info(href)
            item += 1
        item = 0
        menus()
    except KeyboardInterrupt:
        print('interrupted....')
        sys.exit("EXIT")

def product_info(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "lxml")
    for price in soup.findAll('div', {'class': 'product_infos'}):
        price = soup.find_all('meta', attrs={"itemprop":"price"})
    for value in price:
        a = re.findall(r"[-+]?\d*\.\d+|\d+", str(value))
        print(bcolors.FAIL + "[+] " + ''.join(map(str, a)) + "€" + bcolors.ENDC)
        #print(value.text.strip())
        #print(price.text.strip())
        #print(reduced)
        #price = soup.findAll('span', {'class': 'woocommerce-Price-amount'})
        #print(price[item].text.strip())

menus()
#crawl(1)
