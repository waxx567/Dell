"""
Scrapes the prices for a list of items on ebay.co.uk to get the best price
"""
from bs4 import BeautifulSoup
import requests
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.ebay.co.uk/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=m1+macbook+air&_sacat=0"


def get_data(link):
    # get data
    response = requests.get(link)
    # parse data
    soup = BeautifulSoup(response.text, "html.parser")
    list_items = soup.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

    prices = []

    for item in list_items:
        text_price = item.find("span", {"class": "s-item__price"}).text
        if "to" in text_price:
            continue
        price = float(text_price[1:].replace(",", "")) 
        prices.append(price)

    return prices

if __name__ == "__main__":
    prices = get_data(LINK)
    print(f"Average price: {np.mean(prices):.2f}")