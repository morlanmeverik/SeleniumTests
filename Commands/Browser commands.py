import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(1)
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()

# we have to use sleep() to wait until new tab will open
time.sleep(5)

# close and quit commands

# driver.close()
driver.quit()
