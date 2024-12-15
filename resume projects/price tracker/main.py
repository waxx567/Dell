from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.temu.com/za/-two-in-one-smartwatch-with-1-53ips-screen-answer-make-calls-suitable-for-men-and-women-fitness-sleep-pedometer-ip67-waterproof-compatible-with-iphone--g-601099641600577.html?_oak_mp_inf=EMH08tSm1ogBGiA1Y2QwY2VmNGI5Mzc0M2Q2OWRhNjY4ZjU4NDUwMTk5YyDEkOnHvDI%3D&top_gallery_url=https%3A%2F%2Fimg.kwcdn.com%2Fproduct%2Ffancy%2F3e7320b8-31f6-45b6-8ebe-8d0864d5fd96.jpg&spec_gallery_id=601099641600577&refer_page_sn=10009&refer_source=0&freesia_scene=2&_oak_freesia_scene=2&_oak_rec_ext_1=NjY2MDA&_oak_gallery_order=177211680%2C872976172%2C2061801009%2C1134693099%2C2114278436&search_key=iphone&refer_page_el_sn=200049&_x_ns_irclickid=THeXSSTOIxyKWWvUfLynl3slUkCXm2zf5QN%3Axg0&_x_ads_account=18350&_x_ads_id=1580294&_x_ns_iradname=Online%20Tracking%20Link&_x_ns_iradsize=&_x_ns_prodsku=&_x_ns_irmptype=mediapartner&_x_ns_sharedid=8114875&_x_ns_ts=1734243645283&_x_ns_randint=7611655&_x_ns_adtype=ONLINE_TRACKING_LINK&_x_ns_irmpgroupname=%22mz%22&_x_ads_channel=impact&_x_ns_mp_value2=&_x_ns_mp_value3=&_x_ns_irmpname=Connexity%20US&_x_ns_irpid=150372&_x_sessn_id=vdk7kfv8vh&refer_page_name=search_result&refer_page_id=10009_1734243667751_2tih2m965m&no_cache_id=an9h


def get_data(link):
    # get data
    response = requests.get(link)
    # parse data
    soup = BeautifulSoup(response.text, "html.parser")
    # get price
    price = soup.find("div", class_="price").text.strip()
    # get title
    title = soup.find("h1", class_="product__title").text.strip()