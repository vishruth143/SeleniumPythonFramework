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