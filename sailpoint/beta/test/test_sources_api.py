# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.beta.api.sources_api import SourcesApi  # noqa: E501


class TestSourcesApi(unittest.TestCase):
    """SourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SourcesApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_provisioning_policy(self) -> None:
        """Test case for create_provisioning_policy

        Create Provisioning Policy  # noqa: E501
        """
        pass

    def test_create_source(self) -> None:
        """Test case for create_source

        Creates a source in IdentityNow.  # noqa: E501
        """
        pass

    def test_create_source_schema(self) -> None:
        """Test case for create_source_schema

        Creates a new Schema on the specified Source in IdentityNow.  # noqa: E501
        """
        pass

    def test_delete(self) -> None:
        """Test case for delete

        Delete Source by ID  # noqa: E501
        """
        pass

    def test_delete_native_change_detection_config(self) -> None:
        """Test case for delete_native_change_detection_config

        Delete Native Change Detection Configuration  # noqa: E501
        """
        pass

    def test_delete_provisioning_policy(self) -> None:
        """Test case for delete_provisioning_policy

        Delete Provisioning Policy by UsageType  # noqa: E501
        """
        pass

    def test_delete_source_schema(self) -> None:
        """Test case for delete_source_schema

        Delete Source Schema by ID  # noqa: E501
        """
        pass

    def test_get_native_change_detection_config(self) -> None:
        """Test case for get_native_change_detection_config

        Native Change Detection Configuration  # noqa: E501
        """
        pass

    def test_get_provisioning_policy(self) -> None:
        """Test case for get_provisioning_policy

        Get Provisioning Policy by UsageType  # noqa: E501
        """
        pass

    def test_get_source(self) -> None:
        """Test case for get_source

        Get Source by ID  # noqa: E501
        """
        pass

    def test_get_source_accounts_schema(self) -> None:
        """Test case for get_source_accounts_schema

        Downloads source accounts schema template  # noqa: E501
        """
        pass

    def test_get_source_attr_sync_config(self) -> None:
        """Test case for get_source_attr_sync_config

        Attribute Sync Config  # noqa: E501
        """
        pass

    def test_get_source_config(self) -> None:
        """Test case for get_source_config

        Gets source config with language translations  # noqa: E501
        """
        pass

    def test_get_source_entitlement_request_config(self) -> None:
        """Test case for get_source_entitlement_request_config

        Get Source Entitlement Request Configuration  # noqa: E501
        """
        pass

    def test_get_source_entitlements_schema(self) -> None:
        """Test case for get_source_entitlements_schema

        Downloads source entitlements schema template  # noqa: E501
        """
        pass

    def test_get_source_schema(self) -> None:
        """Test case for get_source_schema

        Get Source Schema by ID  # noqa: E501
        """
        pass

    def test_import_source_accounts_schema(self) -> None:
        """Test case for import_source_accounts_schema

        Uploads source accounts schema template  # noqa: E501
        """
        pass

    def test_import_source_connector_file(self) -> None:
        """Test case for import_source_connector_file

        Upload connector file to source  # noqa: E501
        """
        pass

    def test_import_source_entitlements_schema(self) -> None:
        """Test case for import_source_entitlements_schema

        Uploads source entitlements schema template  # noqa: E501
        """
        pass

    def test_list_provisioning_policies(self) -> None:
        """Test case for list_provisioning_policies

        Lists ProvisioningPolicies  # noqa: E501
        """
        pass

    def test_list_source_schemas(self) -> None:
        """Test case for list_source_schemas

        Lists the Schemas that exist on the specified Source in IdentityNow.  # noqa: E501
        """
        pass

    def test_list_sources(self) -> None:
        """Test case for list_sources

        Lists all sources in IdentityNow.  # noqa: E501
        """
        pass

    def test_peek_resource_objects(self) -> None:
        """Test case for peek_resource_objects

        Peek source connector's resource objects  # noqa: E501
        """
        pass

    def test_ping_cluster(self) -> None:
        """Test case for ping_cluster

        Ping cluster for source connector  # noqa: E501
        """
        pass

    def test_put_native_change_detection_config(self) -> None:
        """Test case for put_native_change_detection_config

        Update Native Change Detection Configuration  # noqa: E501
        """
        pass

    def test_put_provisioning_policy(self) -> None:
        """Test case for put_provisioning_policy

        Update Provisioning Policy by UsageType  # noqa: E501
        """
        pass

    def test_put_source(self) -> None:
        """Test case for put_source

        Update Source (Full)  # noqa: E501
        """
        pass

    def test_put_source_attr_sync_config(self) -> None:
        """Test case for put_source_attr_sync_config

        Update Attribute Sync Config  # noqa: E501
        """
        pass

    def test_put_source_schema(self) -> None:
        """Test case for put_source_schema

        Update Source Schema (Full)  # noqa: E501
        """
        pass

    def test_sync_attributes_for_source(self) -> None:
        """Test case for sync_attributes_for_source

        Synchronize single source attributes.  # noqa: E501
        """
        pass

    def test_test_source_configuration(self) -> None:
        """Test case for test_source_configuration

        Test configuration for source connector  # noqa: E501
        """
        pass

    def test_test_source_connection(self) -> None:
        """Test case for test_source_connection

        Check connection for source connector.  # noqa: E501
        """
        pass

    def test_update_provisioning_policies_in_bulk(self) -> None:
        """Test case for update_provisioning_policies_in_bulk

        Bulk Update Provisioning Policies  # noqa: E501
        """
        pass

    def test_update_provisioning_policy(self) -> None:
        """Test case for update_provisioning_policy

        Partial update of Provisioning Policy  # noqa: E501
        """
        pass

    def test_update_source(self) -> None:
        """Test case for update_source

        Update Source (Partial)  # noqa: E501
        """
        pass

    def test_update_source_entitlement_request_config(self) -> None:
        """Test case for update_source_entitlement_request_config

        Update Source Entitlement Request Configuration  # noqa: E501
        """
        pass

    def test_update_source_schema(self) -> None:
        """Test case for update_source_schema

        Update Source Schema (Partial)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
