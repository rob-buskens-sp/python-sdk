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

from sailpoint.beta.models.completed_approval import CompletedApproval


class TestCompletedApproval(unittest.TestCase):
    """CompletedApproval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompletedApproval:
        """Test CompletedApproval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompletedApproval`
        """
        model = CompletedApproval()
        if include_optional:
            return CompletedApproval(
                id = '2c938083633d259901633d25c68c00fa',
                name = 'Approval Name',
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-07-25T20:22:28.104Z',
                request_created = '2017-07-11T18:45:35.098Z',
                request_type = 'GRANT_ACCESS',
                requester = sailpoint.beta.models.access_item_requester_dto.AccessItemRequesterDto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                requested_for = sailpoint.beta.models.access_item_requested_for_dto.AccessItemRequestedForDto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
                reviewed_by = sailpoint.beta.models.completed_approval_reviewed_by.CompletedApproval_reviewedBy(
                    type = 'IDENTITY', 
                    id = '2c3780a46faadee4016fb4e018c20652', 
                    name = 'Allen Albertson', ),
                owner = sailpoint.beta.models.access_item_owner_dto.AccessItemOwnerDto(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                requested_object = sailpoint.beta.models.requestable_object_reference.RequestableObjectReference(
                    id = '2c938083633d259901633d25c68c00fa', 
                    name = 'Object Name', 
                    description = 'Object Description', 
                    type = 'ROLE', ),
                requester_comment = sailpoint.beta.models.comment_dto_1.CommentDto_1(
                    comment = 'This is a comment.', 
                    created = '2017-07-11T18:45:37.098Z', ),
                reviewer_comment = sailpoint.beta.models.completed_approval_reviewer_comment.CompletedApproval_reviewerComment(),
                previous_reviewers_comments = [
                    sailpoint.beta.models.comment_dto_1.CommentDto_1(
                        comment = 'This is a comment.', 
                        created = '2017-07-11T18:45:37.098Z', )
                    ],
                forward_history = [
                    sailpoint.beta.models.approval_forward_history.ApprovalForwardHistory(
                        old_approver_name = 'Frank Mir', 
                        new_approver_name = 'Al Volta', 
                        comment = 'Forwarding from Frank to Al', 
                        modified = '2019-08-23T18:52:57.398Z', 
                        forwarder_name = 'William Wilson', 
                        reassignment_type = 'AUTOMATIC_REASSIGNMENT', )
                    ],
                comment_required_when_rejected = True,
                state = 'APPROVED',
                remove_date = '2020-07-11T00:00Z',
                remove_date_update_requested = True,
                current_remove_date = '2020-07-11T00:00Z',
                sod_violation_context = sailpoint.beta.models.sod_violation_context_check_completed_1.SodViolationContextCheckCompleted_1(
                    state = 'SUCCESS', 
                    uuid = 'f73d16e9-a038-46c5-b217-1246e15fdbdd', 
                    violation_check_result = sailpoint.beta.models.sod_violation_check_result_1.SodViolationCheckResult_1(
                        message = sailpoint.beta.models.error_message_dto.ErrorMessageDto(
                            locale = 'en-US', 
                            locale_origin = 'DEFAULT', 
                            text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                        client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                        violation_contexts = [
                            sailpoint.beta.models.sod_violation_context_1.SodViolationContext_1(
                                policy = sailpoint.beta.models.sod_policy_dto.SodPolicyDto(
                                    type = 'SOD_POLICY', 
                                    id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                    name = 'Business SOD Policy', ), 
                                conflicting_access_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria.SodViolationContext_1_conflictingAccessCriteria(
                                    left_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(
                                        criteria_list = [
                                            sailpoint.beta.models.sod_exempt_criteria_1.SodExemptCriteria_1(
                                                existing = True, 
                                                type = 'IDENTITY', 
                                                id = '2c918085771e9d3301773b3cb66f6398', 
                                                name = 'My HR Entitlement', )
                                            ], ), 
                                    right_criteria = sailpoint.beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(), ), )
                            ], 
                        violated_policies = [
                            sailpoint.beta.models.sod_policy_dto.SodPolicyDto(
                                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                name = 'Business SOD Policy', )
                            ], ), )
            )
        else:
            return CompletedApproval(
        )
        """

    def testCompletedApproval(self):
        """Test CompletedApproval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
