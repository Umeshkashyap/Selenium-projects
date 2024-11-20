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
tableColumn=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(tableColumn)

# 1. select and print specific data

# tableRow=driver.find_element(By.XPATH,"//table[@name='BookTable']//tbody/tr[5]/td[1]")
# print(tableRow.text)

#2. print all the data of the table

# for r in range(2,tableRow+1):
#     for c in range(1,tableColumn+1):
#         data=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="\t")  #print data in a same row
#     print()  #print data in next line after 1 loop is complete

#3. print selected data based on the condition

for r in range(2,tableRow+1):
    bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
    print("test book")
    if bookname=="Master In Selenium":
        print("test if")
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,price)
        break
driver.quit()
