import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "baseline: capture baseline responses")
    config.addinivalue_line("markers", "regression: compare against baseline")

