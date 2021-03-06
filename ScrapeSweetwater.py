import requests
from bs4 import BeautifulSoup

# Scrape with requests
urlPluginSales = 'https://www.sweetwater.com/dealzone/?s=&sb=popular&params=eyJmYWNldCI6eyJDYXRlZ29yeSI6WyI2NzZcLzY5NlwvNzAwIl19fQ'
pagePluginSales = requests.get(urlPluginSales)

# Prepare for parsing with BeautifulSoup
soupPluginSales = BeautifulSoup(pagePluginSales.content, 'lxml')

positionDisc = soupPluginSales.find('div', class_='product-block rebate')
productName = positionDisc.find('strong', class_='product-block__title').string
#brand = positionDisc.find(class_='product_manufacturer').string
#teaser = positionDisc.find(class_='product_teaser').string
#originalPrice = positionDisc.find('span', class_='original_price').string
currentPrice = positionDisc.find('strong', class_='finalamount').string

# positionFree = soupPluginSales.find('li', class_='product-list-item enabled free')
# productNameF = positionFree.find(class_='product_title').string
# brandF = positionFree.find(class_='product_manufacturer').string
# teaserF = positionFree.find(class_='product_teaser').string

# positionCategory = soupPluginSales.find(class_='content')
# category = positionCategory.find(class_='category_title').string

print('DISCOUNTED PLUGINS')
print(productName)
# print(brand)
# print(teaser)
# print(originalPrice)
print(currentPrice)
print()
# print('FREE PLUGINS')
# print(productNameF)
# print(brandF)
# print(teaserF)
