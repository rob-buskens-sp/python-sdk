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

from sailpoint.beta.models.campaign_template import CampaignTemplate

class TestCampaignTemplate(unittest.TestCase):
    """CampaignTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CampaignTemplate:
        """Test CampaignTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CampaignTemplate`
        """
        model = CampaignTemplate()
        if include_optional:
            return CampaignTemplate(
                id = '2c9079b270a266a60170a277bb960008',
                name = 'Manager Campaign Template',
                description = 'Template for the annual manager campaign.',
                created = '2020-03-05T22:44:00.364Z',
                modified = '2020-03-05T22:52:09.969Z',
                scheduled = False,
                owner_ref = sailpoint.beta.models.campaign_template_owner_ref.CampaignTemplate_ownerRef(
                    id = '2c918086676d3e0601677611dbde220f', 
                    type = 'IDENTITY', 
                    name = 'Mister Manager', 
                    email = 'mr.manager@example.com', ),
                deadline_duration = 'P2W',
                campaign = sailpoint.beta.models.campaign.Campaign()
            )
        else:
            return CampaignTemplate(
                name = 'Manager Campaign Template',
                description = 'Template for the annual manager campaign.',
                created = '2020-03-05T22:44:00.364Z',
                modified = '2020-03-05T22:52:09.969Z',
                campaign = sailpoint.beta.models.campaign.Campaign(),
        )
        """

    def testCampaignTemplate(self):
        """Test CampaignTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
