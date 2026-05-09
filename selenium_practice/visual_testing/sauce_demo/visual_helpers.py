import os
import time
from PIL import Image, ImageChops
from selenium.webdriver.common.by import By

BASE_URL = "https://www.saucedemo.com"
SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots", "saucedemo")

# ── Pages to test ─────────────────────────────────────────────────────────────
# Each entry: (page_name, url_path, login_required)
PAGES = [
    ("login_page",     "/",               False),
    ("inventory_page", "/inventory.html", True),
    ("cart_page",      "/cart.html",      True),
]


def get_paths(page_name):
    """Return (baseline, current, diff) absolute paths for a given page name."""
    page_dir = os.path.join(SCREENSHOTS_DIR, page_name)
    os.makedirs(page_dir, exist_ok=True)
    return (
        os.path.join(page_dir, f"{page_name}_baseline.png"),
        os.path.join(page_dir, f"{page_name}_current.png"),
        os.path.join(page_dir, f"{page_name}_diff.png"),
    )


def do_login(driver):
    """Log in with standard_user credentials."""
    driver.get(f"{BASE_URL}/")
    time.sleep(1)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)


def navigate_to(driver, url_path, login_required):
    """Navigate to the given page, logging in first if needed."""
    if login_required:
        do_login(driver)
    driver.get(f"{BASE_URL}{url_path}")
    time.sleep(2)


def take_screenshot(driver, path):
    """Save a screenshot to the given path."""
    driver.save_screenshot(path)
    print(f"  Screenshot saved → {path}")


def compare_images(baseline_path, current_path, diff_path):
    """
    Pixel-by-pixel comparison.
    Returns True  → images match (no diff file written).
    Returns False → differences found (diff file written).
    """
    img1 = Image.open(baseline_path).convert("RGB")
    img2 = Image.open(current_path).convert("RGB")

    if img1.size != img2.size:
        img2 = img2.resize(img1.size)

    diff_img = ImageChops.difference(img1, img2)
    bbox = diff_img.getbbox()

    if bbox:
        diff_img.save(diff_path)
        print(f"  ❌ Differences found → {diff_path}")
        return False

    # Remove stale diff file if images now match
    if os.path.exists(diff_path):
        os.remove(diff_path)
    print("  ✅ No visual differences.")
    return True

