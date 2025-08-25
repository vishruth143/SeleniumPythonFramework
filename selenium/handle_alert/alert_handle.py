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
driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()

time.sleep(2)

# Handle the alert that appears
# print(Alert(driver).text)
# Alert(driver).accept()
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()  # Click OK

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

# Click "Click for JS Alert"
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Switch to alert and accept
alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.accept()   # Click OK

# Click "Click for JS Confirm"
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()

alert = driver.switch_to.alert
print("Alert text:", alert.text)
alert.dismiss()  # Click Cancel

# Click "Click for JS Prompt"
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

alert = driver.switch_to.alert
print("Prompt text:", alert.text)
alert.send_keys("Vishvambruth")  # Enter text
alert.accept()

time.sleep(2)
driver.quit()

# Ensure the browser is closed regardless of the outcome
driver.quit()