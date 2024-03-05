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

from sailpoint.v3.models.workflow_execution_event import WorkflowExecutionEvent

class TestWorkflowExecutionEvent(unittest.TestCase):
    """WorkflowExecutionEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowExecutionEvent:
        """Test WorkflowExecutionEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowExecutionEvent`
        """
        model = WorkflowExecutionEvent()
        if include_optional:
            return WorkflowExecutionEvent(
                type = WorkflowTaskScheduled,
                timestamp = '2022-02-07T20:13:31.640618296Z',
                attributes = {}
            )
        else:
            return WorkflowExecutionEvent(
        )
        """

    def testWorkflowExecutionEvent(self):
        """Test WorkflowExecutionEvent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
