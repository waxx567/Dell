from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime

# link to scrape
LINK = "https://www.bikekings.co.za/collections/fullface/products/shark-skwal-i3-hellcat-matte-kur?_pos=28&_fid=271f4b3e9&_ss=c"


def get_data(link):
    # get data
    response = requests.get(link)
    # parse data    
    soup = BeautifulSoup(response.text, "html.parser")
    # get price
    price = soup.find("div",{"class":"product-page-info__price"}).find_all("span",{"class":"price"})
    print(price)
    return price

def main():
    get_data(LINK)


if __name__ == "__main__":
    main()