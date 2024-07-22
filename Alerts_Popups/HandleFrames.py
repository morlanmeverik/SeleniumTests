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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


driver.switch_to.frame("frame-one796456169")
el = driver.find_element(By.XPATH, "//a[normalize-space()='Powered by']")
driver.execute_script("arguments[0].click()", el)
driver.switch_to.default_content()
time.sleep(2)
driver.back()

