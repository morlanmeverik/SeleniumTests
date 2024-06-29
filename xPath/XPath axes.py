from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://money.rediff.com/gainers")
driver.implicitly_wait(1)
driver.maximize_window()

# self
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/self::a").text
# print(text_msg)

# parent
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/parent::td").text
# print(text_msg)

# ascendant + child methods
# childs = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/child::td")
# print(len(childs))

# ascendant parents and grandfathers
# text_msg = driver.find_element(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr").text
# print(text_msg)  # got data from every child

# Descendant childs and grandchilds
# descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/descendant::*")
# print(len(descendants))  # 10

# Following
# followings = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/following::*")
# print(len(followings))  # 22602

# Following-sibling
# following_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/following-sibling::*")
# print(len(following_siblings))  # 2041

# Preceding
# precedings = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/preceding::*")
# print(len(precedings))  # 255

# Preceding-sibling
precedingSiblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Jonjua Overseas')]/ancestor::tr/preceding::tr")
print(len(precedingSiblings))  # 11
