import requests
import datetime

today = str(datetime.datetime.now().date())

sites = {
         'Trulia': 'https://www.trulia.com/TN/Nashville/',
    'Accelerators' : 'http://seed-db.com/accelerators',
    'Sweetwater' : 'https://tradingpost.sweetwater.com/call/TP_Date/desc/1',
    'SweetwaterPlugins' : 'https://www.sweetwater.com/dealzone/?s=&sb=popular&params=eyJmYWNldCI6eyJDYXRlZ29yeSI6WyI2NzZcLzY5NlwvNzAwIl19fQ',
    'Reverb' : 'https://reverb.com/marketplace?query=&condition=used&page=1',
    'GameStats' : 'https://na.op.gg/statistics/champion/'

         }

for name, link in sites.items():
    response = requests.get(link)
    html = response.content

    fileName = today + '.' + name + '.html'
    outfile = open(fileName, "wb")
    outfile.write(html)
    outfile.close()