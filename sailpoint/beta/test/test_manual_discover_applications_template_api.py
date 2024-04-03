# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.manual_discover_applications_template_api import ManualDiscoverApplicationsTemplateApi


class TestManualDiscoverApplicationsTemplateApi(unittest.TestCase):
    """ManualDiscoverApplicationsTemplateApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManualDiscoverApplicationsTemplateApi()

    def tearDown(self) -> None:
        pass

    def test_get_manual_discover_applications_csv_template(self) -> None:
        """Test case for get_manual_discover_applications_csv_template

        CSV template download for discovery
        """
        pass


if __name__ == '__main__':
    unittest.main()
