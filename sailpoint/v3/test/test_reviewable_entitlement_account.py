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

from sailpoint.v3.models.reviewable_entitlement_account import ReviewableEntitlementAccount


class TestReviewableEntitlementAccount(unittest.TestCase):
    """ReviewableEntitlementAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewableEntitlementAccount:
        """Test ReviewableEntitlementAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewableEntitlementAccount`
        """
        model = ReviewableEntitlementAccount()
        if include_optional:
            return ReviewableEntitlementAccount(
                native_identity = 'CN=Alison Ferguso',
                disabled = False,
                locked = False,
                type = 'IDENTITY',
                id = '2c9180857182305e0171993737eb29e6',
                name = 'Alison Ferguso',
                created = '2020-04-20T20:11:05.067Z',
                modified = '2020-05-20T18:57:16.987Z',
                activity_insights = sailpoint.v3.models.activity_insights.ActivityInsights(
                    account_id = 'c4ddd5421d8549f0abd309162cafd3b1', 
                    usage_days = 45, 
                    usage_days_state = 'COMPLETE', )
            )
        else:
            return ReviewableEntitlementAccount(
        )
        """

    def testReviewableEntitlementAccount(self):
        """Test ReviewableEntitlementAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
