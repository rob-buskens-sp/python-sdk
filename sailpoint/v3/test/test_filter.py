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

from v3.models.filter import Filter  # noqa: E501

class TestFilter(unittest.TestCase):
    """Filter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Filter:
        """Test Filter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Filter`
        """
        model = Filter()  # noqa: E501
        if include_optional:
            return Filter(
                type = 'RANGE',
                range = v3.models.range.Range(
                    lower = v3.models.bound.Bound(
                        value = '1', 
                        inclusive = False, ), 
                    upper = v3.models.bound.Bound(
                        value = '1', 
                        inclusive = False, ), ),
                terms = [
                    'account_count'
                    ],
                exclude = False
            )
        else:
            return Filter(
        )
        """

    def testFilter(self):
        """Test Filter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
