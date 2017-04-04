from selenium import webdriver
import datetime

today = str(datetime.datetime.now().date())


sites = {
         'Trulia': 'https://www.trulia.com/TN/Nashville/',
    'Accelerators' : 'http://seed-db.com/accelerators',
    'Sweetwater' : 'https://tradingpost.sweetwater.com/call/TP_Date/desc/1',
    'Reverb' : 'https://reverb.com/marketplace?query=&condition=used&page=1',
    'GameStats' : 'https://na.op.gg/statistics/champion/'
         }

browser = webdriver.Chrome("/Users/apple/anaconda/bin/chromedriver")

for name, link in sites.items():
    response = browser.get(link)
    html = browser.page_source

    fileName = today + '.' + name + 'Selenium.html'
    outfile = open(fileName, 'w')
    outfile.write(html)
    outfile.close()

browser.quit()