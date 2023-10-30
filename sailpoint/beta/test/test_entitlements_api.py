# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from beta.api.entitlements_api import EntitlementsApi  # noqa: E501


class TestEntitlementsApi(unittest.TestCase):
    """EntitlementsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EntitlementsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_entitlement(self) -> None:
        """Test case for get_entitlement

        Get an entitlement  # noqa: E501
        """
        pass

    def test_get_entitlement_request_config(self) -> None:
        """Test case for get_entitlement_request_config

        Get Entitlement Request Config  # noqa: E501
        """
        pass

    def test_list_entitlement_children(self) -> None:
        """Test case for list_entitlement_children

        List of entitlements children  # noqa: E501
        """
        pass

    def test_list_entitlement_parents(self) -> None:
        """Test case for list_entitlement_parents

        List of entitlements parents  # noqa: E501
        """
        pass

    def test_list_entitlements(self) -> None:
        """Test case for list_entitlements

        Gets a list of entitlements.  # noqa: E501
        """
        pass

    def test_patch_entitlement(self) -> None:
        """Test case for patch_entitlement

        Patch an entitlement  # noqa: E501
        """
        pass

    def test_put_entitlement_request_config(self) -> None:
        """Test case for put_entitlement_request_config

        Replace Entitlement Request Config  # noqa: E501
        """
        pass

    def test_update_entitlements_in_bulk(self) -> None:
        """Test case for update_entitlements_in_bulk

        Bulk update an entitlement list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
