# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.v3.api.identity_profiles_api import IdentityProfilesApi


class TestIdentityProfilesApi(unittest.TestCase):
    """IdentityProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentityProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_identity_profile(self) -> None:
        """Test case for delete_identity_profile

        Delete an Identity Profile
        """
        pass

    def test_delete_identity_profiles(self) -> None:
        """Test case for delete_identity_profiles

        Delete Identity Profiles
        """
        pass

    def test_export_identity_profiles(self) -> None:
        """Test case for export_identity_profiles

        Export Identity Profiles
        """
        pass

    def test_get_default_identity_attribute_config(self) -> None:
        """Test case for get_default_identity_attribute_config

        Get default Identity Attribute Config
        """
        pass

    def test_get_identity_profile(self) -> None:
        """Test case for get_identity_profile

        Get single Identity Profile
        """
        pass

    def test_import_identity_profiles(self) -> None:
        """Test case for import_identity_profiles

        Import Identity Profiles
        """
        pass

    def test_list_identity_profiles(self) -> None:
        """Test case for list_identity_profiles

        Identity Profiles List
        """
        pass

    def test_sync_identity_profile(self) -> None:
        """Test case for sync_identity_profile

        Process identities under profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
