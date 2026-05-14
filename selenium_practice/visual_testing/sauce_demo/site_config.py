"""
SauceDemo site configuration for visual testing.

Defines:
  - BASE_URL
  - PAGES to test
  - Login logic via pre_navigate()
  - SCREENSHOTS_DIR used by the test files
"""

import os
import sys
import time

from selenium.webdriver.common.by import By

# Make the shared framework importable regardless of working directory
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, ".."))

from framework.site_config import SiteConfig, PageEntry

# ── Site-specific constants ────────────────────────────────────────────────────

SCREENSHOTS_DIR = os.path.join(_HERE, "screenshots")

# ── Config class ──────────────────────────────────────────────────────────────

class SauceDemoConfig(SiteConfig):
    BASE_URL = "https://www.saucedemo.com"
    PAGES = [
        PageEntry("login_page",     "/",               requires_login=False),
        PageEntry("inventory_page", "/inventory.html", requires_login=True),
        PageEntry("cart_page",      "/cart.html",      requires_login=True),
    ]

    def pre_navigate(self, driver, page: PageEntry) -> None:
        """Log in with standard_user before navigating to protected pages."""
        driver.get(f"{self.BASE_URL}/")
        time.sleep(1)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)


# Singleton used by the test files
site = SauceDemoConfig()
