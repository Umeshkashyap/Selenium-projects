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
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

# excell file path
file="C:\\Users\\Admin\\Desktop\\Tutorial\\Selenium\\fd.xlsx"

# get excel Rows
rows=XlUtilities.get_row(file,"Sheet1")
for r in range(2,rows+1):

    # get data from the excell
    principle=XlUtilities.read_data(file,"Sheet1",r,1)
    print(principle)
    ROI=XlUtilities.read_data(file,"Sheet1",r,2)
    print(ROI)
    period1=XlUtilities.read_data(file,"Sheet1",r,3)
    print(period1)
    period2 = XlUtilities.read_data(file, "Sheet1", r, 4)
    print(period2)
    frequency=XlUtilities.read_data(file, "Sheet1", r, 5)
    print(frequency)
    maturityValue = XlUtilities.read_data(file, "Sheet1", r, 6)
    print(maturityValue)


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
    print(RealMaturityValue)
    clearButton = driver.find_element(By.XPATH, "//img[@class='PL5']")
    clearButton.click()

# Checking Expected and actual maturity value
    if float(maturityValue)==float(RealMaturityValue):
        print("test paased")
        XlUtilities.write_Data(file,"Sheet1",r,8,"Passed")
        XlUtilities.fill_green(file,"Sheet1",r,8)
    else:
        print("test failed")
        XlUtilities.write_Data(file,"Sheet1",r,8,"Failed")
        XlUtilities.fill_red(file,"Sheet1",r,8)

    clearButton = driver.find_element(By.XPATH, "//img[@class='PL5']")
    clearButton.click()
    time.sleep(2)



