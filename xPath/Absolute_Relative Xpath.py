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

# Absolute XPATH

# (driver
#  .find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]")
#  .send_keys("Hello"))
# (driver
#  .find_element(By.XPATH, "/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button")
#  .click())

# Relative XPATH

(driver
 .find_element(By.XPATH, "//input[@id='search_query_top']")
 .send_keys("Hello"))
(driver
 .find_element(By.XPATH, "//form[@id='searchbox']/button")
 .click())


