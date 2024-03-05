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

from sailpoint.v3.models.schedule1_hours import Schedule1Hours

class TestSchedule1Hours(unittest.TestCase):
    """Schedule1Hours unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Schedule1Hours:
        """Test Schedule1Hours
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Schedule1Hours`
        """
        model = Schedule1Hours()
        if include_optional:
            return Schedule1Hours(
                type = 'LIST',
                values = [MON, WED],
                interval = 3
            )
        else:
            return Schedule1Hours(
                type = 'LIST',
                values = [MON, WED],
        )
        """

    def testSchedule1Hours(self):
        """Test Schedule1Hours"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
