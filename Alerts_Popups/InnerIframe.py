import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")  # disable blocking popups and redirects
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@href='#Multiple']").click()

outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")  # specify frame as a webElement
driver.switch_to.frame(outerFrame)

innerFrame = driver.find_element(By.XPATH, "//iframe[@src='SingleFrame.html']")  # specify frame as a webElement
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("hello")

# driver.switch_to.parent_frame()
