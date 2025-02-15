# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.import_form_definitions202_response import ImportFormDefinitions202Response

class TestImportFormDefinitions202Response(unittest.TestCase):
    """ImportFormDefinitions202Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportFormDefinitions202Response:
        """Test ImportFormDefinitions202Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportFormDefinitions202Response`
        """
        model = ImportFormDefinitions202Response()
        if include_optional:
            return ImportFormDefinitions202Response(
                errors = [
                    sailpoint.beta.models.import_form_definitions_202_response_errors_inner.importFormDefinitions_202_response_errors_inner(
                        detail = {
                            'key' : None
                            }, 
                        key = '', 
                        text = '', )
                    ],
                imported_objects = [
                    sailpoint.beta.models.export_form_definitions_by_tenant_200_response_inner.exportFormDefinitionsByTenant_200_response_inner(
                        object = sailpoint.beta.models.form_definition_response.FormDefinitionResponse(
                            id = '00000000-0000-0000-0000-000000000000', 
                            name = 'My form', 
                            description = 'My form description', 
                            owner = sailpoint.beta.models.form_owner.FormOwner(
                                type = 'IDENTITY', 
                                id = '00000000-0000-0000-0000-000000000000', ), 
                            used_by = [
                                sailpoint.beta.models.form_used_by.FormUsedBy(
                                    type = 'WORKFLOW', 
                                    id = '00000000-0000-0000-0000-000000000000', )
                                ], 
                            form_input = [
                                sailpoint.beta.models.form_definition_input.FormDefinitionInput(
                                    id = '00000000-0000-0000-0000-000000000000', 
                                    type = 'STRING', 
                                    label = 'input1', 
                                    description = 'A single dynamic scalar value (i.e. number, string, date, etc.) that can be passed into the form for use in conditional logic', )
                                ], 
                            form_elements = [
                                sailpoint.beta.models.form_element.FormElement(
                                    id = '00000000-0000-0000-0000-000000000000', 
                                    element_type = 'TEXT', 
                                    config = {label=Department}, 
                                    key = 'department', 
                                    validations = [{validationType=REQUIRED}], )
                                ], 
                            form_conditions = [
                                sailpoint.beta.models.form_condition.FormCondition(
                                    rule_operator = 'AND', 
                                    rules = [
                                        sailpoint.beta.models.condition_rule.ConditionRule(
                                            source_type = 'ELEMENT', 
                                            source = 'department', 
                                            operator = 'EQ', 
                                            value_type = 'STRING', 
                                            value = Engineering, )
                                        ], 
                                    effects = [
                                        sailpoint.beta.models.condition_effect.ConditionEffect(
                                            effect_type = 'HIDE', 
                                            config = sailpoint.beta.models.condition_effect_config.ConditionEffect_config(
                                                default_value_label = 'Access to Remove', 
                                                element = '8110662963316867', ), )
                                        ], )
                                ], 
                            created = '2023-07-12T20:14:57.744860Z', 
                            modified = '2023-07-12T20:14:57.744860Z', ), 
                        self = '', 
                        version = 56, )
                    ],
                infos = [
                    sailpoint.beta.models.import_form_definitions_202_response_errors_inner.importFormDefinitions_202_response_errors_inner(
                        detail = {
                            'key' : None
                            }, 
                        key = '', 
                        text = '', )
                    ],
                warnings = [
                    sailpoint.beta.models.import_form_definitions_202_response_errors_inner.importFormDefinitions_202_response_errors_inner(
                        detail = {
                            'key' : None
                            }, 
                        key = '', 
                        text = '', )
                    ]
            )
        else:
            return ImportFormDefinitions202Response(
        )
        """

    def testImportFormDefinitions202Response(self):
        """Test ImportFormDefinitions202Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
