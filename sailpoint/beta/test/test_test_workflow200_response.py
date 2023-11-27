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

from sailpoint.beta.models.test_workflow200_response import TestWorkflow200Response  # noqa: E501


class TestTestWorkflow200Response(unittest.TestCase):
    """TestWorkflow200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TestWorkflow200Response:
        """Test TestWorkflow200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TestWorkflow200Response`
        """
        model = TestWorkflow200Response()  # noqa: E501
        if include_optional:
            return TestWorkflow200Response(
                workflow_execution_id = '0e11cefa-96e7-4b67-90d0-065bc1da5753'
            )
        else:
            return TestWorkflow200Response(
        )
        """

    def testTestWorkflow200Response(self):
        """Test TestWorkflow200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
