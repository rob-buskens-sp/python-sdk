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

from sailpoint.beta.models.requested_item_status_sod_violation_context import RequestedItemStatusSodViolationContext

class TestRequestedItemStatusSodViolationContext(unittest.TestCase):
    """RequestedItemStatusSodViolationContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestedItemStatusSodViolationContext:
        """Test RequestedItemStatusSodViolationContext
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestedItemStatusSodViolationContext`
        """
        model = RequestedItemStatusSodViolationContext()
        if include_optional:
            return RequestedItemStatusSodViolationContext(
                state = 'SUCCESS',
                uuid = 'f73d16e9-a038-46c5-b217-1246e15fdbdd',
                violation_check_result = sailpoint.beta.models.sod_violation_check_result.SodViolationCheckResult(
                    message = sailpoint.beta.models.error_message_dto.ErrorMessageDto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                    client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                    violation_contexts = [
                        sailpoint.beta.models.sod_violation_context.SodViolationContext(
                            policy = sailpoint.beta.models.sod_policy_dto.SodPolicyDto(
                                type = 'SOD_POLICY', 
                                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                                name = 'Business SOD Policy', ), 
                            conflicting_access_criteria = sailpoint.beta.models.sod_violation_context_conflicting_access_criteria.SodViolationContext_conflictingAccessCriteria(
                                left_criteria = sailpoint.beta.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(
                                    criteria_list = [
                                        sailpoint.beta.models.sod_exempt_criteria.SodExemptCriteria(
                                            existing = True, 
                                            type = 'IDENTITY', 
                                            id = '2c918085771e9d3301773b3cb66f6398', 
                                            name = 'My HR Entitlement', )
                                        ], ), 
                                right_criteria = sailpoint.beta.models.sod_violation_context_conflicting_access_criteria_left_criteria.SodViolationContext_conflictingAccessCriteria_leftCriteria(), ), )
                        ], 
                    violated_policies = [
                        sailpoint.beta.models.sod_policy_dto.SodPolicyDto(
                            id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde', 
                            name = 'Business SOD Policy', )
                        ], )
            )
        else:
            return RequestedItemStatusSodViolationContext(
        )
        """

    def testRequestedItemStatusSodViolationContext(self):
        """Test RequestedItemStatusSodViolationContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
