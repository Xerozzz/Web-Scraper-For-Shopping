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
items_lazada_list, prices_lazada_list, links_lazada_list = LazadaSearch(search_item)

# Combine into one list
items_list = items_lazada_list
prices_list = prices_lazada_list
links_list = links_lazada_list

# Convert the two lists into a dataframe
dfL = pd.DataFrame(zip(items_list, prices_list, links_list), columns=['ItemName', 'Price ($)','Link'])
dfL['Price ($)'] = dfL['Price ($)'].str.replace('$', '').astype(float) # You might need to change "$" into whatever currency symbol is used based on which Lazada you access
dfL['Platform'] = 'Lazada'

# Filters (Optional)
#dfL = dfL[dfL['ItemName'].str.contains('<fill in>') == False] # This removes any entry with '<fill in>' not in its item name. You can change the value to anything you want to filter
#dfL = dfL[dfL['ItemName'].str.contains('<fill in>') == True] # Only shows items that contain "<fill in>" in their name. You can change the value to anything you want to filter

# Variables
timestamp = (datetime.now()).date()
path = "Exports" + f"/{search_item}_{timestamp}.xlsx"

# Print to Excel Sheet
dfL.to_excel(path, header = True)

# Output to confirm it worked
print(f"Scraping success! Output is stored in {path}")