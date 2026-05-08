# Tutorial: Taking Screenshots in Selenium
# ------------------------------------------
# This script demonstrates how to capture and save screenshots of a web page
# using Selenium WebDriver. Screenshots are useful for visual validation,
# debugging test failures, and generating test reports.
#
# Key Method:
#   - driver.save_screenshot(file_path) : Captures the current browser viewport
#                                         and saves it as a PNG image to the given path.
#
# Best Practices:
#   - Use os.path.join() to build file paths in a cross-platform compatible way.
#   - Use os.makedirs(path, exist_ok=True) to ensure the output directory exists
#     before saving, without raising an error if it already exists.
#   - Wrap screenshot logic in a try/except block to handle errors gracefully.
#   - Organize screenshots into a dedicated folder (e.g., "screenshots/") for easy access.
#
# In this example, the script:
#   1. Launches Chrome and navigates to Google.
#   2. Calls a reusable take_screenshot() function that ensures the output
#      directory exists and saves the screenshot as a PNG file.

import os

from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")

    try:
        take_screenshot(driver, "Google_HomePage")
        print("Screenshot saved successfully!")
    except Exception as e:
        print(f"Failed to take screenshot: {str(e)}")

def take_screenshot(driver, file_name):
    # Define the directory for saving screenshots
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    # Create the directory if it doesn't exist
    os.makedirs(screenshots_dir, exist_ok=True)
    # File path with the provided file name
    file_path = os.path.join(screenshots_dir, f"{file_name}.png")
    # Take a screenshot and save it to the specified file path
    driver.save_screenshot(file_path)

if __name__ == "__main__":
    main()