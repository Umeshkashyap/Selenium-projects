from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


print("")
# Setup Chrome WebDriver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Create an explicit wait with a timeout of 10 seconds
mywait = WebDriverWait(driver, 10)

# Open the demo website
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

'''
# Handle Alert with OK button
#---------------------------------------------------------
# Uncomment this section if testing "Alert with OK"
# clickBtn = driver.find_element(By.XPATH, "//a[normalize-space()='Alert with OK']")
clickBtn = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Alert with OK']")))
clickBtn.click()

# Trigger the alert
openPopUp = driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display an')]")
openPopUp.click()

time.sleep(5)  # Static wait (can be replaced with explicit waits)
alertWindow = driver.switch_to.alert
alertWindow.accept()  # Accepts the alert
'''

# Handle Alert with OK and Cancel button
#-----------------------------------------
"""
# Uncomment this section if testing "Alert with OK & Cancel"
alertWithOkAndCancel = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Alert with OK & Cancel']")))
alertWithOkAndCancel.click()

# Trigger the confirmation alert
openPopUp = driver.find_element(By.XPATH, "//button[normalize-space()='click the button to display a confirm box']")
openPopUp.click()

time.sleep(5)  # Static wait (can be avoided with explicit wait)
alertWindow = driver.switch_to.alert
print(alertWindow.text)  # Print the alert text
#alertWindow.accept()  # Uncomment to accept the alert
alertWindow.dismiss()  # Dismiss the alert
"""

# Handle Alert with Input Box
#-----------------------------------------
alertWithInput = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Alert with Textbox']")))
alertWithInput.click()

# Trigger the prompt alert
openPopUp = driver.find_element(By.XPATH, "//button[normalize-space()='click the button to demonstrate the prompt box']")
openPopUp.click()

time.sleep(2)  # Static wait (consider replacing with explicit wait)
alertWindow = driver.switch_to.alert

# Print and interact with the alert box
print(f"Alert text: {alertWindow.text}")
alertWindow.send_keys("")  # Clear any default input
alertWindow.send_keys("Umesh Kashyap")  # Provide input
alertWindow.accept()  # Click on OK button
#alertWindow.dismiss()  # Uncomment to click on Cancel button

# Validate input in the webpage
txt = driver.find_element(By.XPATH, "//p[@id='demo1']").text
print(txt)  # Print the result text

time.sleep(5)  # Wait to observe changes before quitting (optional)

