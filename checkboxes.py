from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
waitTime=WebDriverWait(driver,10)

# Open the OrangeHRM website
driver.get("http://192.168.1.150/dolphin/public/")

username = "admin"
password = "1234"

# Wait until the username input field is present and enter username
userName = waitTime.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
)
userName.send_keys(username)

# Wait until the password input field is present and enter password
passWord = waitTime.until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)
passWord.send_keys(password)

# Wait until the login button is clickable and click it
login = waitTime.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='login-btn']"))
)
login.click()

# Wait until the 'Configuration Management' element is clickable and click it
configuration = waitTime.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Configuration Management']"))
)
configuration.click()

# Wait until the 'Ticket Layout' element is clickable and click it
ticket = waitTime.until(
    EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Ticket Layout']"))
)
ticket.click()


edit= waitTime.until(
    EC.element_to_be_clickable((By.XPATH, "//tbody/tr[3]/td[4]/button[3]"))
)
edit.click()
check= waitTime.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@id='location_name-l01']"))
)
check.click()

checkBoxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' or @class='ticket_options']")
print(len(checkBoxes))

for checkbox in checkBoxes:
    print(checkbox)




# Optional: wait for 5 seconds to observe the browser interaction
time.sleep(5)



# Close the browser
driver.quit()
