"""
Scrapes the prices for a list of items on ebay.co.uk to get the best price
"""
from bs4 import BeautifulSoup
import requests

LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=m1+macbook+air&_sacat=0"

