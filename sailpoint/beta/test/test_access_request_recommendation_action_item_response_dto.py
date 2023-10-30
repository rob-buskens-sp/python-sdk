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

from beta.models.access_request_recommendation_action_item_response_dto import AccessRequestRecommendationActionItemResponseDto  # noqa: E501

class TestAccessRequestRecommendationActionItemResponseDto(unittest.TestCase):
    """AccessRequestRecommendationActionItemResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestRecommendationActionItemResponseDto:
        """Test AccessRequestRecommendationActionItemResponseDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestRecommendationActionItemResponseDto`
        """
        model = AccessRequestRecommendationActionItemResponseDto()  # noqa: E501
        if include_optional:
            return AccessRequestRecommendationActionItemResponseDto(
                identity_id = '2c91808570313110017040b06f344ec9',
                access = beta.models.access_request_recommendation_item.AccessRequestRecommendationItem(
                    id = '2c9180835d2e5168015d32f890ca1581', 
                    type = 'ACCESS_PROFILE', ),
                timestamp = '2017-07-11T18:45:37.098Z'
            )
        else:
            return AccessRequestRecommendationActionItemResponseDto(
        )
        """

    def testAccessRequestRecommendationActionItemResponseDto(self):
        """Test AccessRequestRecommendationActionItemResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
