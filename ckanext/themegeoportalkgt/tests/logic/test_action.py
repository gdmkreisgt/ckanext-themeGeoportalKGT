"""Tests for action.py."""

import pytest

import ckan.tests.helpers as test_helpers


@pytest.mark.ckan_config("ckan.plugins", "themegeoportalkgt")
@pytest.mark.usefixtures("with_plugins")
def test_themegeoportalkgt_get_sum():
    result = test_helpers.call_action(
        "themegeoportalkgt_get_sum", left=10, right=30)
    assert result["sum"] == 40
