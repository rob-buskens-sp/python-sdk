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

from sailpoint.beta.models.approval import Approval

class TestApproval(unittest.TestCase):
    """Approval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Approval:
        """Test Approval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Approval`
        """
        model = Approval()
        if include_optional:
            return Approval(
                approval_id = '38453251-6be2-5f8f-df93-5ce19e295837',
                approvers = [
                    sailpoint.beta.models.approval_identity.ApprovalIdentity(
                        id = '85d173e7d57e496569df763231d6deb6a', 
                        type = 'IDENTITY', 
                        name = 'John Doe', )
                    ],
                created_date = '2023-04-12T23:20:50.52Z',
                type = 'ENTITLEMENT_DESCRIPTIONS',
                name = [
                    sailpoint.beta.models.approval_name.ApprovalName(
                        value = 'Audit DB Access', 
                        locale = 'en_US', )
                    ],
                batch_request = {batchId=38453251-6be2-5f8f-df93-5ce19e295837, batchSize=100},
                description = [
                    sailpoint.beta.models.approval_description.ApprovalDescription(
                        value = 'This access allows viewing and editing of workflow resource', 
                        locale = 'en_US', )
                    ],
                priority = 'HIGH',
                requester = {id=85d173e7d57e496569df763231d6deb6a, type=IDENTITY, name=John Doe},
                comments = [
                    sailpoint.beta.models.approval_comment.ApprovalComment(
                        author = sailpoint.beta.models.approval_identity.ApprovalIdentity(
                            id = '85d173e7d57e496569df763231d6deb6a', 
                            type = 'IDENTITY', 
                            name = 'John Doe', ), 
                        comment = 'Looks good', 
                        created_date = '2023-04-12T23:20:50.52Z', )
                    ],
                approved_by = [
                    sailpoint.beta.models.approval_identity.ApprovalIdentity(
                        id = '85d173e7d57e496569df763231d6deb6a', 
                        type = 'IDENTITY', 
                        name = 'John Doe', )
                    ],
                rejected_by = [
                    sailpoint.beta.models.approval_identity.ApprovalIdentity(
                        id = '85d173e7d57e496569df763231d6deb6a', 
                        type = 'IDENTITY', 
                        name = 'John Doe', )
                    ],
                completed_date = '2023-04-12T23:20:50.52Z',
                approval_criteria = 'SINGLE',
                status = 'PENDING',
                additional_attributes = '{ "llm_description": "generated description" }',
                reference_data = [
                    sailpoint.beta.models.approval_reference.ApprovalReference(
                        id = '64012350-8fd9-4f6c-a170-1fe123683899', 
                        type = 'AccessRequestId', )
                    ]
            )
        else:
            return Approval(
        )
        """

    def testApproval(self):
        """Test Approval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
