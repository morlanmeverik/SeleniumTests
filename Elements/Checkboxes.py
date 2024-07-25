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

# select specific checkbox
#driver.find_elements(By.XPATH, "//input[@id='monday']")

# Select all checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
print(len(checkboxes))

# Approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()
#     time.sleep(1)

# Approach 2
# for checkbox in checkboxes:
#      checkbox.click()

# Select multiple  checkboxes by choice
# for checkbox in checkboxes:
#     weekName = checkbox.get_attribute('id')
#     if weekName == 'monday' or weekName == 'sunday':
#         checkbox.click()

# Select only 2 last checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):  # (5,7) --> 6 7
#     checkboxes[i].click()

# Select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:  # 0 and 1 elements
#         checkboxes[i].click()

# clearing all checkboxes
# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()





