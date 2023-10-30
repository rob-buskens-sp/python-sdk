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

from beta.models.access_profile import AccessProfile  # noqa: E501

class TestAccessProfile(unittest.TestCase):
    """AccessProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfile:
        """Test AccessProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfile`
        """
        model = AccessProfile()  # noqa: E501
        if include_optional:
            return AccessProfile(
                id = '2c91808a7190d06e01719938fcd20792',
                name = 'Employee-database-read-write',
                description = 'Collection of entitlements to read/write the employee database',
                created = '2021-03-01T22:32:58.104Z',
                modified = '2021-03-02T20:22:28.104Z',
                enabled = True,
                owner = beta.models.owner_reference.OwnerReference(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'support', ),
                source = beta.models.access_profile_source_ref.AccessProfileSourceRef(
                    id = '2c91809773dee3610173fdb0b6061ef4', 
                    type = 'SOURCE', 
                    name = 'ODS-AD-SOURCE', ),
                entitlements = [
                    beta.models.entitlement_ref.EntitlementRef(
                        id = '2c91809773dee32014e13e122092014e', 
                        type = 'ENTITLEMENT', 
                        name = 'CN=entitlement.490efde5,OU=OrgCo,OU=ServiceDept,DC=HQAD,DC=local', )
                    ],
                requestable = True,
                access_request_config = beta.models.requestability.Requestability(
                    comments_required = True, 
                    denial_comments_required = True, 
                    approval_schemes = [
                        beta.models.access_profile_approval_scheme.AccessProfileApprovalScheme(
                            approver_type = 'GOVERNANCE_GROUP', 
                            approver_id = '46c79819-a69f-49a2-becb-12c971ae66c6', )
                        ], ),
                revocation_request_config = beta.models.revocability.Revocability(
                    comments_required = False, 
                    denial_comments_required = False, 
                    approval_schemes = [
                        beta.models.access_profile_approval_scheme.AccessProfileApprovalScheme(
                            approver_type = 'GOVERNANCE_GROUP', 
                            approver_id = '46c79819-a69f-49a2-becb-12c971ae66c6', )
                        ], ),
                segments = [f7b1b8a3-5fed-4fd4-ad29-82014e137e19, 29cb6c06-1da8-43ea-8be4-b3125f248f2a],
                provisioning_criteria = beta.models.provisioning_criteria_level1.ProvisioningCriteriaLevel1(
                    operation = 'EQUALS', 
                    attribute = 'email', 
                    value = 'carlee.cert1c9f9b6fd@mailinator.com', 
                    children = [
                        beta.models.provisioning_criteria_level2.ProvisioningCriteriaLevel2(
                            attribute = 'email', 
                            value = 'carlee.cert1c9f9b6fd@mailinator.com', )
                        ], )
            )
        else:
            return AccessProfile(
                name = 'Employee-database-read-write',
                owner = beta.models.owner_reference.OwnerReference(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'support', ),
                source = beta.models.access_profile_source_ref.AccessProfileSourceRef(
                    id = '2c91809773dee3610173fdb0b6061ef4', 
                    type = 'SOURCE', 
                    name = 'ODS-AD-SOURCE', ),
        )
        """

    def testAccessProfile(self):
        """Test AccessProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
