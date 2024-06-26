from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.sinsay.com/ua/uk/")
driver.implicitly_wait(1)
driver.maximize_window()

driver.find_element(By.ID, "cookiebotDialogOkButton").click()
sliders = driver.find_elements(By.CSS_SELECTOR, "#category-40665 .product-slide")
print(len(sliders))