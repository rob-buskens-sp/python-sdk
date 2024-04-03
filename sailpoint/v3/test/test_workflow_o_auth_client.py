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

from sailpoint.v3.models.workflow_o_auth_client import WorkflowOAuthClient

class TestWorkflowOAuthClient(unittest.TestCase):
    """WorkflowOAuthClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowOAuthClient:
        """Test WorkflowOAuthClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowOAuthClient`
        """
        model = WorkflowOAuthClient()
        if include_optional:
            return WorkflowOAuthClient(
                id = '1a58c03a6bf64dc2876f6988c6e2c7b7',
                secret = '00cc24a7fe810fe06a7cb38bc168ae104d703c7abb296f9944dc68e69ddb578b',
                url = 'https://tenant.api.identitynow.com/beta/workflows/execute/external/c17bea3a-574d-453c-9e04-4365fbf5af0b'
            )
        else:
            return WorkflowOAuthClient(
        )
        """

    def testWorkflowOAuthClient(self):
        """Test WorkflowOAuthClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
