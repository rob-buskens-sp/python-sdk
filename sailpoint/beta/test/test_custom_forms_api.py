# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.beta.api.custom_forms_api import CustomFormsApi


class TestCustomFormsApi(unittest.TestCase):
    """CustomFormsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CustomFormsApi()

    def tearDown(self) -> None:
        pass

    def test_create_form_definition(self) -> None:
        """Test case for create_form_definition

        Creates a form definition.
        """
        pass

    def test_create_form_definition_dynamic_schema(self) -> None:
        """Test case for create_form_definition_dynamic_schema

        Generate JSON Schema dynamically.
        """
        pass

    def test_create_form_definition_file_request(self) -> None:
        """Test case for create_form_definition_file_request

        Upload new form definition file.
        """
        pass

    def test_create_form_instance(self) -> None:
        """Test case for create_form_instance

        Creates a form instance.
        """
        pass

    def test_delete_form_definition(self) -> None:
        """Test case for delete_form_definition

        Deletes a form definition.
        """
        pass

    def test_export_form_definitions_by_tenant(self) -> None:
        """Test case for export_form_definitions_by_tenant

        List form definitions by tenant.
        """
        pass

    def test_get_file_from_s3(self) -> None:
        """Test case for get_file_from_s3

        Download definition file by fileId.
        """
        pass

    def test_get_form_definition_by_key(self) -> None:
        """Test case for get_form_definition_by_key

        Return a form definition.
        """
        pass

    def test_get_form_instance_by_key(self) -> None:
        """Test case for get_form_instance_by_key

        Returns a form instance.
        """
        pass

    def test_get_form_instance_file(self) -> None:
        """Test case for get_form_instance_file

        Download instance file by fileId.
        """
        pass

    def test_import_form_definitions(self) -> None:
        """Test case for import_form_definitions

        Import form definitions from export.
        """
        pass

    def test_patch_form_definition(self) -> None:
        """Test case for patch_form_definition

        Patch a form definition.
        """
        pass

    def test_patch_form_instance(self) -> None:
        """Test case for patch_form_instance

        Patch a form instance.
        """
        pass

    def test_search_form_definitions_by_tenant(self) -> None:
        """Test case for search_form_definitions_by_tenant

        Export form definitions by tenant.
        """
        pass

    def test_search_form_element_data_by_element_id(self) -> None:
        """Test case for search_form_element_data_by_element_id

        Retrieves dynamic data by element.
        """
        pass

    def test_search_form_instances_by_tenant(self) -> None:
        """Test case for search_form_instances_by_tenant

        List form instances by tenant.
        """
        pass

    def test_search_pre_defined_select_options(self) -> None:
        """Test case for search_pre_defined_select_options

        List predefined select options.
        """
        pass

    def test_show_preview_data_source(self) -> None:
        """Test case for show_preview_data_source

        Preview form definition data source.
        """
        pass


if __name__ == '__main__':
    unittest.main()
