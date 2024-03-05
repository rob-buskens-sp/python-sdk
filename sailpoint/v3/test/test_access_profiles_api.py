# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.api.access_profiles_api import AccessProfilesApi


class TestAccessProfilesApi(unittest.TestCase):
    """AccessProfilesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccessProfilesApi()

    def tearDown(self) -> None:
        pass

    def test_create_access_profile(self) -> None:
        """Test case for create_access_profile

        Create an Access Profile
        """
        pass

    def test_delete_access_profile(self) -> None:
        """Test case for delete_access_profile

        Delete the specified Access Profile
        """
        pass

    def test_delete_access_profiles_in_bulk(self) -> None:
        """Test case for delete_access_profiles_in_bulk

        Delete Access Profile(s)
        """
        pass

    def test_get_access_profile(self) -> None:
        """Test case for get_access_profile

        Get an Access Profile
        """
        pass

    def test_get_access_profile_entitlements(self) -> None:
        """Test case for get_access_profile_entitlements

        List Access Profile's Entitlements
        """
        pass

    def test_list_access_profiles(self) -> None:
        """Test case for list_access_profiles

        List Access Profiles
        """
        pass

    def test_patch_access_profile(self) -> None:
        """Test case for patch_access_profile

        Patch a specified Access Profile
        """
        pass


if __name__ == '__main__':
    unittest.main()
