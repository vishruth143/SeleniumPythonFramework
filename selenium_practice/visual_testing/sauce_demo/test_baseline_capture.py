import os
import pytest
from visual_helpers import PAGES, get_paths, navigate_to, take_screenshot


class TestSauceDemoVisualBaseline:
    """
    STEP 1 — Run once to capture baseline screenshots for all SauceDemo pages.
    Delete screenshots/<page>/<page>_baseline.png to re-capture a specific page.
    """

    @pytest.mark.parametrize("page_name,url_path,login_required", PAGES)
    def test_capture_baseline(self, driver, page_name, url_path, login_required):
        baseline, _, _ = get_paths(page_name)

        if os.path.exists(baseline):
            pytest.skip(f"Baseline exists for '{page_name}'. Delete to re-capture.")

        navigate_to(driver, url_path, login_required)
        take_screenshot(driver, baseline)
        assert os.path.exists(baseline), f"Baseline not created for '{page_name}'!"
        print(f"  Baseline captured for '{page_name}'.")
