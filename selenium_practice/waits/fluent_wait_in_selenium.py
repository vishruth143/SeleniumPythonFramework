# Tutorial: Fluent Wait in Selenium
# ------------------------------------
# Fluent Wait is an advanced form of Explicit Wait that gives you full control
# over the polling behavior while waiting for a condition to be met.
#
# Key Parameters of WebDriverWait (Fluent Wait):
#   - timeout         : Maximum time to wait for the condition (in seconds).
#   - poll_frequency  : How often (in seconds) to check the condition. Default is 0.5s.
#   - ignored_exceptions: A list of exceptions to ignore during polling (e.g., NoSuchElementException).
#
# How it differs from Explicit Wait:
#   - Explicit Wait uses default polling (every 0.5s) with no ignored exceptions.
#   - Fluent Wait lets you customize the poll interval and suppress specific exceptions,
#     making it ideal for elements that appear intermittently or take irregular time to load.
#
# Syntax:
#   fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=5, ignored_exceptions=[NoSuchElementException])
#   fluent_wait.until(EC.presence_of_element_located((By.XPATH, "...")))
#
# In this example, the driver checks every 5 seconds (up to 10 seconds total) for
# the element to be present, ignoring NoSuchElementException during each poll.

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