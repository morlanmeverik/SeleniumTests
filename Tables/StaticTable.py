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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1 Count number of rows and columns
tableRows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
tableColumns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
print(len(tableRows))  # 7
print(len(tableColumns))  # 4
print(tableColumns[1].text)  # Author

# 2 Read specific row and column data

data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[5]/td[1]").text

print(data)  # Master in Selenium

# 3 Read all rows and columns data
# print("All data...")
# for rows in range(2, len(tableRows)+1):
#     for columns in range(1, len(tableColumns)+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(rows)+"]/td["+str(columns)+"]").text
#         print(data)
#     print()

# 4 Read data based on condition(only Mukesh)
print("Mukesh's book names are: ")
for rows in range(2, len(tableRows)+1):
    authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(rows)+"]/td[2]").text
    if authorName == "Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(rows)+"]/td[1]").text
        bookPrice = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr["+str(rows)+"]/td[4]").text
        print(bookName, '', bookPrice)


