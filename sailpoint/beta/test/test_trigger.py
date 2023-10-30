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

from beta.models.trigger import Trigger  # noqa: E501

class TestTrigger(unittest.TestCase):
    """Trigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Trigger:
        """Test Trigger
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Trigger`
        """
        model = Trigger()  # noqa: E501
        if include_optional:
            return Trigger(
                id = 'idn:access-request-dynamic-approver',
                name = 'Access Request Dynamic Approver',
                type = 'FIRE_AND_FORGET',
                description = 'Trigger for getting a dynamic approver.',
                input_schema = '{"definitions":{"record:AccessRequestDynamicApproverInput":{"type":"object","required":["accessRequestId","requestedFor","requestedItems","requestedBy"],"additionalProperties":true,"properties":{"accessRequestId":{"type":"string"},"requestedFor":{"$ref":"#/definitions/record:requestedForIdentityRef"},"requestedItems":{"type":"array","items":{"$ref":"#/definitions/record:requestedObjectRef"}},"requestedBy":{"$ref":"#/definitions/record:requestedByIdentityRef"}}},"record:requestedForIdentityRef":{"type":"object","required":["id","name","type"],"additionalProperties":true,"properties":{"id":{"type":"string"},"name":{"type":"string"},"type":{"type":"string"}}},"record:requestedObjectRef":{"type":"object","optional":["description","comment"],"required":["id","name","type","operation"],"additionalProperties":true,"properties":{"id":{"type":"string"},"name":{"type":"string"},"description":{"oneOf":[{"type":"null"},{"type":"string"}]},"type":{"type":"string"},"operation":{"type":"string"},"comment":{"oneOf":[{"type":"null"},{"type":"string"}]}}},"record:requestedByIdentityRef":{"type":"object","required":["type","id","name"],"additionalProperties":true,"properties":{"type":{"type":"string"},"id":{"type":"string"},"name":{"type":"string"}}}},"$ref":"#/definitions/record:AccessRequestDynamicApproverInput"}',
                example_input = None,
                output_schema = '{"definitions":{"record:AccessRequestDynamicApproverOutput":{"type":["null","object"],"required":["id","name","type"],"additionalProperties":true,"properties":{"id":{"type":"string"},"name":{"type":"string"},"type":{"type":"string"}}}},"$ref":"#/definitions/record:AccessRequestDynamicApproverOutput"}',
                example_output = None
            )
        else:
            return Trigger(
                id = 'idn:access-request-dynamic-approver',
                name = 'Access Request Dynamic Approver',
                type = 'FIRE_AND_FORGET',
                input_schema = '{"definitions":{"record:AccessRequestDynamicApproverInput":{"type":"object","required":["accessRequestId","requestedFor","requestedItems","requestedBy"],"additionalProperties":true,"properties":{"accessRequestId":{"type":"string"},"requestedFor":{"$ref":"#/definitions/record:requestedForIdentityRef"},"requestedItems":{"type":"array","items":{"$ref":"#/definitions/record:requestedObjectRef"}},"requestedBy":{"$ref":"#/definitions/record:requestedByIdentityRef"}}},"record:requestedForIdentityRef":{"type":"object","required":["id","name","type"],"additionalProperties":true,"properties":{"id":{"type":"string"},"name":{"type":"string"},"type":{"type":"string"}}},"record:requestedObjectRef":{"type":"object","optional":["description","comment"],"required":["id","name","type","operation"],"additionalProperties":true,"properties":{"id":{"type":"string"},"name":{"type":"string"},"description":{"oneOf":[{"type":"null"},{"type":"string"}]},"type":{"type":"string"},"operation":{"type":"string"},"comment":{"oneOf":[{"type":"null"},{"type":"string"}]}}},"record:requestedByIdentityRef":{"type":"object","required":["type","id","name"],"additionalProperties":true,"properties":{"type":{"type":"string"},"id":{"type":"string"},"name":{"type":"string"}}}},"$ref":"#/definitions/record:AccessRequestDynamicApproverInput"}',
                example_input = None,
        )
        """

    def testTrigger(self):
        """Test Trigger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
