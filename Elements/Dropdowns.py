import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dropCountry_ele = driver.find_element(By.XPATH, "//select[@id='country']")
dropCountry = Select(dropCountry_ele)

# select option from dropdown
# dropCountry.select_by_visible_text("Germany")
# time.sleep(3)
# dropCountry.select_by_value("france")
# time.sleep(3)
# dropCountry.select_by_index(1)  # Canada

# capture all options and print them
# allOptions = dropCountry.options
# print("total number of oprions:", len(allOptions))

# for opt in allOptions:
#     print(opt.text)

# Select option from dropdown without built-in method
# for opt in allOptions:
#     if opt.text == "Germany":
#         opt.click()
#         break

# without additional methods
Options = driver.find_elements(By.XPATH, "//select[@id='country']/option")
print(len(Options))
print(Options[2].text)  # United Kingdom
Options[3].click()
