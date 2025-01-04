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