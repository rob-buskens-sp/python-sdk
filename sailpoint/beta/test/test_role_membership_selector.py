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

from sailpoint.beta.models.role_membership_selector import RoleMembershipSelector


class TestRoleMembershipSelector(unittest.TestCase):
    """RoleMembershipSelector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleMembershipSelector:
        """Test RoleMembershipSelector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleMembershipSelector`
        """
        model = RoleMembershipSelector()
        if include_optional:
            return RoleMembershipSelector(
                type = 'IDENTITY_LIST',
                criteria = sailpoint.beta.models.role_criteria_level1.RoleCriteriaLevel1(
                    operation = 'EQUALS', 
                    key = sailpoint.beta.models.role_criteria_key.RoleCriteriaKey(
                        type = 'ACCOUNT', 
                        property = 'attribute.email', 
                        source_id = '2c9180867427f3a301745aec18211519', ), 
                    string_value = 'carlee.cert1c9f9b6fd@mailinator.com', 
                    children = [
                        sailpoint.beta.models.role_criteria_level2.RoleCriteriaLevel2(
                            string_value = 'carlee.cert1c9f9b6fd@mailinator.com', )
                        ], ),
                identities = [
                    sailpoint.beta.models.role_membership_identity.RoleMembershipIdentity(
                        type = 'IDENTITY', 
                        id = '2c9180a46faadee4016fb4e018c20639', 
                        name = 'Thomas Edison', 
                        alias_name = 't.edison', )
                    ]
            )
        else:
            return RoleMembershipSelector(
        )
        """

    def testRoleMembershipSelector(self):
        """Test RoleMembershipSelector"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
