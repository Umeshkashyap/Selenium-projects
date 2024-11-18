from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver, 10)

# Navigate to the URL
driver.get("https://demo.automationtesting.in/Frames.html")

# Switch to outer frame
outterFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outterFrame)
print("Outer frame switched")

# Switch to inner frame
innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)
print("Inner frame switched")

# Wait for the input box and interact
inpBox = myWait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div/input")))
inpBox.click()
print("Clicked input box")
inpBox.send_keys("Test iframe successfully")
print("Data inserted")

# Exit browser
driver.quit()
