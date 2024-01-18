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

from sailpoint.v3.models.sod_violation_context_conflicting_access_criteria_left_criteria import SodViolationContextConflictingAccessCriteriaLeftCriteria


class TestSodViolationContextConflictingAccessCriteriaLeftCriteria(
        unittest.TestCase):
    """SodViolationContextConflictingAccessCriteriaLeftCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> SodViolationContextConflictingAccessCriteriaLeftCriteria:
        """Test SodViolationContextConflictingAccessCriteriaLeftCriteria
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodViolationContextConflictingAccessCriteriaLeftCriteria`
        """
        model = SodViolationContextConflictingAccessCriteriaLeftCriteria()
        if include_optional:
            return SodViolationContextConflictingAccessCriteriaLeftCriteria(
                criteria_list = [
                    sailpoint.v3.models.sod_exempt_criteria.SodExemptCriteria(
                        existing = True, 
                        type = 'IDENTITY', 
                        id = '2c918085771e9d3301773b3cb66f6398', 
                        name = 'My HR Entitlement', )
                    ]
            )
        else:
            return SodViolationContextConflictingAccessCriteriaLeftCriteria(
        )
        """

    def testSodViolationContextConflictingAccessCriteriaLeftCriteria(self):
        """Test SodViolationContextConflictingAccessCriteriaLeftCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
