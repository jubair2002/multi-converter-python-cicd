"""Unit tests for application configuration."""

import pytest
from backend.config import Config


@pytest.mark.unit
class TestConfig:
    """Test Config class."""

    def test_secret_key_exists(self):
        """SECRET_KEY is set and non-empty."""
        assert hasattr(Config, "SECRET_KEY")
        assert Config.SECRET_KEY is not None
        assert len(Config.SECRET_KEY) > 0

    def test_debug_is_bool(self):
        """DEBUG is a boolean."""
        assert hasattr(Config, "DEBUG")
        assert isinstance(Config.DEBUG, bool)

    def test_host_is_string(self):
        """HOST is a string."""
        assert hasattr(Config, "HOST")
        assert isinstance(Config.HOST, str)
        assert len(Config.HOST) > 0

    def test_port_is_int(self):
        """PORT is an integer in valid range."""
        assert hasattr(Config, "PORT")
        assert isinstance(Config.PORT, int)
        assert 1 <= Config.PORT <= 65535
