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

from v3.models.account import Account  # noqa: E501

class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Account`
        """
        model = Account()  # noqa: E501
        if include_optional:
            return Account(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z',
                source_id = '2c9180835d2e5168015d32f890ca1581',
                source_name = 'Employees',
                identity_id = '2c9180835d2e5168015d32f890ca1581',
                attributes = {firstName=SailPoint, lastName=Support, displayName=SailPoint Support},
                authoritative = False,
                description = '',
                disabled = False,
                locked = False,
                native_identity = '552775',
                system_account = False,
                uncorrelated = False,
                uuid = 'slpt.support',
                manually_correlated = False,
                has_entitlements = True
            )
        else:
            return Account(
                name = 'aName',
                source_id = '2c9180835d2e5168015d32f890ca1581',
                source_name = 'Employees',
                attributes = {firstName=SailPoint, lastName=Support, displayName=SailPoint Support},
                authoritative = False,
                disabled = False,
                locked = False,
                native_identity = '552775',
                system_account = False,
                uncorrelated = False,
                manually_correlated = False,
                has_entitlements = True,
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
