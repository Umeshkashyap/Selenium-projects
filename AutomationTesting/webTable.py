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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

tableRow=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(tableRow)
tableColumn=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(tableColumn)

# 1. select and print specific data

# tableRow=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr[5]/td[1]")
# print(tableRow.text)

#2. print all the data of the table

for r in range(2,tableRow+1):
    print("test r")
    for c in range(1,tableColumn+1):
        print("test c")
        data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print("test data")
        print(data)
