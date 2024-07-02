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

# FIND_ELEMENT() - single element return

# 1 Locator matching with a single element
# driver.find_element(By.XPATH, "//input[@name='username']").send_keys("usernameText") # webElementObject

# 2 Locator matching with multiple webelements
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button").click()
# element = driver.find_element(By.XPATH, "//ul[@class='oxd-main-menu']//a")
# print(element.text)  # only first link from sidebar -  "Admin"

# 3 Element not available then throw NoSuchElementException
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button").click()
# driver.find_element(By.LINK_TEXT, "Tim").click() # wrong link text

# FIND_ELEMENTS() - multiple webElements return

# 1 Locator matching with a single webElement
# elements = driver.find_elements(By.XPATH, "//input[@name='username']")  # saves list
# print(len(elements))  # 1
# elements[0].send_keys("username")

# 2 Locator matching with multiple webelements
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button").click()
# elements = driver.find_elements(By.XPATH, "//ul[@class='oxd-main-menu']//a")
# print(len(elements))  # every link from sidebar, 12 links available
# print(elements[1].text)  # user sees second link - "PIM"
# for links in elements:
#     print(links.text)  # simple loop to show all links

# 3 Element not available then  - zero in the list
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "oxd-button").click()
elements = driver.find_elements(By.LINK_TEXT, "Tim")  # wrong link text
print(len(elements))
