from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://www.automationpractice.pl/index.php")
driver.implicitly_wait(1)
driver.maximize_window()

# OR
# (driver
#  .find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']")
#  .send_keys("T-Shirts"))
# AND
# (driver
#  .find_element(By.XPATH, "//button[@name='submit_search' and @class='btn btn-default button-search']")
#  .click())

# contains() and starts-with()
# (driver
#  .find_element(By.XPATH, "//input[contains(@id,'search')]")
#  .send_keys("T-Shirts"))
# (driver
#  .find_element(By.XPATH,"//button[starts-with(@name,'submit')]")
#  .click())

# text()

driver.find_element(By.XPATH, "//a[text()='Women']").click()



