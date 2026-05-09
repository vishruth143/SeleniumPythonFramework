import os
import pytest
from api_helpers import ENDPOINTS, get_paths, call_api, save_response, compare_responses


class TestReqresComparison:
    """
    STEP 2 — Call each ReqRes endpoint and compare against the saved baseline.
    Fails if the status code or body differs (ignoring keys in IGNORED_KEYS).
    """

    @pytest.mark.regression
    @pytest.mark.parametrize("api_name,url,method,payload", ENDPOINTS)
    def test_api_comparison(self, api_name, url, method, payload):
        baseline, current, diff = get_paths(api_name)

        if not os.path.exists(baseline):
            pytest.skip(
                f"No baseline for '{api_name}'. Run test_api_baseline.py first."
            )

        status_code, body = call_api(url, method, payload)
        save_response(api_name, status_code, body, current)
        assert os.path.exists(current), f"Current response not saved for '{api_name}'!"

        match = compare_responses(baseline, current, diff)
        assert match, (
            f"API response changed for '{api_name}'! Check diff: {diff}"
        )

