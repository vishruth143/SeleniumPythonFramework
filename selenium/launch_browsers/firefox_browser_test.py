import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.maximize_window()

driver.get("https://google.com")

driver.set_page_load_timeout(10)

driver.find_element(By.NAME, "q").send_keys("Automation step by step")

time.sleep(2)

driver.find_element(By.XPATH, "(//input[@name='btnK'])[1]").click()

time.sleep(2)

driver.quit()

print("Test Completed")