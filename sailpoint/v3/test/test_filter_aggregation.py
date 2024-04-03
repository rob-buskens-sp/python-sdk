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

from sailpoint.v3.models.filter_aggregation import FilterAggregation

class TestFilterAggregation(unittest.TestCase):
    """FilterAggregation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FilterAggregation:
        """Test FilterAggregation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FilterAggregation`
        """
        model = FilterAggregation()
        if include_optional:
            return FilterAggregation(
                name = 'Entitlements',
                type = 'TERM',
                field = 'access.type',
                value = 'ENTITLEMENT'
            )
        else:
            return FilterAggregation(
                name = 'Entitlements',
                field = 'access.type',
                value = 'ENTITLEMENT',
        )
        """

    def testFilterAggregation(self):
        """Test FilterAggregation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
