from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.facebook.com/")
driver.implicitly_wait(1)
driver.maximize_window()

# tag name and id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("hello1")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("hello1")  # same

# tag name and class name
# driver.find_element(By.CSS_SELECTOR, "input.inputtext._55r1._6luy").send_keys("hello2")
# driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("hello2")
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("hello2")

# tag name and attribute
# driver.find_element(By.CSS_SELECTOR, 'input[data-testid="royal_email"]').send_keys("hello3")
# driver.find_element(By.CSS_SELECTOR, '[data-testid="royal_email"]').send_keys("hello3")

# tag name, class and attribute
driver.find_element(By.CSS_SELECTOR, 'input.inputtext[data-testid="royal_pass"]').send_keys("hello4")


