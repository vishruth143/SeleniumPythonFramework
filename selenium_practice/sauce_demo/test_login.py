import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Users expected to successfully log in
VALID_USERS = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user",
]

# Users expected to be blocked / show an error on login
LOCKED_USERS = [
    "locked_out_user",
]

class TestSauceDemo:
    @pytest.mark.parametrize("username, password", [
        (user, "secret_sauce") for user in VALID_USERS
    ])
    def test_login_success(self, username, password):
        """Valid users should land on the inventory page after login."""
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()

            # Assert successful login — URL must change to the inventory page
            assert "/inventory.html" in driver.current_url, (
                f"Login failed for '{username}': stayed on {driver.current_url}"
            )
        finally:
            driver.quit()


    @pytest.mark.parametrize("username, password", [
        (user, "secret_sauce") for user in LOCKED_USERS
    ])
    def test_login_locked_user(self, username, password):
        """Locked-out users should see an error message and NOT be redirected."""
        driver = webdriver.Chrome()
        try:
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()
            driver.find_element(By.ID, "user-name").send_keys(username)
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "login-button").click()

            # Assert error container is visible
            error_element = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
            assert error_element.is_displayed(), (
                f"Expected an error message for locked user '{username}' but none was shown."
            )
            assert "locked out" in error_element.text.lower(), (
                f"Unexpected error text for '{username}': {error_element.text}"
            )
        finally:
            driver.quit()
