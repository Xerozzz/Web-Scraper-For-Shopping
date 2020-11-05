# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd


def LazadaSearch(search_item):
    # Intializing global variables
    webdriver_path = "chromedriver.exe" 
    Lazada_url = 'https://www.lazada.sg/' # Your lazada website URL (Singapore one is used here)

    # Select custom Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless') # Run script with browser in background
    options.add_argument('start-maximized')  
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')

    # Open the Chrome browser
    browser = webdriver.Chrome(webdriver_path, options=options)
    browser.get(Lazada_url)

    # Search Bar
    search_bar = browser.find_element_by_id('q')
    search_bar.send_keys(search_item)
    search_bar.submit()
    item_items = browser.find_elements_by_class_name('c16H9d')
    item_prices = browser.find_elements_by_class_name('c13VH6')

    # Initialize empty lists
    items_list = []
    prices_list = []
    links_list = []

    # Loop over the item_items and item_prices
    for item in item_items:
        items_list.append(item.text)
        links_list.append(item.find_element_by_xpath('a').get_attribute("href"))
    for price in item_prices:
        prices_list.append(price.text)

    return items_list,prices_list,links_list