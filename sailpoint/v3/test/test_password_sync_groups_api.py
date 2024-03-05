# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.api.password_sync_groups_api import PasswordSyncGroupsApi


class TestPasswordSyncGroupsApi(unittest.TestCase):
    """PasswordSyncGroupsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PasswordSyncGroupsApi()

    def tearDown(self) -> None:
        pass

    def test_create_password_sync_group(self) -> None:
        """Test case for create_password_sync_group

        Create Password Sync Group
        """
        pass

    def test_delete_password_sync_group(self) -> None:
        """Test case for delete_password_sync_group

        Delete Password Sync Group by ID
        """
        pass

    def test_get_password_sync_group(self) -> None:
        """Test case for get_password_sync_group

        Get Password Sync Group by ID
        """
        pass

    def test_get_password_sync_groups(self) -> None:
        """Test case for get_password_sync_groups

        Get Password Sync Group List
        """
        pass

    def test_update_password_sync_group(self) -> None:
        """Test case for update_password_sync_group

        Update Password Sync Group by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
