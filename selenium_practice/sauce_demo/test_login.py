import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    # @pytest.mark.skip
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
    # @pytest.mark.skip
    @pytest.mark.parametrize("username, password", [
        (user, "secret_sauce") for user in LOCKED_USERS
    ])

    # @pytest.mark.skip
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

    # @pytest.mark.skip
    def test_add_all_items_to_cart(self):
        item_names = [
            'Sauce Labs Backpack',
            'Sauce Labs Bolt T-Shirt',
            'Sauce Labs Onesie',
            'Sauce Labs Bike Light',
            'Sauce Labs Fleece Jacket',
            'Test.allTheThings() T-Shirt (Red)',
        ]

        # Chrome options
        chrome_options = Options()

        # Disable password manager popup
        chrome_options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )

        # Suppress password breach / safety check popups
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--password-store=basic")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)

        # Launch browser
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get("https://www.saucedemo.com/")
            driver.maximize_window()

            # Login
            driver.find_element(By.ID, "user-name").send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()

            # Add all items
            while True:
                add_to_cart_buttons = driver.find_elements(
                    By.XPATH,
                    '//button[contains(@class, "btn_inventory") and text()="Add to cart"]'
                )

                if not add_to_cart_buttons:
                    break

                add_to_cart_buttons[0].click()

            # Validate cart count
            cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

            assert cart_badge.text == str(len(item_names)), (
                f"Expected {len(item_names)} items in cart, but got {cart_badge.text}"
            )

        finally:
            driver.quit()
