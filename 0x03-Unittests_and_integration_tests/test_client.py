#!/usr/bin/env python3
"""test the client"""

from parameterized import parameterized
from unittest import mock, TestCase
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ implements client methods """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @mock.patch('client.get_json')
    def test_org(self, org, mck: mock.Mock):
        """This method test that GithubOrgClient.org returns
        the correct value."""
        gh = GithubOrgClient(org_name=org)
        di = gh.org()
        mck.assert_called_once()
