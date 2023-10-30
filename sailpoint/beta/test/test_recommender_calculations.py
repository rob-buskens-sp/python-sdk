# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from beta.models.recommender_calculations import RecommenderCalculations  # noqa: E501

class TestRecommenderCalculations(unittest.TestCase):
    """RecommenderCalculations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecommenderCalculations:
        """Test RecommenderCalculations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecommenderCalculations`
        """
        model = RecommenderCalculations()  # noqa: E501
        if include_optional:
            return RecommenderCalculations(
                identity_id = '2c91808457d8f3ab0157e3e62cb4213c',
                entitlement_id = '2c91809050db617d0150e0bf3215385e',
                recommendation = 'YES',
                overall_weighted_score = 1.337,
                feature_weighted_scores = {
                    'key' : 1.337
                    },
                threshold = 1.337,
                identity_attributes = {
                    'key' : beta.models.recommender_calculations_identity_attributes_value.RecommenderCalculations_identityAttributes_value(
                        value = '', )
                    },
                feature_values = beta.models.feature_value_dto.FeatureValueDto(
                    feature = 'department', 
                    numerator = 14, 
                    denominator = 14, )
            )
        else:
            return RecommenderCalculations(
        )
        """

    def testRecommenderCalculations(self):
        """Test RecommenderCalculations"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
