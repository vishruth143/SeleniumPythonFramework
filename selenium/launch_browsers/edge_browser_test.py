# Tutorial: Launching Microsoft Edge Browser with Selenium
# ----------------------------------------------------------
# This script demonstrates how to launch Microsoft Edge using Selenium WebDriver
# and perform a basic search on Google.
#
# Key Concepts:
#   - webdriver.Edge()           : Initializes a Microsoft Edge browser instance.
#                                  Requires Microsoft Edge and EdgeDriver to be installed.
#                                  EdgeDriver must match the installed Edge browser version.
#   - driver.maximize_window()   : Maximizes the browser window.
#   - driver.get(url)            : Navigates to the specified URL.
#   - set_page_load_timeout(sec) : Sets the maximum time to wait for a page to load.
#   - find_element(By, value)    : Locates a web element using a locator strategy (e.g., NAME, XPATH).
#   - send_keys(text)            : Types text into an input field.
#   - .click()                   : Clicks on a web element.
#   - time.sleep(sec)            : Pauses execution for a given number of seconds.
#   - driver.quit()              : Closes the browser and ends the WebDriver session.
#
# In this example, the script opens Google in Edge, searches for "Automation step by step",
# and clicks the search button, with short pauses to observe the actions.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.maximize_window()

driver.get("https://google.com")

driver.set_page_load_timeout(10)

driver.find_element(By.NAME, "q").send_keys("Automation step by step")

time.sleep(2)

driver.find_element(By.XPATH, "(//input[@name='btnK'])[1]").click()

time.sleep(2)

driver.quit()

print("Test Completed")
