# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.password_info import PasswordInfo

class TestPasswordInfo(unittest.TestCase):
    """PasswordInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordInfo:
        """Test PasswordInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordInfo`
        """
        model = PasswordInfo()
        if include_optional:
            return PasswordInfo(
                identity_id = '2c918085744fec4301746f9a5bce4605',
                source_id = '2c918083746f642c01746f990884012a',
                public_key_id = 'N2M1OTJiMGEtMDJlZS00ZWU3LTkyYTEtNjA5YmI5NWE3ZWVh',
                public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuGFkWi2J75TztpbaPKd36bJnIB3J8gZ6UcoS9oSDYsqBzPpTsfZXYaEf4Y4BKGgJIXmE/lwhwuj7mU1itdZ2qTSNFtnXA8Fn75c3UUkk+h+wdZbkuSmqlsJo3R1OnJkwkJggcAy9Jvk9jlcrNLWorpQ1w9raUvxtvfgkSdq153KxotenQ1HciSyZ0nA/Kw0UaucLnho8xdRowZs11afXGXA9IT9H6D8T6zUdtSxm0nAyH+mluma5LdTfaM50W3l/L8q56Vrqmx2pZIiwdx/0+g3Y++jV70zom0ZBkC1MmSoLMrQYG5OICNjr72f78B2PaGXfarQHqARLjKpMVt9YIQIDAQAB',
                accounts = [
                    sailpoint.v3.models.password_info_account.PasswordInfoAccount(
                        account_id = 'CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com', 
                        account_name = 'Abby.Smith', )
                    ],
                policies = [passwordRepeatedChar is 3, passwordMinAlpha is 1, passwordMinLength is 5, passwordMinNumeric is 1]
            )
        else:
            return PasswordInfo(
        )
        """

    def testPasswordInfo(self):
        """Test PasswordInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
