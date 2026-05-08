# Tutorial: Handling iFrames in Selenium
# ----------------------------------------
# An iFrame (Inline Frame) is an HTML element that embeds another HTML document
# within the current page. Selenium cannot directly interact with elements inside
# an iFrame without first switching its focus into it.
#
# Key Methods:
#   - driver.switch_to.frame(element) : Switches WebDriver focus into the specified iFrame.
#                                       Accepts a WebElement, index, or name/id string.
#   - driver.switch_to.default_content(): Switches focus back to the main page (exits all iFrames).
#   - driver.switch_to.parent_frame()  : Switches focus to the immediate parent frame.
#
# Ways to Locate and Switch to an iFrame:
#   - By index      : driver.switch_to.frame(0)
#   - By name/id    : driver.switch_to.frame("iframeResult")
#   - By WebElement : driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='...']"))
#
# In this example, the script:
#   1. Navigates to a W3Schools page containing an iFrame.
#   2. Locates and switches into the iFrame by its WebElement.
#   3. Clicks a button inside the iFrame that triggers a JS Confirm alert.
#   4. Reads and dismisses the alert.

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm")

iframe = driver.find_element(By.XPATH, "//iframe[@id='iframeResult']")

driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()

print(Alert(driver).text)

Alert(driver).dismiss()

driver.quit()