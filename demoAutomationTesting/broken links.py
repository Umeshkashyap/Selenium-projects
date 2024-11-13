import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
waitTime = WebDriverWait(driver, 10)

# Open the Dolphin website
driver.get("http://www.deadlinkcity.com/")

# find numbers of link in a page

allLinks=driver.find_elements(By.XPATH,"//a")
print(len(allLinks))
brokenLinksCount=0
validLinksCount=0

# get links url and response


for link in allLinks:
    url=link.get_attribute("href")

    try:
        res=requests.head(url)
    except:
        None

    #print response status code
    # print(res.status_code)
    if res.status_code>=400:
        print(url,"is broken link")
        brokenLinksCount+=1
    else:
        print(url,"is valid link")
        validLinksCount+=1


print("Total number of broken links", brokenLinksCount)
print("Total number of valid links",validLinksCount)


