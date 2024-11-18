from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\drivers\chromedriver-win64 (2)\chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)

# Open the OrangeHRM website
driver.get("http://192.168.1.150/dolphin/public/")
# Wait until the username input field is present

username="admin"
password="1234"
userName = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
)
userName.send_keys(username)

passWord = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)

# Enter the password "Admin"
passWord.send_keys(password)

login= WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[@id='login-btn']"))
)


login.click()


# Optional: wait for 5 seconds to observe the browser interaction
WebDriverWait(driver, 5)

time.sleep(10)

# Close the browser
driver.quit()
