"""Shared pytest configuration and markers for multiple test types."""

import pytest


def pytest_configure(config):
    """Register custom markers for test types."""
    config.addinivalue_line(
        "markers", "unit: mark test as a unit test (fast, isolated logic)"
    )
    config.addinivalue_line(
        "markers", "integration: mark test as an integration test (API/routes, DB)"
    )
    config.addinivalue_line(
        "markers", "smoke: mark test as a smoke test (critical path, run first)"
    )
