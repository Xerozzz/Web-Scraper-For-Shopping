# Import scripts
from lazada import LazadaSearch
from shopee import ShopeeSearch
# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Other Libraries
from datetime import datetime

# Item to search
search_item = input('Item to search: ') 

# Lazada Search
lazadaPD = LazadaSearch(search_item)

# Shopee Search
shopeePD = ShopeeSearch(search_item)

# Combine the Pandaframes
totalPD = pd.concat([shopeePD,lazadaPD])

# Variables
timestamp = (datetime.now()).date()
path = "Exports" + f"/{search_item}_{timestamp}.xlsx"

# Print to Excel Sheet
totalPD.to_excel(path, header = True)

# Output to confirm it worked
print(f"Scraping success! Output is stored in {path}")