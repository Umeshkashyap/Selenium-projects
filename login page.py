<<<<<<< HEAD
from selenium import webdriver
=======
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://ayushman.nwaredev.com/")


driver.find_element(By.XPATH,"//input[@id='email']").send_keys("admin@gmail.com")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("password")

driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()

driver.find_element(By.XPATH,"//a[normalize-space()='Master Hospitals']").click()
driver.find_element(By.XPATH,"//a[@class='btn btn-primary']").click()

driver.find_element(By.XPATH,"//input[@id='title']").send_keys("Testing")
fileinput=driver.find_element(By.XPATH,"//input[@id='customFile']").click()

fileinput
time.sleep(10)
>>>>>>> 5181629 (add details)
