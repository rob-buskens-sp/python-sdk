# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.identity_profiles_api import IdentityProfilesApi


class TestIdentityProfilesApi(unittest.TestCase):
    """IdentityProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentityProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_create_identity_profile(self) -> None:
        """Test case for create_identity_profile

        Create an Identity Profile
        """
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

    def test_generate_identity_preview(self) -> None:
        """Test case for generate_identity_preview

        Generate Identity Profile Preview
        """
        pass

    def test_get_default_identity_attribute_config(self) -> None:
        """Test case for get_default_identity_attribute_config

        Default identity attribute config
        """
        pass

    def test_get_identity_profile(self) -> None:
        """Test case for get_identity_profile

        Gets a single Identity Profile
        """
        pass

    def test_import_identity_profiles(self) -> None:
        """Test case for import_identity_profiles

        Import Identity Profiles
        """
        pass

    def test_list_identity_profiles(self) -> None:
        """Test case for list_identity_profiles

        Identity Profiles list
        """
        pass

    def test_sync_identity_profile(self) -> None:
        """Test case for sync_identity_profile

        Process identities under profile
        """
        pass

    def test_update_identity_profile(self) -> None:
        """Test case for update_identity_profile

        Update the Identity Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
