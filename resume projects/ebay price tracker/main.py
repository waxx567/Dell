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
    """
    Given a link to an ebay.co.uk search page, this function will scrape the prices of all
        items on the page and return them as a list of floats.
    """
    # get data
    response = requests.get(link)
    # parse data
    soup = BeautifulSoup(response.text, "html.parser")
    # get list of items
    list_items = soup.find("ul", {"class": "srp-results"}).find_all("li", {"class": "s-item"})

    # empty list to store prices
    prices = []

    # get prices and append them to the list of prices
    for item in list_items:
        text_price = item.find("span", {"class": "s-item__price"}).text
        # if prices are within a range, skip
        if "to" in text_price:
            continue
        # remove commas and convert price to float
        price = float(text_price[1:].replace(",", "")) 
        prices.append(price)

    return prices

def remove_outliers(prices, m=2):
    # remove outliers
    """
    Removes outliers from a list of prices by removing all values that are more than m standard
        deviations away from the mean.
    """
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def main():
    # get data
    prices = get_data(LINK)
    # remove outliers
    prices = remove_outliers(prices)
    # get best price
    best_price = np.min(prices)
    # print best price
    print(f"Best price: £{best_price:.2f}")

if __name__ == "__main__":    
    main()