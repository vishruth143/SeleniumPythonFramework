from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.maximize_window()

e_title = "Demo Guru99 Page"
a_title = ""

driver.get("http://demo.guru99.com/test/guru99home/")

a_title = driver.title

if e_title == a_title:
    print('Test Passed')
else:
    print('Test Failed')

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//i[@class='icon-wrench']"))).click()

driver.quit()