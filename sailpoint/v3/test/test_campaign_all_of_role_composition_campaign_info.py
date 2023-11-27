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

from sailpoint.v3.models.campaign_all_of_role_composition_campaign_info import CampaignAllOfRoleCompositionCampaignInfo  # noqa: E501


class TestCampaignAllOfRoleCompositionCampaignInfo(unittest.TestCase):
    """CampaignAllOfRoleCompositionCampaignInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self,
            include_optional) -> CampaignAllOfRoleCompositionCampaignInfo:
        """Test CampaignAllOfRoleCompositionCampaignInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignAllOfRoleCompositionCampaignInfo`
        """
        model = CampaignAllOfRoleCompositionCampaignInfo()  # noqa: E501
        if include_optional:
            return CampaignAllOfRoleCompositionCampaignInfo(
                reviewer = sailpoint.v3.models.campaign_all_of_search_campaign_info_reviewer.Campaign_allOf_searchCampaignInfo_reviewer(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                role_ids = [2c90ad2a70ace7d50170acf22ca90010],
                remediator_ref = sailpoint.v3.models.campaign_all_of_role_composition_campaign_info_remediator_ref.Campaign_allOf_roleCompositionCampaignInfo_remediatorRef(
                    type = 'IDENTITY', 
                    id = '2c90ad2a70ace7d50170acf22ca90010', 
                    name = 'Role Admin', ),
                query = 'Search Query',
                description = 'Role Composition Description'
            )
        else:
            return CampaignAllOfRoleCompositionCampaignInfo(
                remediator_ref = sailpoint.v3.models.campaign_all_of_role_composition_campaign_info_remediator_ref.Campaign_allOf_roleCompositionCampaignInfo_remediatorRef(
                    type = 'IDENTITY', 
                    id = '2c90ad2a70ace7d50170acf22ca90010', 
                    name = 'Role Admin', ),
        )
        """

    def testCampaignAllOfRoleCompositionCampaignInfo(self):
        """Test CampaignAllOfRoleCompositionCampaignInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
