from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# click a link
# driver.find_element(By.LINK_TEXT,'open cart').click()

# find all links on the page
# allLinks = driver.find_elements(By.XPATH, '//a')
allLinks = driver.find_elements(By.TAG_NAME, 'a')
print(len(allLinks))

# Print all links names

for linkName in allLinks:
    print(linkName.text)
