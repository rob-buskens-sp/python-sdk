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

from sailpoint.beta.models.fullcampaign_all_of_role_composition_campaign_info import FullcampaignAllOfRoleCompositionCampaignInfo  # noqa: E501


class TestFullcampaignAllOfRoleCompositionCampaignInfo(unittest.TestCase):
    """FullcampaignAllOfRoleCompositionCampaignInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self,
            include_optional) -> FullcampaignAllOfRoleCompositionCampaignInfo:
        """Test FullcampaignAllOfRoleCompositionCampaignInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FullcampaignAllOfRoleCompositionCampaignInfo`
        """
        model = FullcampaignAllOfRoleCompositionCampaignInfo()  # noqa: E501
        if include_optional:
            return FullcampaignAllOfRoleCompositionCampaignInfo(
                reviewer = sailpoint.beta.models.fullcampaign_all_of_search_campaign_info_reviewer.fullcampaign_allOf_searchCampaignInfo_reviewer(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                role_ids = [2c90ad2a70ace7d50170acf22ca90010],
                remediator_ref = sailpoint.beta.models.fullcampaign_all_of_role_composition_campaign_info_remediator_ref.fullcampaign_allOf_roleCompositionCampaignInfo_remediatorRef(
                    type = 'IDENTITY', 
                    id = '2c90ad2a70ace7d50170acf22ca90010', 
                    name = 'Role Admin', ),
                query = 'Search Query',
                description = 'Role Composition Description'
            )
        else:
            return FullcampaignAllOfRoleCompositionCampaignInfo(
                remediator_ref = sailpoint.beta.models.fullcampaign_all_of_role_composition_campaign_info_remediator_ref.fullcampaign_allOf_roleCompositionCampaignInfo_remediatorRef(
                    type = 'IDENTITY', 
                    id = '2c90ad2a70ace7d50170acf22ca90010', 
                    name = 'Role Admin', ),
        )
        """

    def testFullcampaignAllOfRoleCompositionCampaignInfo(self):
        """Test FullcampaignAllOfRoleCompositionCampaignInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
