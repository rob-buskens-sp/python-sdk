# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.beta.api.roles_api import RolesApi


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RolesApi()

    def tearDown(self) -> None:
        pass

    def test_bulk_delete_roles(self) -> None:
        """Test case for bulk_delete_roles

        Delete Role(s)
        """
        pass

    def test_create_role(self) -> None:
        """Test case for create_role

        Create a Role
        """
        pass

    def test_delete_role(self) -> None:
        """Test case for delete_role

        Delete a Role
        """
        pass

    def test_get_role(self) -> None:
        """Test case for get_role

        Get a Role
        """
        pass

    def test_get_role_assigned_identities(self) -> None:
        """Test case for get_role_assigned_identities

        Identities assigned a Role
        """
        pass

    def test_list_roles(self) -> None:
        """Test case for list_roles

        List Roles
        """
        pass

    def test_patch_role(self) -> None:
        """Test case for patch_role

        Patch a specified Role
        """
        pass


if __name__ == '__main__':
    unittest.main()
