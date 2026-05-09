import os
import pytest
from visual_helpers import PAGES, get_paths, navigate_to, take_screenshot, compare_images


class TestSauceDemoVisualRegression:
    """
    STEP 2 — Compare current state of each SauceDemo page against the baseline.
    Fails if any pixel differences are detected.
    """

    @pytest.mark.parametrize("page_name,url_path,login_required", PAGES)
    def test_visual_regression(self, driver, page_name, url_path, login_required):
        baseline, current, diff = get_paths(page_name)

        if not os.path.exists(baseline):
            pytest.skip(
                f"No baseline for '{page_name}'. Run test_visual_baseline.py first."
            )

        navigate_to(driver, url_path, login_required)
        take_screenshot(driver, current)
        assert os.path.exists(current), \
            f"Current screenshot not created for '{page_name}'!"

        match = compare_images(baseline, current, diff)
        assert match, (
            f"Visual differences detected on '{page_name}'! "
            f"Check diff image: {diff}"
        )

