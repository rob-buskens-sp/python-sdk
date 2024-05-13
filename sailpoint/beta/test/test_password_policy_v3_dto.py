# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.password_policy_v3_dto import PasswordPolicyV3Dto

class TestPasswordPolicyV3Dto(unittest.TestCase):
    """PasswordPolicyV3Dto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordPolicyV3Dto:
        """Test PasswordPolicyV3Dto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordPolicyV3Dto`
        """
        model = PasswordPolicyV3Dto()
        if include_optional:
            return PasswordPolicyV3Dto(
                id = '2c91808e7d976f3b017d9f5ceae440c8',
                description = 'Information about the Password Policy',
                name = 'PasswordPolicy Example',
                date_crated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                first_expiration_reminder = 45,
                account_id_min_word_length = 4,
                account_name_min_word_length = 6,
                min_alpha = 5,
                min_character_types = 5,
                max_length = 25,
                min_length = 8,
                max_repeated_chars = 3,
                min_lower = 8,
                min_numeric = 8,
                min_special = 8,
                min_upper = 8,
                password_expiration = 8,
                default_policy = True,
                enable_passwd_expiration = True,
                require_strong_authn = True,
                require_strong_auth_off_network = True,
                require_strong_auth_untrusted_geographies = True,
                use_account_attributes = False,
                use_dictionary = False,
                use_identity_attributes = False,
                validate_against_account_id = False,
                validate_against_account_name = True,
                source_ids = [2c91808382ffee0b01830de154f14034, 2f98808382ffee0b01830de154f12134]
            )
        else:
            return PasswordPolicyV3Dto(
        )
        """

    def testPasswordPolicyV3Dto(self):
        """Test PasswordPolicyV3Dto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
