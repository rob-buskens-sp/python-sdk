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

from sailpoint.beta.models.violation_prediction import ViolationPrediction

class TestViolationPrediction(unittest.TestCase):
    """ViolationPrediction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ViolationPrediction:
        """Test ViolationPrediction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ViolationPrediction`
        """
        model = ViolationPrediction()
        if include_optional:
            return ViolationPrediction(
                violation_contexts = [
                    sailpoint.beta.models.violation_context.ViolationContext(
                        policy = sailpoint.beta.models.violation_context_policy.ViolationContext_policy(
                            type = ENTITLEMENT, ), 
                        conflicting_access_criteria = sailpoint.beta.models.exception_access_criteria.ExceptionAccessCriteria(
                            left_criteria = sailpoint.beta.models.exception_criteria.ExceptionCriteria(
                                criteria_list = [{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66, existing=true}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67, existing=false}], ), 
                            right_criteria = sailpoint.beta.models.exception_criteria.ExceptionCriteria(
                                criteria_list = [{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66, existing=true}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67, existing=false}], ), ), )
                    ]
            )
        else:
            return ViolationPrediction(
        )
        """

    def testViolationPrediction(self):
        """Test ViolationPrediction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
