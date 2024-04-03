# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.work_reassignment_api import WorkReassignmentApi


class TestWorkReassignmentApi(unittest.TestCase):
    """WorkReassignmentApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkReassignmentApi()

    def tearDown(self) -> None:
        pass

    def test_create_reassignment_configuration(self) -> None:
        """Test case for create_reassignment_configuration

        Create a Reassignment Configuration
        """
        pass

    def test_delete_reassignment_configuration(self) -> None:
        """Test case for delete_reassignment_configuration

        Delete Reassignment Configuration
        """
        pass

    def test_get_evaluate_reassignment_configuration(self) -> None:
        """Test case for get_evaluate_reassignment_configuration

        Evaluate Reassignment Configuration
        """
        pass

    def test_get_reassignment_config_types(self) -> None:
        """Test case for get_reassignment_config_types

        List Reassignment Config Types
        """
        pass

    def test_get_reassignment_configuration(self) -> None:
        """Test case for get_reassignment_configuration

        Get Reassignment Configuration
        """
        pass

    def test_get_tenant_config_configuration(self) -> None:
        """Test case for get_tenant_config_configuration

        Get Tenant-wide Reassignment Configuration settings
        """
        pass

    def test_list_reassignment_configurations(self) -> None:
        """Test case for list_reassignment_configurations

        List Reassignment Configurations
        """
        pass

    def test_put_reassignment_config(self) -> None:
        """Test case for put_reassignment_config

        Update Reassignment Configuration
        """
        pass

    def test_put_tenant_configuration(self) -> None:
        """Test case for put_tenant_configuration

        Update Tenant-wide Reassignment Configuration settings
        """
        pass


if __name__ == '__main__':
    unittest.main()
