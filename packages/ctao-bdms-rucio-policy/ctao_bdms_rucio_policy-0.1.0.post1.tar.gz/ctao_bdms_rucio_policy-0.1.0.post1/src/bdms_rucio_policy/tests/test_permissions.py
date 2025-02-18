"""
Tests for permissions part of the policy package
"""

import importlib


def test_import():
    importlib.import_module("bdms_rucio_policy.permission")
