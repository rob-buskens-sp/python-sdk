# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.exception_criteria_criteria_list_inner import ExceptionCriteriaCriteriaListInner

class TestExceptionCriteriaCriteriaListInner(unittest.TestCase):
    """ExceptionCriteriaCriteriaListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExceptionCriteriaCriteriaListInner:
        """Test ExceptionCriteriaCriteriaListInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExceptionCriteriaCriteriaListInner`
        """
        model = ExceptionCriteriaCriteriaListInner()
        if include_optional:
            return ExceptionCriteriaCriteriaListInner(
                type = ENTITLEMENT,
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'CN=HelpDesk,OU=test,OU=test-service,DC=TestAD,DC=local',
                existing = True
            )
        else:
            return ExceptionCriteriaCriteriaListInner(
        )
        """

    def testExceptionCriteriaCriteriaListInner(self):
        """Test ExceptionCriteriaCriteriaListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
