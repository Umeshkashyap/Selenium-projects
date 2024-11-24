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

# scrolldown page by pixel

# driver.execute_script("window.scrollBy(0,2000)","")
# print("passed")
# value=driver.execute_script("return window.pageYOffset;")
# print("Scroller postion:",value)
#
# # scrolldown page till the element is visible
# heading=driver.find_element(By.XPATH,"//h2[normalize-space()='Dynamic Web Table']")
# driver.execute_script("arguments[0].scrollIntoView();",heading)
# value=driver.execute_script("return window.pageYOffset;")
# print("Scroller postion:",value)
#

# scrolldown page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Scroller postion:",value)

# scrolldown upto starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Scroller postion:",value)


time.sleep(10)