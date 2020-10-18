import os
# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Intializing global variables
webdriver_path = r"C:\Users\yiter\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver.exe" # Enter the file directory of the Chromedriver
Lazada_url = 'https://www.lazada.sg/' # Your lazada website URL
search_item = 'Nescafe Gold refill 170g' # Item to search

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

item_titles = browser.find_elements_by_class_name('c16H9d')
item_prices = browser.find_elements_by_class_name('c13VH6')

# Initialize empty lists
titles_list = []
prices_list = []

# Loop over the item_titles and item_prices
for title in item_titles:
    titles_list.append(title.text)
for price in item_prices:
    prices_list.append(price.text)

# Check if next page option is disabled
try:
    browser.find_element_by_xpath('//*[@class=”ant-pagination-next” and not(@aria-disabled)]').click()
except NoSuchElementException: 
    browser.quit()

# Convert the two lists into a dataframe
dfL = pd.DataFrame(zip(titles_list, prices_list), columns=['ItemName', 'Price'])
dfL['Price'] = dfL['Price'].str.replace('$', '').astype(float)
dfL['Platform'] = 'Lazada'

# Filters
#dfL = dfL[dfL['ItemName'].str.contains('x2') == False] # This removes any entry with 'x2' in its title
#dfL = dfL[dfL['ItemName'].str.contains('170g') == True]

print(dfL)