#!/usr/bin/env python3
"""Parameterize a unit test """
import unittest
from parameterized import parameterized, param
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to."""

    @parameterized.expand([
        param(nested_map={"a": 1}, path=("a",)),
        param(nested_map={"a": {"b": 2}}, path=("a",)),
        param(nested_map={"a": {"b": 2}}, path=("a", "b"))
    ])
    def test_access_nested_map(self, nested_map, path):
        """test_access_nested_mapmethod to test that the method
        returns what it is supposed to"""
        access_nested_map(nested_map=nested_map, path=path)
