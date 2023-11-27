# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.v3.api.service_desk_integration_api import ServiceDeskIntegrationApi  # noqa: E501


class TestServiceDeskIntegrationApi(unittest.TestCase):
    """ServiceDeskIntegrationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ServiceDeskIntegrationApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_service_desk_integration(self) -> None:
        """Test case for create_service_desk_integration

        Create new Service Desk integration  # noqa: E501
        """
        pass

    def test_delete_service_desk_integration(self) -> None:
        """Test case for delete_service_desk_integration

        Delete a Service Desk integration  # noqa: E501
        """
        pass

    def test_get_service_desk_integration(self) -> None:
        """Test case for get_service_desk_integration

        Get a Service Desk integration  # noqa: E501
        """
        pass

    def test_get_service_desk_integration_template(self) -> None:
        """Test case for get_service_desk_integration_template

        Service Desk integration template by scriptName.  # noqa: E501
        """
        pass

    def test_get_service_desk_integration_types(self) -> None:
        """Test case for get_service_desk_integration_types

        Service Desk Integration Types List.  # noqa: E501
        """
        pass

    def test_get_service_desk_integrations(self) -> None:
        """Test case for get_service_desk_integrations

        List existing Service Desk Integrations  # noqa: E501
        """
        pass

    def test_get_status_check_details(self) -> None:
        """Test case for get_status_check_details

        Get the time check configuration  # noqa: E501
        """
        pass

    def test_patch_service_desk_integration(self) -> None:
        """Test case for patch_service_desk_integration

        Service Desk Integration Update PATCH  # noqa: E501
        """
        pass

    def test_put_service_desk_integration(self) -> None:
        """Test case for put_service_desk_integration

        Update a Service Desk integration  # noqa: E501
        """
        pass

    def test_update_status_check_details(self) -> None:
        """Test case for update_status_check_details

        Update the time check configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
