# Tutorial: Implicit Wait in Selenium
# -------------------------------------
# Implicit Wait tells the WebDriver to wait for a certain amount of time
# before throwing a "No Such Element" exception. It is set once and applies
# globally to all element searches for the lifetime of the WebDriver instance.
#
# Syntax: driver.implicitly_wait(time_in_seconds)
#
# In this example, the driver will wait up to 10 seconds for elements to appear
# before raising an exception. This is useful when dealing with pages that load
# content dynamically or have slight delays.

from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.implicitly_wait(10)

e_title = "Demo Guru99 Page"
a_title = ""

driver.get("http://demo.guru99.com/test/guru99home/")

a_title = driver.title

if e_title == a_title:
    print('Test Passed')
else:
    print('Test Failed')

driver.quit()