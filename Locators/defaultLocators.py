from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(1)
driver.maximize_window()

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()
# find search by 2 class names
driver.find_element(By.CLASS_NAME, "oxd-input.oxd-input--active").send_keys("Time")

# find link by css selector
driver.find_element(By.CSS_SELECTOR, 'a[href="/web/index.php/time/viewTimeModule"]').click()

# find link by linkText & partialLinkText
# driver.find_element(By.PARTIAL_LINK_TEXT, "Tim").click()
# driver.find_element(By.LINK_TEXT, "Time").click()










