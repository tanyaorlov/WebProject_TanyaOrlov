import requests
import datetime
from bs4 import BeautifulSoup
import json

# Create list of dicts for JSON Object
response = []

# First page to be parsed with BeautifulSoup
url = 'https://www.youtube.com/results?sp=CAMSAggF&q=music+video'

parse = True
i = 1

# Parse YouTube url
while parse == True:
# while i < 3:
    pages = requests.get(url)
    soup = BeautifulSoup(pages.content, 'lxml')

#   parse each page
    for position in soup.find_all('div', class_='yt-lockup-content'):
        title = position.find('a').string

        # Make changes to response
        response.append({'Title': title})

    #print(url)
    parse = False
    for nextPosition in soup.find_all('span', class_='yt-uix-button-content'):
        if nextPosition.string == 'Next »':
            url = 'https://www.youtube.com/' + nextPosition.parent.get('href')
            parse = True
            i += 1
            #print(i)



# Write response to JSON file
today = str(datetime.datetime.now().date())
postingsFile = today + '.YouTube.json'

with open(postingsFile, 'w') as outfile:
    json.dump(response, outfile, sort_keys=True, indent=2)

outfile.close()