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

from sailpoint.v3.models.sod_violation_check import SodViolationCheck  # noqa: E501


class TestSodViolationCheck(unittest.TestCase):
    """SodViolationCheck unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SodViolationCheck:
        """Test SodViolationCheck
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodViolationCheck`
        """
        model = SodViolationCheck()  # noqa: E501
        if include_optional:
            return SodViolationCheck(
                request_id = '089899f13a8f4da7824996191587bab9',
                created = '2020-01-01T00:00Z'
            )
        else:
            return SodViolationCheck(
                request_id = '089899f13a8f4da7824996191587bab9',
        )
        """

    def testSodViolationCheck(self):
        """Test SodViolationCheck"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
