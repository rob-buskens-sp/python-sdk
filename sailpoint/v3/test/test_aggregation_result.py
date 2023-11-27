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

from sailpoint.v3.models.aggregation_result import AggregationResult  # noqa: E501


class TestAggregationResult(unittest.TestCase):
    """AggregationResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AggregationResult:
        """Test AggregationResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AggregationResult`
        """
        model = AggregationResult()  # noqa: E501
        if include_optional:
            return AggregationResult(
                aggregations = {Identity Locations={buckets=[{key=Austin, doc_count=109}, {key=London, doc_count=64}, {key=San Jose, doc_count=27}, {key=Brussels, doc_count=26}, {key=Sao Paulo, doc_count=24}, {key=Munich, doc_count=23}, {key=Singapore, doc_count=22}, {key=Tokyo, doc_count=20}, {key=Taipei, doc_count=16}]}},
                hits = [
                    sailpoint.v3.models.search_document.SearchDocument()
                    ]
            )
        else:
            return AggregationResult(
        )
        """

    def testAggregationResult(self):
        """Test AggregationResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
