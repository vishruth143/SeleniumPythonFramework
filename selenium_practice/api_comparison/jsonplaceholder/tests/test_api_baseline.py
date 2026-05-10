import os
import pytest
from framework.api_helpers import ENDPOINTS, get_paths, call_api, save_response


class TestReqresBaseline:
    """
    STEP 1 — Capture baseline responses for all ReqRes endpoints.
    Delete responses/<api_name>/<api_name>_baseline.json to re-capture a specific one.
    """

    @pytest.mark.baseline
    @pytest.mark.parametrize("api_name,url,method,payload", ENDPOINTS)
    def test_capture_baseline(self, api_name, url, method, payload):
        baseline, _, _ = get_paths(api_name)

        if os.path.exists(baseline):
            pytest.skip(f"Baseline exists for '{api_name}'. Delete to re-capture.")

        status_code, body = call_api(url, method, payload)
        save_response(api_name, status_code, body, baseline)

        assert os.path.exists(baseline), f"Baseline not created for '{api_name}'!"
        print(f"  ✅ Baseline captured for '{api_name}' [HTTP {status_code}]")
