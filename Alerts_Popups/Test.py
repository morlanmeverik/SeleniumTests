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

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("Selenium")
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()
links = driver.find_elements(By.XPATH, "//div[@id='Wikipedia1_wikipedia-search-results']//a")
print(links)

for everyLink in links:
    everyLink.click()

windowIDs = driver.window_handles
time.sleep(2)

# switch between windows

# for winID in windowIDs:
#     driver.switch_to.window(winID)
#     print(winID)
#     time.sleep(1)

# enumerate the array and close every tab except parent
for index, content in enumerate(windowIDs):
    print(index, content)
    if index > 0:
        driver.switch_to.window(content)
        time.sleep(2)
        driver.close()

