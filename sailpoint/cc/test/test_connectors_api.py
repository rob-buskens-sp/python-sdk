# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.cc.api.connectors_api import ConnectorsApi


class TestConnectorsApi(unittest.TestCase):
    """ConnectorsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConnectorsApi()

    def tearDown(self) -> None:
        pass

    def test_create_connector(self) -> None:
        """Test case for create_connector

        Create Connector
        """
        pass

    def test_delete_connector(self) -> None:
        """Test case for delete_connector

        Delete Connector
        """
        pass

    def test_export_connector_config(self) -> None:
        """Test case for export_connector_config

        Export Connector Config
        """
        pass

    def test_import_connector_config(self) -> None:
        """Test case for import_connector_config

        Import Connector Config
        """
        pass

    def test_list_connectors(self) -> None:
        """Test case for list_connectors

        List Connectors
        """
        pass


if __name__ == '__main__':
    unittest.main()
