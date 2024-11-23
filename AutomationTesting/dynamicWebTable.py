from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Chrome driver
serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
myWait = WebDriverWait(driver, 10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(5)
# # Login the page
# userName = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
# userName.send_keys("Admin")
# password = driver.find_element(By.XPATH, "//input[@placeholder='Password']")
# password.send_keys("admin123")
# button = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
# button.click()
#
#
# # time.sleep(5)
#
# adminBtn=myWait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span")))
# adminBtn.click()
# # driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
#
# # find out the table because of this whole table built in div and container
# # table=myWait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='orangehrm-container']")))
# # print("test sucess")
#
# tableRow=driver.find_element(By.XPATH,"//div[2][@class='oxd-table-card']").text
#
# print(tableRow)
#
#
# # for r in tableRow:
# #     data=driver.find_element(By.XPATH,"//div["+str(r)+"]@class='oxd-table-card']//div[5]")
# #     # #print(data)
#
#
#
#
#
# # tableColumn=myWait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='oxd-table-body']//div[1]//div//div[5]")))
# # print(tableColumn.text)
#
#



time.sleep(5)
