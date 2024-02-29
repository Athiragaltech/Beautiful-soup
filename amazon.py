import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
driver = webdriver.Chrome()
url = 'https://flipkart.com'
# We;ll use the get method of driver and pass in the URL
driver.get(url)
def get_url(search_item):
    '''
    This function fetches the URL of the item that you want to search
    '''
    template = 'https://www.flipkart.com/search?q={}&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones&requestId=e625b409-ca2a-456a-b53c-0fdb7618b658&as-backfill=on'
    # We'are replacing every space with '+' to adhere with the pattern 
    search_item = search_item.replace(" ","+")
    return template.format(search_item)
# Checking whether the function is working properly or not
url = get_url('mobile phones')
print(url)
https://www.flipkart.com/search?q=mobile+phones&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobile+phones&requestId=e625b409-ca2a-456a-b
# Creating a soup object using driver.page_source to retreive the HTML text and then we'll use the default html parser to parse
# the HTML.
soup = BeautifulSoup(driver.page_source, 'html.parser')
