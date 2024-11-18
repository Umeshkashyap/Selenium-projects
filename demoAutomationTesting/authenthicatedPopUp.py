from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
serv_obj=Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#driver.get("https://the-internet.herokuapp.com/basic_auth") #instead of using this

# Bypassing the authentication PopUp
#--------------------------------------
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")  #by pass the authenticated popup by injecting detail in url
driver.maximize_window()
time.sleep(5)
