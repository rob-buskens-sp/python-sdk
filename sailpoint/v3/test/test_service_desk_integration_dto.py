# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.v3.models.service_desk_integration_dto import ServiceDeskIntegrationDto


class TestServiceDeskIntegrationDto(unittest.TestCase):
    """ServiceDeskIntegrationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceDeskIntegrationDto:
        """Test ServiceDeskIntegrationDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceDeskIntegrationDto`
        """
        model = ServiceDeskIntegrationDto()
        if include_optional:
            return ServiceDeskIntegrationDto(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z',
                description = 'A very nice Service Desk integration',
                type = 'ServiceNowSDIM',
                owner_ref = sailpoint.v3.models.service_desk_integration_dto_all_of_owner_ref.ServiceDeskIntegrationDto_allOf_ownerRef(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', ),
                cluster_ref = sailpoint.v3.models.source_cluster_dto.SourceClusterDto(
                    type = 'CLUSTER', 
                    id = '2c9180847a7fccdd017aa5896f9f4f6f', 
                    name = 'Training VA', ),
                cluster = 'xyzzy999',
                managed_sources = [2c9180835d191a86015d28455b4a2329, 2c5680835d191a85765d28455b4a9823],
                provisioning_config = sailpoint.v3.models.provisioning_config.ProvisioningConfig(
                    universal_manager = True, 
                    managed_resource_refs = [{type=SOURCE, id=2c9180855d191c59015d291ceb051111, name=My Source 1}, {type=SOURCE, id=2c9180855d191c59015d291ceb052222, name=My Source 2}], 
                    plan_initializer_script = sailpoint.v3.models.provisioning_config_plan_initializer_script.ProvisioningConfig_planInitializerScript(
                        source = '<?xml version='1.0' encoding='UTF-8'?>\r\n<!DOCTYPE Rule PUBLIC \"sailpoint.dtd\" \"sailpoint.dtd\">\r\n<Rule name=\"Example Rule\" type=\"BeforeProvisioning\">\r\n  <Description>Before Provisioning Rule which changes disables and enables to a modify.</Description>\r\n  <Source><![CDATA[\r\nimport sailpoint.object.*;\r\nimport sailpoint.object.ProvisioningPlan.AccountRequest;\r\nimport sailpoint.object.ProvisioningPlan.AccountRequest.Operation;\r\nimport sailpoint.object.ProvisioningPlan.AttributeRequest;\r\nimport sailpoint.object.ProvisioningPlan;\r\nimport sailpoint.object.ProvisioningPlan.Operation;\r\n\r\nfor ( AccountRequest accountRequest : plan.getAccountRequests() ) {\r\n  if ( accountRequest.getOp().equals( ProvisioningPlan.ObjectOperation.Disable ) ) {\r\n    accountRequest.setOp( ProvisioningPlan.ObjectOperation.Modify );\r\n  }\r\n  if ( accountRequest.getOp().equals( ProvisioningPlan.ObjectOperation.Enable ) ) {\r\n    accountRequest.setOp( ProvisioningPlan.ObjectOperation.Modify );\r\n  }\r\n}\r\n\r\n  ]]></Source>
', ), 
                    no_provisioning_requests = True, 
                    provisioning_request_expiration = 7, ),
                attributes = {property=value, key=value},
                before_provisioning_rule = sailpoint.v3.models.before_provisioning_rule_dto.BeforeProvisioningRuleDto(
                    type = 'RULE', 
                    id = '048eb3d55c5a4758bd07dccb87741c78', 
                    name = 'Before Provisioning Airtable Rule', )
            )
        else:
            return ServiceDeskIntegrationDto(
                name = 'aName',
                description = 'A very nice Service Desk integration',
                type = 'ServiceNowSDIM',
                attributes = {property=value, key=value},
        )
        """

    def testServiceDeskIntegrationDto(self):
        """Test ServiceDeskIntegrationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
