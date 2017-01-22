#!/usr/bin/env python3.5
import requests
import crowley
import re
"""Pr0l0ader """
BASE = 'https://pr0gramm.com'
URL = 'https://pr0gramm.com/static/top/'
PATH = 'test/'
def fetch():
    soup = crowley.crawlsite(URL)
    for link in soup.find_all('a', href=re.compile('\/static\/\d{1,8}')):
        test = re.findall('\/static\/\d{1,8}', str(link))
        url = BASE+''.join(test)
        getlink(url)

def getlink(url):
    soup = crowley.crawlsite(url)
    for link in soup.find_all('video'):
        download(link["src"])

def download(url):
    url = 'https:' + url
    r = requests.get(url)
    name = re.findall('[a-z0-9]+\.mp4', url)
    filename = PATH + ''.join(name)
    print(filename)
    with open(filename, "wb") as code:
        code.write(r.content)
    print('[+] Finished ' + str(name))
fetch()
