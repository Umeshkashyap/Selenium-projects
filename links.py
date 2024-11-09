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

links=driver.find_elements(By.XPATH,"//a")
print(len(links))

# print all links text

for link in links:
    print(link.text)
    if

