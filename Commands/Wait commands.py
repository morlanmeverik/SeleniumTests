import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

# Implicitly command
driver.implicitly_wait(10)

driver.get("https://google.com")
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()

# time sleep
time.sleep(3)
driver.find_element(By.XPATH, "//a[@href='https://www.selenium.dev/']").click()


