import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service("D:\\WebDrivers\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")  # disable notifications( geolocation from browser for example
# options.add_argument("--disable-web-security")  # disable blocking popups and redirects
options.add_experimental_option("detach", True)  # to prevent browser closing
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# find input
driver.find_element(By.XPATH, "//input[@id='dob']").click()

# Months dropdown
datepicker_month = Select(driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Dec")

# Years dropdown
datepicker_year = Select(driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']/select[@class='ui-datepicker-year']"))
datepicker_year.select_by_visible_text("1997")

allDates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in allDates:
    if date.text == "25":
        date.click()
        break