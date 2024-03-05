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

from sailpoint.v3.models.access_review_item import AccessReviewItem

class TestAccessReviewItem(unittest.TestCase):
    """AccessReviewItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessReviewItem:
        """Test AccessReviewItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessReviewItem`
        """
        model = AccessReviewItem()
        if include_optional:
            return AccessReviewItem(
                access_summary = sailpoint.v3.models.access_summary.AccessSummary(
                    access = sailpoint.v3.models.access_summary_access.AccessSummary_access(
                        type = 'IDENTITY', 
                        id = '2c9180867160846801719932c5153fb7', 
                        name = 'Entitlement for Company Database', ), 
                    entitlement = sailpoint.v3.models.reviewable_entitlement.ReviewableEntitlement(
                        id = '2c918085718230600171993742c63558', 
                        name = 'CN=entitlement.bbb7c650', 
                        description = 'Gives read/write access to the company database', 
                        privileged = False, 
                        owner = sailpoint.v3.models.identity_reference_with_name_and_email.IdentityReferenceWithNameAndEmail(
                            id = '5168015d32f890ca15812c9180835d2e', 
                            name = 'Alison Ferguso', 
                            email = 'alison.ferguso@identitysoon.com', ), 
                        attribute_name = 'memberOf', 
                        attribute_value = 'CN=entitlement.bbb7c650', 
                        source_schema_object_type = 'groups', 
                        source_name = 'ODS-AD-Source', 
                        source_type = 'Active Directory - Direct', 
                        source_id = '78ca6be511cb41fbb86dba2fcca7780c', 
                        has_permissions = False, 
                        is_permission = False, 
                        revocable = True, 
                        cloud_governed = False, 
                        contains_data_access = True, 
                        data_access = sailpoint.v3.models.data_access.DataAccess(
                            policies = [
                                sailpoint.v3.models.data_access_policies_inner.DataAccess_policies_inner(
                                    value = 'GDPR-20', )
                                ], 
                            categories = [
                                sailpoint.v3.models.data_access_categories_inner.DataAccess_categories_inner(
                                    value = 'email-7', 
                                    match_count = 10, )
                                ], 
                            impact_score = sailpoint.v3.models.data_access_impact_score.DataAccess_impactScore(
                                value = 'Medium', ), ), 
                        account = sailpoint.v3.models.reviewable_entitlement_account.ReviewableEntitlement_account(
                            native_identity = 'CN=Alison Ferguso', 
                            disabled = False, 
                            locked = False, 
                            id = '2c9180857182305e0171993737eb29e6', 
                            name = 'Alison Ferguso', 
                            created = '2020-04-20T20:11:05.067Z', 
                            modified = '2020-05-20T18:57:16.987Z', 
                            activity_insights = sailpoint.v3.models.activity_insights.ActivityInsights(
                                account_id = 'c4ddd5421d8549f0abd309162cafd3b1', 
                                usage_days = 45, 
                                usage_days_state = 'COMPLETE', ), ), ), 
                    access_profile = sailpoint.v3.models.reviewable_access_profile.ReviewableAccessProfile(
                        id = '2c91808a7190d06e01719938fcd20792', 
                        name = 'Employee-database-read-write', 
                        description = 'Collection of entitlements to read/write the employee database', 
                        privileged = False, 
                        cloud_governed = False, 
                        end_date = '2021-12-25T00:00Z', 
                        entitlements = [
                            sailpoint.v3.models.reviewable_entitlement.ReviewableEntitlement(
                                id = '2c918085718230600171993742c63558', 
                                name = 'CN=entitlement.bbb7c650', 
                                description = 'Gives read/write access to the company database', 
                                privileged = False, 
                                attribute_name = 'memberOf', 
                                attribute_value = 'CN=entitlement.bbb7c650', 
                                source_schema_object_type = 'groups', 
                                source_name = 'ODS-AD-Source', 
                                source_type = 'Active Directory - Direct', 
                                source_id = '78ca6be511cb41fbb86dba2fcca7780c', 
                                has_permissions = False, 
                                is_permission = False, 
                                revocable = True, 
                                cloud_governed = False, 
                                contains_data_access = True, )
                            ], 
                        created = '2021-01-01T22:32:58.104Z', 
                        modified = '2021-02-01T22:32:58.104Z', ), 
                    role = sailpoint.v3.models.reviewable_role.ReviewableRole(
                        id = '2c91808a7190d06e0171993907fd0794', 
                        name = 'Accounting-Employees', 
                        description = 'Role for members of the accounting department with the necessary Access Profiles', 
                        privileged = False, 
                        revocable = False, 
                        end_date = '2021-12-25T00:00Z', 
                        access_profiles = [
                            sailpoint.v3.models.reviewable_access_profile.ReviewableAccessProfile(
                                id = '2c91808a7190d06e01719938fcd20792', 
                                name = 'Employee-database-read-write', 
                                description = 'Collection of entitlements to read/write the employee database', 
                                privileged = False, 
                                cloud_governed = False, 
                                end_date = '2021-12-25T00:00Z', 
                                created = '2021-01-01T22:32:58.104Z', 
                                modified = '2021-02-01T22:32:58.104Z', )
                            ], ), ),
                identity_summary = sailpoint.v3.models.certification_identity_summary.CertificationIdentitySummary(
                    id = '2c91808772a504f50172a9540e501ba7', 
                    name = 'Alison Ferguso', 
                    identity_id = '2c9180857182306001719937377a33de', 
                    completed = True, ),
                id = 'ef38f94347e94562b5bb8424a56397d8',
                completed = False,
                new_access = False,
                decision = 'APPROVE',
                comments = 'This user still needs access to this source'
            )
        else:
            return AccessReviewItem(
        )
        """

    def testAccessReviewItem(self):
        """Test AccessReviewItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
