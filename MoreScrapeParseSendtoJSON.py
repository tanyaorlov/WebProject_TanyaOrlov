import requests
import datetime
from bs4 import BeautifulSoup
import json


# Create list of dicts for JSON Object
response = []

# Prepare for parsing with BeautifulSoup
url = 'https://tradingpost.sweetwater.com/call/TP_Date/desc/1'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'lxml')

# Parse url
for position in soup.find_all('td', class_='item'):
    if (position.find('a').next_sibling and position.find('a').next_sibling.find('strong') != -1):
        description = position.find('a').next_sibling.find('strong').string
        print(description)

    # Make changes to response
    response.append({'Description': description})

# Write response to JSON file
today = str(datetime.datetime.now().date())
postingsFile = today + '.Sweetwater.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()