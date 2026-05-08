# Tutorial: Explicit Wait in Selenium
# -------------------------------------
# Explicit Wait tells the WebDriver to wait for a specific condition to be met
# before proceeding, up to a maximum timeout. Unlike implicit wait, it applies
# only to a particular element or condition, giving you more precise control.
#
# Key Classes:
#   - WebDriverWait(driver, timeout): Sets up the wait with a max timeout (seconds).
#   - expected_conditions (EC): Provides built-in conditions to wait for, such as:
#       * presence_of_element_located  - element exists in the DOM
#       * visibility_of_element_located - element is visible on the page
#       * element_to_be_clickable      - element is visible and enabled
#
# Syntax:
#   WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "...")))
#
# In this example, the driver waits up to 10 seconds for a specific element
# (identified by XPATH) to be present in the DOM before clicking it.

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