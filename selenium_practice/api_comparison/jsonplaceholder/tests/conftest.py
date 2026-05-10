import sys
import os

# ── Add framework/ to path so test files can import api_helpers ──────────
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "framework"))


def pytest_configure(config):
    config.addinivalue_line("markers", "baseline: capture baseline responses")
    config.addinivalue_line("markers", "regression: compare against baseline")
