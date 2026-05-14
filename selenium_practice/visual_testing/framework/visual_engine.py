"""
Generic, site-agnostic visual-testing engine.

Provides:
  - get_screenshot_paths()  → (baseline, current, diff) paths
  - take_screenshot()
  - compare_images()
"""

import os
from PIL import Image, ImageChops


def get_screenshot_paths(screenshots_root: str, page_name: str) -> tuple[str, str, str]:
    """
    Return (baseline, current, diff) absolute paths for a page.

    screenshots_root : absolute path to the site's screenshots directory
    page_name        : slug used as sub-folder and filename prefix
    """
    page_dir = os.path.join(screenshots_root, page_name)
    os.makedirs(page_dir, exist_ok=True)
    return (
        os.path.join(page_dir, f"{page_name}_baseline.png"),
        os.path.join(page_dir, f"{page_name}_current.png"),
        os.path.join(page_dir, f"{page_name}_diff.png"),
    )


def take_screenshot(driver, path: str) -> None:
    """Save a full-page screenshot to *path*."""
    driver.save_screenshot(path)
    print(f"  📸 Screenshot saved → {path}")


def compare_images(baseline_path: str, current_path: str, diff_path: str) -> bool:
    """
    Pixel-by-pixel comparison between baseline and current screenshots.

    Returns
    -------
    True  → images match (any stale diff file is removed).
    False → differences found (diff image written to diff_path).
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

    if os.path.exists(diff_path):
        os.remove(diff_path)
    print("  ✅ No visual differences.")
    return True

