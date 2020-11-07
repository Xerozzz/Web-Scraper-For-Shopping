# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Others
import requests

def ShopeeSearch(search_item):
    # Intializing global variables
    Shopee_url = 'https://shopee.sg/' # Your Shopee website URL (Singapore one is used here)
    headers = {
        'User-Agent': 'Chrome',
        'Referer': '{}search?keyword={}'.format(Shopee_url, search_item)
    }

    # Configure the url to request
    url = 'https://shopee.sg/api/v2/search_items/?by=relevancy&keyword={}&limit=100&newest=0&order=desc&page_type=search'.format(search_item)

    # Shopee API request
    r = requests.get(url, headers = headers).json()

    # Shopee scraping script
    titles_list = []
    prices_list = []
    links_list = []
    for item in r['items']:
        # print(item)
        # break
        titles_list.append(item['name'])
        prices_list.append(item['price_min'])
        string = f"{item['name']}-i.{item['shopid']}.{item['itemid']}"
        links_list.append(string)
    
    # Create the pandaframe
    shopeePD = pd.DataFrame(zip(titles_list, prices_list,links_list), columns=['ItemName', 'Price ($)','Link'])
    shopeePD['Platform'] = 'Shopee'

    # Change column type to float
    shopeePD['Price ($)'] = shopeePD['Price ($)'] / 100000
    
    # Return Lists
    return shopeePD