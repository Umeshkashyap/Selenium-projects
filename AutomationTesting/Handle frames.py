from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver, 10)

driver.get("https://practice-automation.com/iframes/")
driver.maximize_window()

driver.switch_to.frame("top-iframe")  # select by frame name
# print("Frame pass")
button1= myWait.until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='__docusaurus']/nav/div[1]/div[1]/a[2]"))
)
# print("element loacted")
button1.click()
# print("button clicked")
driver.switch_to.default_content()  #return to the main frame
# print("default frame")

driver.switch_to.frame("bottom-iframe")
# print("frame2 pass")
button2= myWait.until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/section[2]/div/div/div[1]/div/div[2]/div/a/i"))
)
# print("frame2 element loacted")
time.sleep(10)
button2.click()
# print("button2 clicked")
driver.switch_to.default_content()

driver.quit()
