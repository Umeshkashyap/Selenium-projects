from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver, 10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

minSlider=driver.find_element(By.XPATH,"//div[@id='HTML7']//span[1]")
maxSlider=driver.find_element(By.XPATH,"//div[@id='HTML7']//span[2]")
print(minSlider.location)
print(maxSlider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(minSlider,60,0).perform()
act.drag_and_drop_by_offset(maxSlider,-50,0).perform()

print(minSlider.location)
print(maxSlider.location)

time.sleep(5)