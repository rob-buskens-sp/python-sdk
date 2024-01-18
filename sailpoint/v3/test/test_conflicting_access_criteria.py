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

from sailpoint.v3.models.conflicting_access_criteria import ConflictingAccessCriteria


class TestConflictingAccessCriteria(unittest.TestCase):
    """ConflictingAccessCriteria unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConflictingAccessCriteria:
        """Test ConflictingAccessCriteria
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConflictingAccessCriteria`
        """
        model = ConflictingAccessCriteria()
        if include_optional:
            return ConflictingAccessCriteria(
                left_criteria = sailpoint.v3.models.access_criteria.AccessCriteria(
                    name = 'money-in', 
                    criteria_list = [{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66, name=Administrator}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67, name=Administrator}], ),
                right_criteria = sailpoint.v3.models.access_criteria.AccessCriteria(
                    name = 'money-in', 
                    criteria_list = [{type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a66, name=Administrator}, {type=ENTITLEMENT, id=2c9180866166b5b0016167c32ef31a67, name=Administrator}], )
            )
        else:
            return ConflictingAccessCriteria(
        )
        """

    def testConflictingAccessCriteria(self):
        """Test ConflictingAccessCriteria"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
