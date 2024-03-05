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

from sailpoint.beta.models.account_uncorrelated import AccountUncorrelated

class TestAccountUncorrelated(unittest.TestCase):
    """AccountUncorrelated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountUncorrelated:
        """Test AccountUncorrelated
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountUncorrelated`
        """
        model = AccountUncorrelated()
        if include_optional:
            return AccountUncorrelated(
                identity = sailpoint.beta.models.account_uncorrelated_identity.AccountUncorrelated_identity(
                    type = 'IDENTITY', 
                    id = '2c3780a46faadee4016fb4e018c20652', 
                    name = 'Allen Albertson', ),
                source = sailpoint.beta.models.account_uncorrelated_source.AccountUncorrelated_source(
                    type = 'SOURCE', 
                    id = '2c6180835d191a86015d28455b4b231b', 
                    name = 'Corporate Directory', ),
                account = sailpoint.beta.models.account_uncorrelated_account.AccountUncorrelated_account(
                    type = ACCOUNT, 
                    id = '4dd497e3723e439991cb6d0e478375dd', 
                    name = 'Sadie Jensen', 
                    native_identity = 'cn=john.doe,ou=users,dc=acme,dc=com', 
                    uuid = '1cb1f07d-3e5a-4431-becd-234fa4306108', ),
                entitlement_count = 0
            )
        else:
            return AccountUncorrelated(
                identity = sailpoint.beta.models.account_uncorrelated_identity.AccountUncorrelated_identity(
                    type = 'IDENTITY', 
                    id = '2c3780a46faadee4016fb4e018c20652', 
                    name = 'Allen Albertson', ),
                source = sailpoint.beta.models.account_uncorrelated_source.AccountUncorrelated_source(
                    type = 'SOURCE', 
                    id = '2c6180835d191a86015d28455b4b231b', 
                    name = 'Corporate Directory', ),
                account = sailpoint.beta.models.account_uncorrelated_account.AccountUncorrelated_account(
                    type = ACCOUNT, 
                    id = '4dd497e3723e439991cb6d0e478375dd', 
                    name = 'Sadie Jensen', 
                    native_identity = 'cn=john.doe,ou=users,dc=acme,dc=com', 
                    uuid = '1cb1f07d-3e5a-4431-becd-234fa4306108', ),
        )
        """

    def testAccountUncorrelated(self):
        """Test AccountUncorrelated"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
