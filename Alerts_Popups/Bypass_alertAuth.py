import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

# # we can't work with auth alert, so we need to bypass it
# usual opening
# driver.get("https://the-internet.herokuapp.com/basic_auth")

# bypass -- username - admin , password - admin
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()