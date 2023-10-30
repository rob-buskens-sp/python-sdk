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

from beta.models.sod_violation_context_check_completed1 import SodViolationContextCheckCompleted1  # noqa: E501

class TestSodViolationContextCheckCompleted1(unittest.TestCase):
    """SodViolationContextCheckCompleted1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SodViolationContextCheckCompleted1:
        """Test SodViolationContextCheckCompleted1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodViolationContextCheckCompleted1`
        """
        model = SodViolationContextCheckCompleted1()  # noqa: E501
        if include_optional:
            return SodViolationContextCheckCompleted1(
                state = 'SUCCESS',
                uuid = 'f73d16e9-a038-46c5-b217-1246e15fdbdd',
                violation_check_result = beta.models.sod_violation_check_result_1.SodViolationCheckResult_1(
                    message = beta.models.error_message_dto.ErrorMessageDto(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'The request was syntactically correct but its content is semantically invalid.', ), 
                    client_metadata = {requestedAppName=test-app, requestedAppId=2c91808f7892918f0178b78da4a305a1}, 
                    violation_contexts = [
                        beta.models.sod_violation_context_1.SodViolationContext_1(
                            policy = beta.models.base_reference_dto.BaseReferenceDto(
                                type = 'IDENTITY', 
                                id = '2c91808568c529c60168cca6f90c1313', 
                                name = 'William Wilson', ), 
                            conflicting_access_criteria = beta.models.sod_violation_context_1_conflicting_access_criteria.SodViolationContext_1_conflictingAccessCriteria(
                                left_criteria = beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(
                                    criteria_list = [
                                        beta.models.sod_exempt_criteria_1.SodExemptCriteria_1(
                                            existing = True, 
                                            id = '2c918085771e9d3301773b3cb66f6398', 
                                            name = 'My HR Entitlement', )
                                        ], ), 
                                right_criteria = beta.models.sod_violation_context_1_conflicting_access_criteria_left_criteria.SodViolationContext_1_conflictingAccessCriteria_leftCriteria(), ), )
                        ], 
                    violated_policies = [
                        beta.models.base_reference_dto_1.BaseReferenceDto_1(
                            id = 'ff8081814d977c21014da056804a0af3', 
                            name = 'Github', )
                        ], )
            )
        else:
            return SodViolationContextCheckCompleted1(
        )
        """

    def testSodViolationContextCheckCompleted1(self):
        """Test SodViolationContextCheckCompleted1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
