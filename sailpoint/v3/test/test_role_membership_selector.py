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

from v3.models.role_membership_selector import RoleMembershipSelector  # noqa: E501

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
        model = RoleMembershipSelector()  # noqa: E501
        if include_optional:
            return RoleMembershipSelector(
                type = 'IDENTITY_LIST',
                criteria = v3.models.role_criteria_level1.RoleCriteriaLevel1(
                    operation = 'EQUALS', 
                    key = v3.models.role_criteria_key.RoleCriteriaKey(
                        type = 'ACCOUNT', 
                        property = 'attribute.email', 
                        source_id = '2c9180867427f3a301745aec18211519', ), 
                    string_value = 'carlee.cert1c9f9b6fd@mailinator.com', 
                    children = [
                        v3.models.role_criteria_level2.RoleCriteriaLevel2(
                            string_value = 'carlee.cert1c9f9b6fd@mailinator.com', )
                        ], ),
                identities = [
                    v3.models.role_membership_identity.RoleMembershipIdentity(
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
