# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.connector_rule_management_api import ConnectorRuleManagementApi


class TestConnectorRuleManagementApi(unittest.TestCase):
    """ConnectorRuleManagementApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorRuleManagementApi()

    def tearDown(self) -> None:
        pass

    def test_create_connector_rule(self) -> None:
        """Test case for create_connector_rule

        Create Connector Rule
        """
        pass

    def test_delete_connector_rule(self) -> None:
        """Test case for delete_connector_rule

        Delete a Connector-Rule
        """
        pass

    def test_get_connector_rule(self) -> None:
        """Test case for get_connector_rule

        Connector-Rule by ID
        """
        pass

    def test_get_connector_rule_list(self) -> None:
        """Test case for get_connector_rule_list

        List Connector Rules
        """
        pass

    def test_update_connector_rule(self) -> None:
        """Test case for update_connector_rule

        Update a Connector Rule
        """
        pass

    def test_validate_connector_rule(self) -> None:
        """Test case for validate_connector_rule

        Validate Connector Rule
        """
        pass


if __name__ == '__main__':
    unittest.main()
