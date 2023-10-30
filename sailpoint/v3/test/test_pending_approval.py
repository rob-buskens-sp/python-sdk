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

from v3.models.pending_approval import PendingApproval  # noqa: E501

class TestPendingApproval(unittest.TestCase):
    """PendingApproval unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PendingApproval:
        """Test PendingApproval
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PendingApproval`
        """
        model = PendingApproval()  # noqa: E501
        if include_optional:
            return PendingApproval(
                id = 'id12345',
                name = 'aName',
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-07-25T20:22:28.104Z',
                request_created = '2017-07-11T18:45:35.098Z',
                request_type = 'GRANT_ACCESS',
                requester = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                requested_for = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                owner = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                requested_object = v3.models.requestable_object_reference.RequestableObjectReference(
                    id = '2c9180835d2e5168015d32f890ca1581', 
                    name = 'Applied Research Access', 
                    description = 'Access to research information, lab results, and schematics', 
                    type = 'ROLE', ),
                requester_comment = v3.models.comment_dto.CommentDto(
                    comment = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat', 
                    author = v3.models.comment_dto_author.CommentDto_author(
                        type = 'IDENTITY', 
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'Adam Kennedy', ), 
                    created = '2017-07-11T18:45:37.098Z', ),
                previous_reviewers_comments = [
                    v3.models.comment_dto.CommentDto(
                        comment = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat', 
                        author = v3.models.comment_dto_author.CommentDto_author(
                            type = 'IDENTITY', 
                            id = '2c91808568c529c60168cca6f90c1313', 
                            name = 'Adam Kennedy', ), 
                        created = '2017-07-11T18:45:37.098Z', )
                    ],
                forward_history = [
                    v3.models.approval_forward_history.ApprovalForwardHistory(
                        old_approver_name = 'Frank Mir', 
                        new_approver_name = 'Al Volta', 
                        comment = 'Forwarding from Frank to Al', 
                        modified = '2019-08-23T18:52:57.398Z', 
                        forwarder_name = 'William Wilson', 
                        reassignment_type = 'AUTOMATIC_REASSIGNMENT', )
                    ],
                comment_required_when_rejected = True,
                action_in_process = 'APPROVED',
                remove_date = '2020-07-11T00:00Z',
                remove_date_update_requested = True,
                current_remove_date = '2020-07-11T00:00Z',
                sod_violation_context = v3.models.sod_violation_context_check_completed.SodViolationContextCheckCompleted(
                    state = 'SUCCESS', 
                    uuid = 'f73d16e9-a038-46c5-b217-1246e15fdbdd', 
                    violation_check_result = v3.models.sod_violation_check_result.SodViolationCheckResult(
                        message = v3.models.error_message_dto.ErrorMessageDto(
                            locale = 'en-US', 
                            locale_origin = 'DEFAULT', 
                            text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                        client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                        violation_contexts = [
                            v3.models.sod_violation_context.SodViolationContext(
                                policy = v3.models.base_reference_dto.BaseReferenceDto(
                                    type = 'IDENTITY', 
                                    id = '2c91808568c529c60168cca6f90c1313', 
                                    name = 'William Wilson', ), 
                                conflicting_access_criteria = v3.models.sod_violation_context_conflicting_access_criteria.SodViolationContext_conflictingAccessCriteria(
                                    left_criteria = v3.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(
                                        criteria_list = [
                                            v3.models.sod_exempt_criteria.SodExemptCriteria(
                                                existing = True, 
                                                id = '2c918085771e9d3301773b3cb66f6398', 
                                                name = 'My HR Entitlement', )
                                            ], ), 
                                    right_criteria = v3.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(), ), )
                            ], 
                        violated_policies = [
                            v3.models.base_reference_dto.BaseReferenceDto(
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'William Wilson', )
                            ], ), )
            )
        else:
            return PendingApproval(
        )
        """

    def testPendingApproval(self):
        """Test PendingApproval"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
