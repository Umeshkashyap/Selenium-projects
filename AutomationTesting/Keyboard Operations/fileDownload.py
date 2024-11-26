from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

location = os.getcwd()


def chrome_browser():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\\drivers\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")

    # Download file in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    # Initialize browser with ad-blocking enabled
    driver = webdriver.Chrome(service=serv_obj, options=ops)
    block_ads(driver)  # Call the ad-blocking function
    return driver



def edge_browser():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\drivers\edgedriver_win64\msedgedriver.exe")
    # Download file in desired location
    preferences = {"download.default_directory": location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", preferences)

    # Initialize browser with ad-blocking enabled
    driver = webdriver.Edge(service=serv_obj, options=ops)
    block_ads(driver)  # Call the ad-blocking function
    return driver

def firefox_browser():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\drivers\geckodriver-v0.35.0-win-aarch64\geckodriver.exe")
    # Download file in desired location
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2)
    ops.set_preference("browser.download.dir",location)
    driver =webdriver.Firefox(service=serv_obj,options=ops)
    return driver


def block_ads(driver):
    """
    Blocks ads by preventing requests to common ad domains using Chrome DevTools Protocol.
    """
    ad_domains = ["*ads*", "*doubleclick.net*", "*googlesyndication.com*", "*adservice.google.com*"]
    driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ad_domains})
    driver.execute_cdp_cmd("Network.enable", {})
    print("Ad-blocking enabled.")


# Main script execution
#driver = chrome_browser()
#driver= edge_browser()
driver=firefox_browser()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
print("passed")
driver.maximize_window()

# Locate and click the download button
button = driver.find_element(By.XPATH, "//div[@id='table-files_wrapper']//tbody//tr[1]//td//a")
print("pass")
button.click()
print("clicked")

time.sleep(10)
driver.quit()
