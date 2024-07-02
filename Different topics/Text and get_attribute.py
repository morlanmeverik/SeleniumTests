from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(1)
driver.maximize_window()


username = driver.find_element(By.NAME, "username")

username.clear()
username.send_keys("newUsername")

print("result of text:", username.text)  # nothing
print("result of get_attribute:", username.get_attribute('value'))  # print newUsername

button = driver.find_element(By.CLASS_NAME, "oxd-button")

print("result of text:", button.text)  # Login
print("result of get_attribute:", button.get_attribute('value'))  # nothing

