import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")  # disable notifications( geolocation from browser for example
# options.add_argument("--disable-web-security")  # disable blocking popups and redirects
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Login
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
time.sleep(2)

# Find and open admin page
driver.find_element(By.LINK_TEXT, "Admin").click()

# How many rows in table
tableRows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table']//div[@class='oxd-table-body']/div[@class='oxd-table-card']"))
print("Total numbers of rows:",tableRows)

# how many users disabled/enabled
dis = 0
en = 0
for rows in range(1, tableRows+1):
    userStatus = driver.find_element(By.XPATH, "//div[@class='oxd-table']//div[@class='oxd-table-body']//div[" + str(
        rows) + "]//div[@role='cell'][5]").text
    if userStatus == "Enabled":
        en += 1
    else:
        dis += 1
print("User with enabled status:", en)
print("User with disabled status:", dis)




