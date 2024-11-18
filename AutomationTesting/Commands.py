from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Set up Chrome driver
serv_obj = Service("C:/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open the OrangeHRM website
driver.get("https://www.facebook.com/")

