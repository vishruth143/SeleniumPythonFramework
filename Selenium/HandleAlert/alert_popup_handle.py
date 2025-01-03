import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Navigate to the Rediff login page
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

# Click the "Sign in" button without entering credentials
driver.find_element(By.XPATH, "//input[@title='Sign in']").click()

time.sleep(10)

# Handle the alert that appears
Alert(driver).accept()

# Ensure the browser is closed regardless of the outcome
driver.quit()