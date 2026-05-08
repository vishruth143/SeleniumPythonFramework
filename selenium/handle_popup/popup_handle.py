# Tutorial: Handling Popup Windows in Selenium
# ----------------------------------------------
# This script demonstrates how to handle browser popup windows (new tabs/windows)
# that open when interacting with web elements.
#
# Key Concepts:
#   - driver.current_window_handle  : Returns the handle (unique ID) of the currently focused window.
#   - driver.window_handles          : Returns a list of all open window handles in the session.
#   - driver.switch_to.window(handle): Switches WebDriver focus to the specified window.
#   - driver.close()                 : Closes the currently focused window (not the entire session).
#   - driver.quit()                  : Closes all windows and ends the WebDriver session.
#
# Typical Workflow for Handling Popups:
#   1. Store the main window handle before triggering the popup.
#   2. Click the element that opens the new window/tab.
#   3. Iterate over all window handles and switch to the one that is not the main window.
#   4. Perform any required actions in the popup window.
#   5. Close the popup and switch focus back to the main window.
#
# In this example, the script opens a new window via a link click, reads its title
# and content, closes it, and then switches back to the main window.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")

# Step 2: Get main window handle
main_window = driver.current_window_handle
print("Main Window Title:", driver.title)

# Step 3: Click link that opens a new window
driver.find_element(By.LINK_TEXT, "Click Here").click()

# Step 4: Get all window handles
all_windows = driver.window_handles

# Step 5: Switch to the new window
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        print("Popup Window Title:", driver.title)
        print("Popup Window Text:", driver.find_element(By.TAG_NAME, "h3").text)

        # Close the popup window
        driver.close()

# Step 6: Switch back to main window
driver.switch_to.window(main_window)
print("Back to Main Window:", driver.title)

time.sleep(2)
driver.quit()