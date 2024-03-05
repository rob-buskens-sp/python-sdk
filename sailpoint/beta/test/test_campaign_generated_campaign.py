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

from sailpoint.beta.models.campaign_generated_campaign import CampaignGeneratedCampaign

class TestCampaignGeneratedCampaign(unittest.TestCase):
    """CampaignGeneratedCampaign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignGeneratedCampaign:
        """Test CampaignGeneratedCampaign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignGeneratedCampaign`
        """
        model = CampaignGeneratedCampaign()
        if include_optional:
            return CampaignGeneratedCampaign(
                id = '2c91808576f886190176f88cac5a0010',
                name = 'Manager Access Campaign',
                description = 'Audit access for all employees.',
                created = '2021-02-16T03:04:45.815Z',
                modified = '2021-02-17T03:04:45.815Z',
                deadline = '2021-02-18T03:04:45.815Z',
                type = MANAGER,
                campaign_owner = sailpoint.beta.models.campaign_generated_campaign_campaign_owner.CampaignGenerated_campaign_campaignOwner(
                    id = '37f080867702c1910177031320c40n27', 
                    display_name = 'John Snow', 
                    email = 'john.snow@example.com', ),
                status = STAGED
            )
        else:
            return CampaignGeneratedCampaign(
                id = '2c91808576f886190176f88cac5a0010',
                name = 'Manager Access Campaign',
                description = 'Audit access for all employees.',
                created = '2021-02-16T03:04:45.815Z',
                type = MANAGER,
                campaign_owner = sailpoint.beta.models.campaign_generated_campaign_campaign_owner.CampaignGenerated_campaign_campaignOwner(
                    id = '37f080867702c1910177031320c40n27', 
                    display_name = 'John Snow', 
                    email = 'john.snow@example.com', ),
                status = STAGED,
        )
        """

    def testCampaignGeneratedCampaign(self):
        """Test CampaignGeneratedCampaign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
