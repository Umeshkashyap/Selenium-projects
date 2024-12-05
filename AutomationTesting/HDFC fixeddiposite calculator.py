import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from DataDrivenTesting import XlUtilities

# Set ChromeOptions to handle notification popups
options = Options()
options.add_argument("--disable-notifications")  # Disable browser notifications

# Initialize the WebDriver with service object and options
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=options)

file="C:\\Users\\Admin\\Desktop\\Tutorial\\Selenium\\fdcalculator.xlsx"

rows=XlUtilities.get_row(file,"Sheet1")



#--------------------------------------------------------------------------------------------------------

# # Navigate to the target website
# driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
# driver.maximize_window()
#
# principle=driver.find_element(By.XPATH,"//input[@id='principal']")
# principle.send_keys("599999")
#
# rateofinterest=driver.find_element(By.XPATH,"//input[@id='interest']")
# rateofinterest.send_keys("77")
#
# period=driver.find_element(By.XPATH,"//input[@id='tenure']")
# period.send_keys("5")
#
# periodoptions=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
# periodoptions.select_by_visible_text("year(s)")
#
# frequency=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
# frequency.select_by_visible_text("Compounded Yearly")
#
# button=driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
# button.click()
# clearButton=driver.find_element(By.XPATH,"//img[@class='PL5']")
# clearButton.click()
#
# maturityvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']")
# print(maturityvalue.text)
#
# # Allow time for page elements to load
# time.sleep(5)
#
