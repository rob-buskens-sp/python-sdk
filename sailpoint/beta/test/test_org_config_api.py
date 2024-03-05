# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.org_config_api import OrgConfigApi


class TestOrgConfigApi(unittest.TestCase):
    """OrgConfigApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrgConfigApi()

    def tearDown(self) -> None:
        pass

    def test_get_org_config(self) -> None:
        """Test case for get_org_config

        Get Org configuration settings
        """
        pass

    def test_get_valid_time_zones(self) -> None:
        """Test case for get_valid_time_zones

        Get list of time zones
        """
        pass

    def test_patch_org_config(self) -> None:
        """Test case for patch_org_config

        Patch an Org configuration property
        """
        pass


if __name__ == '__main__':
    unittest.main()
