import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.facebook.com/")
driver.implicitly_wait(1000)
driver.maximize_window()
driver.get("https://www.google.com.ua/")
time.sleep(1)

# back()
driver.back()  # facebook
time.sleep(1)
# forward
driver.forward()  # google
time.sleep(1)
# refresh
driver.refresh()

driver.quit()


