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

from sailpoint.beta.models.sod_violation_context1_conflicting_access_criteria_left_criteria import SodViolationContext1ConflictingAccessCriteriaLeftCriteria


class TestSodViolationContext1ConflictingAccessCriteriaLeftCriteria(
        unittest.TestCase):
    """SodViolationContext1ConflictingAccessCriteriaLeftCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> SodViolationContext1ConflictingAccessCriteriaLeftCriteria:
        """Test SodViolationContext1ConflictingAccessCriteriaLeftCriteria
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodViolationContext1ConflictingAccessCriteriaLeftCriteria`
        """
        model = SodViolationContext1ConflictingAccessCriteriaLeftCriteria()
        if include_optional:
            return SodViolationContext1ConflictingAccessCriteriaLeftCriteria(
                criteria_list = [
                    sailpoint.beta.models.sod_exempt_criteria_1.SodExemptCriteria_1(
                        existing = True, 
                        type = 'IDENTITY', 
                        id = '2c918085771e9d3301773b3cb66f6398', 
                        name = 'My HR Entitlement', )
                    ]
            )
        else:
            return SodViolationContext1ConflictingAccessCriteriaLeftCriteria(
        )
        """

    def testSodViolationContext1ConflictingAccessCriteriaLeftCriteria(self):
        """Test SodViolationContext1ConflictingAccessCriteriaLeftCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
