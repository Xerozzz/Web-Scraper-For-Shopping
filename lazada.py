# Import OS for environment variables
import os
# Web Scraping
from selenium import webdriver
from selenium.common.exceptions import *
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

webdriver_path = os.getenv("chromedriver") # Enter the file directory of the Chromedriver
Lazada_url = 'https://www.lazada.com.my'
search_item = 'Nescafe Gold refill 170g' # Chose this because I often search for coffee!\

print(webdriver_path)