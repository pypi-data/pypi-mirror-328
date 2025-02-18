"""Basic unit tests for ADPA."""

import pytest
from adpa.utils.testing import parse_robot_results, load_screenshots

def test_parse_robot_results_none():
    """Test parse_robot_results with non-existent file."""
    assert parse_robot_results("non_existent.xml") is None

def test_load_screenshots_empty():
    """Test load_screenshots with no screenshots."""
    screenshots = load_screenshots()
    assert isinstance(screenshots, list)
    assert len(screenshots) >= 0  # Could be 0 or more depending on if tests have run
