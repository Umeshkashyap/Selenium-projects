from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
import os

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver, 10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

cookies=driver.get_cookies()
print(len(cookies))

for cookie in cookies:
    print("Name: ",cookie.get("name"),"Value:",cookie.get("value"))


driver.add_cookie({"name":"mycookies","value":"dhhhdhdhdhggg"})
cook=driver.get_cookies()
print(len(cook))


driver.delete_cookie("mycookies")