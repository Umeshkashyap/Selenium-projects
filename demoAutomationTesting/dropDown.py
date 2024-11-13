import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj=Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
waitTime=WebDriverWait(driver,10)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# dropDown=(driver.find_element(By.XPATH,"//select[@id='input-country']"))
# Need to import Select class
dropDown=Select(driver.find_element(By.XPATH,"//select[@id='Skills']"))

# select options from the dropDown using inbuit functions

# #dropDown.select_by_visible_text("CSS")
# #dropDown.select_by_index(9)
# dropDown.select_by_value("Spreadsheet")


#capture all dropDown option using select inbuit function

#allOptions=dropDown.options
# print(len(allOptions))
#
# for opt in allOptions:
#     print(opt.text)

#select option
#
# for opt in allOptions:
#     print(opt.text)
#     if opt.text=="Microsoft Outlook":
#         opt.click()
#         break
# time.sleep(120)


# Capture and select Dropdown options without using inbuilt functions using select id

allOPt=driver.find_elements(By.XPATH,"//select[@id='Skills']/option")
print(len(allOPt))

for opt in allOPt:
    print(opt.text)
    if opt.text=="Windows":
        opt.click()
        break

time.sleep(10)