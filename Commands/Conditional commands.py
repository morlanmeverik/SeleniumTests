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

driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

# is_displayed() and is_enabled()
searchBox = driver.find_element(By.XPATH, "//div[@class='oxd-main-menu-search']")

print("Display checkBox status:", searchBox.is_displayed())
print("Enable checkBox status:", searchBox.is_enabled())

# is_selected
driver.find_element(By.XPATH, "//a[@href='/web/index.php/pim/viewMyDetails']").click()

male_input = driver.find_element(By.XPATH, "//input[@value='1']")
female_input = driver.find_element(By.XPATH, "//input[@value='2']")

male_label = driver.find_element(By.XPATH, "//label[text()='Male']")
female_label = driver.find_element(By.XPATH, "//label[text()='Female']")
print("Male selected:", male_input.is_selected())  # False
print("Female selected:", female_input.is_selected())  # False

female_label.click()
print("Male selected:", male_input.is_selected())  # False
print("Female selected:", female_input.is_selected())  # True

male_label.click()
print("Male selected:", male_input.is_selected())  # True
print("Female selected:", female_input.is_selected())  # False
