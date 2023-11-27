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

from sailpoint.v3.models.aggregations import Aggregations  # noqa: E501


class TestAggregations(unittest.TestCase):
    """Aggregations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Aggregations:
        """Test Aggregations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Aggregations`
        """
        model = Aggregations()  # noqa: E501
        if include_optional:
            return Aggregations(
                nested = sailpoint.v3.models.nested_aggregation.NestedAggregation(
                    name = 'id', 
                    type = 'access', ),
                metric = sailpoint.v3.models.metric_aggregation.MetricAggregation(
                    name = 'Access Name Count', 
                    type = 'UNIQUE_COUNT', 
                    field = '@access.name', ),
                filter = sailpoint.v3.models.filter_aggregation.FilterAggregation(
                    name = 'Entitlements', 
                    type = 'TERM', 
                    field = 'access.type', 
                    value = 'ENTITLEMENT', ),
                bucket = sailpoint.v3.models.bucket_aggregation.BucketAggregation(
                    name = 'Identity Locations', 
                    type = 'TERMS', 
                    field = 'attributes.city', 
                    size = 100, 
                    min_doc_count = 2, )
            )
        else:
            return Aggregations(
        )
        """

    def testAggregations(self):
        """Test Aggregations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
