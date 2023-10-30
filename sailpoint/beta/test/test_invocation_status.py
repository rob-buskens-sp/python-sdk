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

from beta.models.invocation_status import InvocationStatus  # noqa: E501

class TestInvocationStatus(unittest.TestCase):
    """InvocationStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InvocationStatus:
        """Test InvocationStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InvocationStatus`
        """
        model = InvocationStatus()  # noqa: E501
        if include_optional:
            return InvocationStatus(
                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                trigger_id = 'idn:access-requested',
                subscription_id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                type = 'TEST',
                created = '2020-03-27T20:40:10.738Z',
                completed = '2020-03-27T20:42:14.738Z',
                start_invocation_input = beta.models.start_invocation_input.StartInvocationInput(
                    trigger_id = 'idn:access-requested', 
                    input = {identityId=201327fda1c44704ac01181e963d463c}, 
                    content_json = {workflowId=1234}, ),
                complete_invocation_input = beta.models.complete_invocation_input.CompleteInvocationInput(
                    localized_error = beta.models.localized_message.LocalizedMessage(
                        locale = 'An error has occurred!', 
                        message = 'Error has occurred!', ), 
                    output = {approved=false}, )
            )
        else:
            return InvocationStatus(
                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                trigger_id = 'idn:access-requested',
                subscription_id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                type = 'TEST',
                created = '2020-03-27T20:40:10.738Z',
                start_invocation_input = beta.models.start_invocation_input.StartInvocationInput(
                    trigger_id = 'idn:access-requested', 
                    input = {identityId=201327fda1c44704ac01181e963d463c}, 
                    content_json = {workflowId=1234}, ),
        )
        """

    def testInvocationStatus(self):
        """Test InvocationStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
