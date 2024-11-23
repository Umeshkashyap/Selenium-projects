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

button=driver.find_element(By.XPATH,"//button[normalize-space()='Point Me']")
firstEle=driver.find_element(By.XPATH,"(//a[normalize-space()='Mobiles'])[1]")
secondEle=driver.find_element(By.XPATH,"(//a[normalize-space()='Laptops'])[1]")
act=ActionChains(driver)
act.move_to_element(button).move_to_element(firstEle).move_to_element(secondEle).click().perform()
print("Hover succes")

driver.quit()