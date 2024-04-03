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

from sailpoint.v3.models.create_external_execute_workflow200_response import CreateExternalExecuteWorkflow200Response

class TestCreateExternalExecuteWorkflow200Response(unittest.TestCase):
    """CreateExternalExecuteWorkflow200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateExternalExecuteWorkflow200Response:
        """Test CreateExternalExecuteWorkflow200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateExternalExecuteWorkflow200Response`
        """
        model = CreateExternalExecuteWorkflow200Response()
        if include_optional:
            return CreateExternalExecuteWorkflow200Response(
                workflow_execution_id = '0e11cefa-96e7-4b67-90d0-065bc1da5753',
                message = 'Workflow was not executed externally. Check enabled flag on workflow definition'
            )
        else:
            return CreateExternalExecuteWorkflow200Response(
        )
        """

    def testCreateExternalExecuteWorkflow200Response(self):
        """Test CreateExternalExecuteWorkflow200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
