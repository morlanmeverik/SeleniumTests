import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")  # disable notifications( geolocation from browser for example
# options.add_argument("--disable-web-security")  # disable blocking popups and redirects
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://whatmylocation.com/")
driver.maximize_window()