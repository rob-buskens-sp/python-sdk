# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.source_usages_api import SourceUsagesApi


class TestSourceUsagesApi(unittest.TestCase):
    """SourceUsagesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SourceUsagesApi()

    def tearDown(self) -> None:
        pass

    def test_get_status_by_source_id(self) -> None:
        """Test case for get_status_by_source_id

        Finds status of source usage
        """
        pass

    def test_get_usages_by_source_id(self) -> None:
        """Test case for get_usages_by_source_id

        Returns source usage insights
        """
        pass


if __name__ == '__main__':
    unittest.main()
