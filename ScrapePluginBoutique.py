import requests
from bs4 import BeautifulSoup

# Scrape with requests
# urlPluginSales = 'http://www.pluginboutique.com/deals/index?s=position_asc'
# pagePluginSales = requests.get(urlPluginSales)

urlPluginFree = 'http://www.pluginboutique.com/categories/2-Effects?free=true'
pagePluginFree = requests.get(urlPluginFree)

# Prepare for parsing with BeautifulSoup
# soupPluginSales = BeautifulSoup(pagePluginSales.content, 'lxml')
soupPluginFree = BeautifulSoup(pagePluginFree).content, 'lxml')

# positionDisc = soupPluginSales.find('div', class_='deal')
# productName = positionDisc.find(class_='deal-title').string
# brand = positionDisc.find(class_='product_manufacturer').string
# teaser = positionDisc.find('div', class_='deal-about').string
#category = positionDisc.find(class_='category_title')
#originalPrice = positionDisc.find('dd', class_='buybox-item .4.1').string
#currentPrice = positionDisc.find('span', class_='current_pric').string

positionFree = soupPluginFree.find('li', class_='product-list-item enabled free')
productNameF = positionFree.find("h3", class_='producttitle-title').string
# brandF = positionFree.find(class_='product_manufacturer').string
# teaserF = positionFree.find(class_='product_teaser').string
# categoryF = positionFree.find(class_='category_title')

# positionCategory = soupPluginSales.find(class_='content')
# category = positionCategory.find(class_='category_title').string

print()
# print(category)
# print()
# print('DISCOUNTED PLUGINS')
# print(productName)
# print(brand)
# print(teaser)
# print(originalPrice)
# print(currentPrice)
# print()
print('FREE PLUGINS')
print(productNameF)
print(brandF)
print(teaserF)
