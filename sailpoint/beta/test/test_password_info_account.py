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

from beta.models.password_info_account import PasswordInfoAccount  # noqa: E501

class TestPasswordInfoAccount(unittest.TestCase):
    """PasswordInfoAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordInfoAccount:
        """Test PasswordInfoAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordInfoAccount`
        """
        model = PasswordInfoAccount()  # noqa: E501
        if include_optional:
            return PasswordInfoAccount(
                account_id = 'CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com',
                account_name = 'Abby.Smith'
            )
        else:
            return PasswordInfoAccount(
        )
        """

    def testPasswordInfoAccount(self):
        """Test PasswordInfoAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
