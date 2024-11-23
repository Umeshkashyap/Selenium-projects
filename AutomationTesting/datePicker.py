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

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# date picker inside the frame
driver.switch_to.frame(0)
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

Month="January"
Year="2026"
Date="18"

# capturing month and year
while True:
    month=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    year=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if month==Month and year==Year:
        print(month,year)
        break
    else:
        nextArrow=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() #using for next arrow clicked

        # using when select on previous dates
        #previuosArrow=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click

# select a date from calender
date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr//td//a")
for d in date:
    if d.text==Date:
        print("date",d.text)
        d.click()
        break

