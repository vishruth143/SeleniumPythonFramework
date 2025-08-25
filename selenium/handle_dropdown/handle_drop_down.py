import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://demo.guru99.com/test/newtours/register.php")

country_drp_dwn = Select(driver.find_element(By.NAME, "country"))
country_drp_dwn.select_by_visible_text("ANTARCTICA")

all_options = country_drp_dwn.options
print("Total countries:", len(all_options))

for option in all_options:
    print(option.text)   # print visible text

#Selecting Items in a Multiple SELECT elements
driver.get("http://jsbin.com/osebed/2")
Select(driver.find_element(By.ID, "fruits")).select_by_visible_text("Banana")
Select(driver.find_element(By.ID, "fruits")).select_by_index(1)
time.sleep(10)

driver.quit()