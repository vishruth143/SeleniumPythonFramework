from selenium import webdriver
from selenium.common import NoSuchElementException
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

fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
fluent_wait.until(EC.presence_of_element_located((By.XPATH, "//i[@class='icon-wrench']"))).click()

driver.quit()