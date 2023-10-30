# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from beta.models.list_form_definitions_by_tenant_response import ListFormDefinitionsByTenantResponse  # noqa: E501

class TestListFormDefinitionsByTenantResponse(unittest.TestCase):
    """ListFormDefinitionsByTenantResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListFormDefinitionsByTenantResponse:
        """Test ListFormDefinitionsByTenantResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFormDefinitionsByTenantResponse`
        """
        model = ListFormDefinitionsByTenantResponse()  # noqa: E501
        if include_optional:
            return ListFormDefinitionsByTenantResponse(
                count = 1,
                results = [
                    beta.models.form_definition_response.FormDefinitionResponse(
                        id = '00000000-0000-0000-0000-000000000000', 
                        name = 'My form', 
                        description = 'My form description', 
                        owner = beta.models.form_owner.FormOwner(
                            type = 'IDENTITY', 
                            id = '00000000-0000-0000-0000-000000000000', ), 
                        used_by = [
                            beta.models.form_used_by.FormUsedBy(
                                type = 'WORKFLOW', 
                                id = '00000000-0000-0000-0000-000000000000', )
                            ], 
                        form_input = [
                            beta.models.form_definition_input.FormDefinitionInput(
                                id = '00000000-0000-0000-0000-000000000000', 
                                type = 'STRING', 
                                label = 'input1', 
                                description = 'A single dynamic scalar value (i.e. number, string, date, etc.) that can be passed into the form for use in conditional logic', )
                            ], 
                        form_elements = [
                            beta.models.form_element.FormElement(
                                id = '00000000-0000-0000-0000-000000000000', 
                                element_type = 'TEXT', 
                                config = {label=Department}, 
                                key = 'department', 
                                validations = [{validationType=REQUIRED}], )
                            ], 
                        form_conditions = [
                            beta.models.form_condition.FormCondition(
                                rule_operator = 'AND', 
                                rules = [
                                    beta.models.condition_rule.ConditionRule(
                                        source_type = 'ELEMENT', 
                                        source = 'department', 
                                        operator = 'EQ', 
                                        value_type = 'STRING', 
                                        value = Engineering, )
                                    ], 
                                effects = [
                                    beta.models.condition_effect.ConditionEffect(
                                        effect_type = 'HIDE', 
                                        config = beta.models.condition_effect_config.ConditionEffect_config(
                                            default_value_label = 'Access to Remove', 
                                            element = '8110662963316867', ), )
                                    ], )
                            ], 
                        created = '2023-07-12T20:14:57.744860Z', 
                        modified = '2023-07-12T20:14:57.744860Z', )
                    ]
            )
        else:
            return ListFormDefinitionsByTenantResponse(
        )
        """

    def testListFormDefinitionsByTenantResponse(self):
        """Test ListFormDefinitionsByTenantResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
