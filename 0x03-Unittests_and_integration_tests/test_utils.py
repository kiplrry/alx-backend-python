#!/usr/bin/env python3
"""Parameterize a unit test """
from unittest import TestCase, mock
from parameterized import parameterized, param
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
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

    @parameterized.expand([
        param(nested_map={}, path=("a",)),
        param(nested_map={"a": 1}, path=("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that a KeyError is raised for the inputs """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nested_map, path=path)


class TestGetJson(TestCase):
    """Mock HTTP calls"""

    @parameterized.expand([
        param(test_url="http://example.com", test_payload={"payload": True}),
        param(test_url="http://holberton.io", test_payload={"payload": False})
    ]
    )
    def test_get_json(self, test_url: str, test_payload: dict):
        """testing the get json method"""
        class Mocked(mock.Mock):
            """a subclass of the Mock class"""

            def json(self):
                """implementing the json method"""
                return test_payload

        with mock.patch('requests.get') as mckup:
            mckup.return_value = Mocked()
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(TestCase):
    """tests the utils.memoize decorator"""

    def test_memoize(self):
        """Testing memoization"""
        class TestClass:
            """a test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mocking:
            test = TestClass()
            self.assertEqual(test.a_property(), test.a_property())
            mocking.assert_called_once()
