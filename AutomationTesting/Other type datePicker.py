from selenium import webdriver
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

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='departon']").click()

# select year and month by visible text
year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year.select_by_visible_text("2025")

month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
month.select_by_visible_text("Jan")

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table//tbody//tr//td//a")
for date in dates:
    if date.text=="18":
        date.click()
        break

time.sleep(5)