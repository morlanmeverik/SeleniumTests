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

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Handle single window ID
# windowID = driver.current_window_handle
# print(windowID)

# Handle multiple window IDs
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
windowIDs = driver.window_handles
time.sleep(2)
# Approach 1

# parentWindowID = windowIDs[0]
# childWindowID = windowIDs[1]
# print(parentWindowID, childWindowID)
# print(driver.title)  # clicked on the link but parentWindow is still a currentWindow
#
# driver.switch_to.window(childWindowID)  # Switched to the childWindow, now child is the current window
# print(driver.title)
#
# driver.switch_to.window(parentWindowID)  # Return to the parentWindow
# print(driver.title)

# Approach 2

# for winID in windowIDs:
#     driver.switch_to.window(winID)
#     print(driver.title)

# close specific browser window
for winID in windowIDs:
    driver.switch_to.window(winID)
    if driver.title == "OrangeHRM":
        driver.close()

