import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
# # Alert has text, text field and 2 buttons OK and cancel

# opens alert window
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(3)
# normalize-space() == text() but first ignore additional spaces

alertWindow = driver.switch_to.alert

# show alert text
print(alertWindow.text)

# add some text to the alert field
alertWindow.send_keys("Hello")

# close alert window with OK clicking
# alertWindow.accept()

# Close alert window with Cancel button
alertWindow.dismiss()
