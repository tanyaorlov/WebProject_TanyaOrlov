import requests
import datetime
from bs4 import BeautifulSoup
import json
import csv

today = str(datetime.datetime.now().date())

# Create a list of dictionaries for JSON Object
response = []

# Scrape with requests
urlPluginSales = 'https://www.plugin-alliance.com/en/products.html?sort=manufacturerAZ'
pagePluginSales = requests.get(urlPluginSales)

# Prepare for parsing with BeautifulSoup
soupPluginSales = BeautifulSoup(pagePluginSales.content, 'lxml')

# Parse url
# 'position' marks the beginning of each news brief in the html
# All other data is found in its relationship to 'position'
for position in soupPluginSales.find_all('li', class_='product-list-item enabled discounted'):
    productName = position.find(class_='product_title').string
    brand = position.find(class_='product_manufacturer').string
    teaser = position.find(class_='product_teaser').string
    # category = position.find(class_='category_title')
    originalPrice = position.find('span', class_='original_price').string
    currentPrice = position.find('span', class_='current_price').string

    # Make changes to response for APNewsBriefs
    response.append({'Product Name': productName, 'Brand': brand, 'Teaser': teaser, 'Original Price': originalPrice,
                    'Current Price': currentPrice})

# Write response to JSON file
postingsFile = '/Users/apple/PycharmProjects/WebProject_TanyaOrlov/' + today + '.PluginAllianceSales.json'

#Write response to JSON file in another location
#postingsFile = '/APBriefs/' + today + '.APNewsBriefs.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()