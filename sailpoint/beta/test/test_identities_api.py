# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.identities_api import IdentitiesApi


class TestIdentitiesApi(unittest.TestCase):
    """IdentitiesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdentitiesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_identity(self) -> None:
        """Test case for delete_identity

        Deletes an identity.
        """
        pass

    def test_get_identity(self) -> None:
        """Test case for get_identity

        Identity Details
        """
        pass

    def test_get_identity_ownership_details(self) -> None:
        """Test case for get_identity_ownership_details

        Get ownership details
        """
        pass

    def test_get_role_assignment(self) -> None:
        """Test case for get_role_assignment

        Get role assignment
        """
        pass

    def test_get_role_assignments(self) -> None:
        """Test case for get_role_assignments

        Get role assignments
        """
        pass

    def test_list_identities(self) -> None:
        """Test case for list_identities

        List Identities
        """
        pass

    def test_reset_identity(self) -> None:
        """Test case for reset_identity

        Reset an identity
        """
        pass

    def test_start_identity_processing(self) -> None:
        """Test case for start_identity_processing

        Process a list of identityIds
        """
        pass

    def test_synchronize_attributes_for_identity(self) -> None:
        """Test case for synchronize_attributes_for_identity

        Attribute synchronization for single identity.
        """
        pass


if __name__ == '__main__':
    unittest.main()
