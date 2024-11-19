from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver,15)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)

# getting only single window id

#windowId = driver.current_window_handle
#print(windowId)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

# Approach1 to getting multiple window id at a time

windowsID = driver.window_handles   # to getting multiple window id

# parentWindow = windowsID[0]
# childWindow = windowsID[1]
#
# driver.switch_to.window(parentWindow)
# print(driver.title,"Parent window id:", parentWindow)
#
# driver.switch_to.window(childWindow)
# print(driver.title,"Child window id", childWindow)


# Approach2

for winID in windowsID:
    driver.switch_to.window(winID)
    print(driver.title)


#Approach3

for winId in windowsID:
    driver.switch_to.window(winId)
    if driver.title=="Human Resources Management Software | OrangeHRM":
        # clicked on a button
        driver.find_element(By.XPATH,"//div[@class='d-flex web-menu-btn']//li[1]//a[1]").click()
        driver.close()

driver.quit()









