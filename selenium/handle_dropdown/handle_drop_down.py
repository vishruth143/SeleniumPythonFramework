# Tutorial: Handling Dropdowns in Selenium
# ------------------------------------------
# This script demonstrates how to interact with HTML <select> dropdown elements
# using Selenium's built-in Select class.
#
# Key Class:
#   - Select(element) : Wraps a <select> web element to provide dropdown-specific methods.
#
# Key Methods:
#   - select_by_visible_text(text) : Selects an option by its displayed text.
#   - select_by_index(index)       : Selects an option by its position (0-based index).
#   - select_by_value(value)       : Selects an option by its HTML "value" attribute.
#   - .options                     : Returns a list of all available options in the dropdown.
#   - .all_selected_options        : Returns a list of all currently selected options.
#   - .first_selected_option       : Returns the first (or only) selected option.
#
# Types of Dropdowns:
#   - Single-select  : Only one option can be selected at a time (default).
#   - Multi-select   : Multiple options can be selected simultaneously (select_by_* called multiple times).
#
# In this example, the script:
#   1. Selects "ANTARCTICA" from a country dropdown by visible text and prints all available options.
#   2. Navigates to a multi-select dropdown and selects items by visible text and by index.

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