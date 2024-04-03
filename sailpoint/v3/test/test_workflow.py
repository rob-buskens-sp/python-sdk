# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.workflow import Workflow

class TestWorkflow(unittest.TestCase):
    """Workflow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Workflow:
        """Test Workflow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Workflow`
        """
        model = Workflow()
        if include_optional:
            return Workflow(
                name = 'Send Email',
                owner = sailpoint.v3.models.workflow_body_owner.WorkflowBody_owner(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                description = 'Send an email to the identity who's attributes changed.',
                definition = sailpoint.v3.models.workflow_definition.WorkflowDefinition(
                    start = 'Send Email Test', 
                    steps = {Send Email={actionId=sp:send-email, attributes={body=This is a test, from=sailpoint@sailpoint.com, recipientId.$=$.identity.id, subject=test}, nextStep=success, selectResult=null, type=ACTION}, success={type=success}}, ),
                enabled = False,
                trigger = sailpoint.v3.models.workflow_trigger.WorkflowTrigger(
                    type = 'EVENT', 
                    attributes = null, ),
                id = 'd201c5e9-d37b-4aff-af14-66414f39d569',
                execution_count = 2,
                failure_count = 0,
                created = '2022-01-10T16:06:16.636381447Z',
                creator = sailpoint.v3.models.workflow_all_of_creator.Workflow_allOf_creator(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', )
            )
        else:
            return Workflow(
        )
        """

    def testWorkflow(self):
        """Test Workflow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
