import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")  # disable notifications( geolocation from browser for example
# options.add_argument("--disable-web-security")  # disable blocking popups and redirects
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # switch to the first iframe on the page, better to use when we have 1 frame on the page

# mm/dd/yy
# driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("05/30/24")  # when we can write

# variables
year = "2026"
month = "April"
day = "9"

driver.find_element(By.XPATH, "// input[@id='datepicker']").click()  # opens datepicker

# find and compare month and year
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break;
    if int(year) < 2024:
        driver.find_element(By.XPATH, "//a[@class='ui-datepicker-prev ui-corner-all']").click()  # prev arrow
    else:
        driver.find_element(By.XPATH, "//a[@class='ui-datepicker-next ui-corner-all']").click()  # next arrow

# select date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text == day:
        ele.click()
        break
