"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.themegeoportalkgt.logic import validators


def test_themegeoportalkgt_reauired_with_valid_value():
    assert validators.themegeoportalkgt_required("value") == "value"


def test_themegeoportalkgt_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.themegeoportalkgt_required(None)
