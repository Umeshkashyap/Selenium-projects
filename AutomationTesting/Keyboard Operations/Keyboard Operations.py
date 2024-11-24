from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
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

driver.get("https://text-compare.com/")
driver.maximize_window()

#Operations need to performs:
# 1. CTRL+A
# 2. CTRL+C
# 3. Tab
# 4. CTRL+V

textBox1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
textBox2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

textBox1.send_keys("test keyBoard operations")

act=ActionChains(driver)
# press ctrl+a in inputbox 1
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# press ctrl+c in inputbox 1
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab
act.send_keys(Keys.TAB).perform()

# press ctrl+v in inputBox 2
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

print("KeyBoard Operations passed")
time.sleep(5)

