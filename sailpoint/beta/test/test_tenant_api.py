# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.tenant_api import TenantApi


class TestTenantApi(unittest.TestCase):
    """TenantApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TenantApi()

    def tearDown(self) -> None:
        pass

    def test_get_tenant(self) -> None:
        """Test case for get_tenant

        Get Tenant Information.
        """
        pass


if __name__ == '__main__':
    unittest.main()
