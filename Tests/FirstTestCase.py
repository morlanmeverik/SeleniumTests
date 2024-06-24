from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(1)

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()
actual_title = driver.title
exp_title = "OrangeHRM"

if actual_title == exp_title:
    print("test passed successfully")
else:
    print("test failed easily")

#driver.close()