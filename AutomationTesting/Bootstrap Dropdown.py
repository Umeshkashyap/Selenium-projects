from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
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
print("tests")
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
print("print")
country_name=driver.find_elements(By.XPATH,"//ul[@class='select2-results__options']//li")
print(len(country_name))

for country in country_name:
    if country.text=="India":
        country.click()
        break
time.sleep(5)
driver.quit()