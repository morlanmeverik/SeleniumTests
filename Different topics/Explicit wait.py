from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

# Explicit
# waitTime = WebDriverWait(driver,10)  # explicit time wait declaration # basic variant
waitTime = WebDriverWait(driver,10, poll_frequency= 2,   ignored_exceptions=[NoSuchElementException,
                                                               ElementNotVisibleException,
                                                               ElementNotSelectableException,
                                                               Exception]
                         )


driver.get("https://google.com")
driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")
search.submit()

link = waitTime.until(EC.presence_of_element_located((By.XPATH, "//a[@href='https://www.selenium.dev/']")))
# the previous condition should be satisfied only if the element is available
link.click()