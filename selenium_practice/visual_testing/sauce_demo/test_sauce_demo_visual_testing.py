import os
import sys
import pytest

# Make the shared framework importable regardless of working directory
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from framework.visual_engine import get_screenshot_paths, take_screenshot, compare_images
from sauce_demo.site_config import site, SCREENSHOTS_DIR


class TestSauceDemoVisualBaseline:
    """
    STEP 1 — Run once to capture baseline screenshots for all SauceDemo pages.
    Delete screenshots/<page>/<page>_baseline.png to re-capture a specific page.
    """

    @pytest.mark.parametrize("page", site.PAGES, ids=[p.name for p in site.PAGES])
    def test_capture_baseline(self, driver, page):
        baseline, _, _ = get_screenshot_paths(SCREENSHOTS_DIR, page.name)

        if os.path.exists(baseline):
            pytest.skip(f"Baseline exists for '{page.name}'. Delete to re-capture.")

        site.navigate_to(driver, page)
        take_screenshot(driver, baseline)
        assert os.path.exists(baseline), f"Baseline not created for '{page.name}'!"
        print(f"  Baseline captured for '{page.name}'.")


class TestSauceDemoVisualRegression:
    """
    STEP 2 — Compare current state of each SauceDemo page against the baseline.
    Fails if any pixel differences are detected.
    """

    @pytest.mark.parametrize("page", site.PAGES, ids=[p.name for p in site.PAGES])
    def test_visual_regression(self, driver, page):
        baseline, current, diff = get_screenshot_paths(SCREENSHOTS_DIR, page.name)

        if not os.path.exists(baseline):
            pytest.skip(
                f"No baseline for '{page.name}'. Run test_capture_baseline first."
            )

        site.navigate_to(driver, page)
        take_screenshot(driver, current)
        assert os.path.exists(current), \
            f"Current screenshot not created for '{page.name}'!"

        match = compare_images(baseline, current, diff)
        assert match, (
            f"Visual differences detected on '{page.name}'! "
            f"Check diff image: {diff}"
        )
