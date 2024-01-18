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

from sailpoint.v3.models.review_decision import ReviewDecision


class TestReviewDecision(unittest.TestCase):
    """ReviewDecision unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewDecision:
        """Test ReviewDecision
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewDecision`
        """
        model = ReviewDecision()
        if include_optional:
            return ReviewDecision(
                id = 'ef38f94347e94562b5bb8424a56397d8',
                decision = 'APPROVE',
                proposed_end_date = '2017-07-11T18:45:37.098Z',
                bulk = True,
                recommendation = sailpoint.v3.models.review_recommendation.ReviewRecommendation(
                    recommendation = '', 
                    reasons = [Reason 1, Reason 2], 
                    timestamp = '2020-06-01T13:49:37.385Z', ),
                comments = 'This user no longer needs access to this source'
            )
        else:
            return ReviewDecision(
                id = 'ef38f94347e94562b5bb8424a56397d8',
                decision = 'APPROVE',
                bulk = True,
        )
        """

    def testReviewDecision(self):
        """Test ReviewDecision"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
