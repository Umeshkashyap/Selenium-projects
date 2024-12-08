import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import mysql.connector

# Set ChromeOptions to handle notification popups
options = Options()
options.add_argument("--disable-notifications")  # Disable browser notifications

# Initialize the WebDriver with service object and options
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=options)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

select_query="SELECT * FROM fd_data"

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="hdfc_calculator")
curs = conn.cursor()
curs.execute(select_query)
for row in curs:
    # get data from the Database
    principle=row[0]
    ROI=row[1]
    period1=row[2]
    period2 =row[3]
    frequency=row[4]
    maturityValue =row[5]
#   provide data for input field and dropdown
    Principle = driver.find_element(By.XPATH, "//input[@id='principal']")
    Principle.send_keys(principle)
    rateofinterest = driver.find_element(By.XPATH, "//input[@id='interest']")
    rateofinterest.send_keys(ROI)
    period = driver.find_element(By.XPATH, "//input[@id='tenure']")
    period.send_keys(period1)
    periodoptions = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    periodoptions.select_by_visible_text(period2)
    frequencyOptions = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencyOptions.select_by_visible_text(frequency)
    button=driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']")
    button.click()
    RealMaturityValue = driver.find_element(By.XPATH, "//span[@id='resp_matval']").text


# Checking Expected and actual maturity value
    if float(maturityValue)==float(RealMaturityValue):
        print("Test passed")
    else:
        print("Test failed")

    clearButton = driver.find_element(By.XPATH, "//img[@class='PL5']")
    clearButton.click()
time.sleep(2)



