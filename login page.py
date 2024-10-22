from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:/drivers/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open the OrangeHRM website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Wait until the username input field is present
userName = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))
)
userName.send_keys("Admin")

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
)

# Enter the password "Admin"
password.send_keys("admin123")

login= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
)


login.click()


# Optional: wait for 5 seconds to observe the browser interaction
WebDriverWait(driver, 5)

time.sleep(10)

# Close the browser
driver.quit()
