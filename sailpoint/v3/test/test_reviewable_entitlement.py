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

from v3.models.reviewable_entitlement import ReviewableEntitlement  # noqa: E501

class TestReviewableEntitlement(unittest.TestCase):
    """ReviewableEntitlement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReviewableEntitlement:
        """Test ReviewableEntitlement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReviewableEntitlement`
        """
        model = ReviewableEntitlement()  # noqa: E501
        if include_optional:
            return ReviewableEntitlement(
                id = '2c918085718230600171993742c63558',
                name = 'CN=entitlement.bbb7c650',
                description = 'Gives read/write access to the company database',
                privileged = False,
                owner = v3.models.identity_reference_with_name_and_email.IdentityReferenceWithNameAndEmail(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', 
                    name = 'Alison Ferguso', 
                    email = 'alison.ferguso@identitysoon.com', ),
                attribute_name = 'memberOf',
                attribute_value = 'CN=entitlement.bbb7c650',
                source_schema_object_type = 'groups',
                source_name = 'ODS-AD-Source',
                source_type = 'Active Directory - Direct',
                has_permissions = False,
                is_permission = False,
                revocable = True,
                cloud_governed = False,
                contains_data_access = True,
                data_access = v3.models.data_access.DataAccess(
                    policies = [
                        v3.models.data_access_policies_inner.DataAccess_policies_inner(
                            value = 'GDPR-20', )
                        ], 
                    categories = [
                        v3.models.data_access_categories_inner.DataAccess_categories_inner(
                            value = 'email-7', 
                            match_count = 10, )
                        ], 
                    impact_score = v3.models.data_access_impact_score.DataAccess_impactScore(
                        value = 'Medium', ), ),
                account = v3.models.reviewable_entitlement_account.ReviewableEntitlement_account(
                    native_identity = 'CN=Alison Ferguso', 
                    disabled = False, 
                    locked = False, 
                    type = 'IDENTITY', 
                    id = '2c9180857182305e0171993737eb29e6', 
                    name = 'Alison Ferguso', 
                    created = '2020-04-20T20:11:05.067Z', 
                    modified = '2020-05-20T18:57:16.987Z', )
            )
        else:
            return ReviewableEntitlement(
        )
        """

    def testReviewableEntitlement(self):
        """Test ReviewableEntitlement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
