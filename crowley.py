#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup

def crawlsite(url):
    source_code = requests.get(url)
    plain = source_code.text
    soup = BeautifulSoup(plain, "lxml")
    return soup
