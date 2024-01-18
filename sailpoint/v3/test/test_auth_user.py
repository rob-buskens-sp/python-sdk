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

from sailpoint.v3.models.auth_user import AuthUser


class TestAuthUser(unittest.TestCase):
    """AuthUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuthUser:
        """Test AuthUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuthUser`
        """
        model = AuthUser()
        if include_optional:
            return AuthUser(
                tenant = 'test-tenant',
                id = '2c91808458ae7a4f0158b1bbf8af0628',
                uid = 'will.smith',
                profile = '2c91808458ae7a4f0158b1bbf8af0756',
                identification_number = '19-5588452',
                email = 'william.smith@example.com',
                phone = '5555555555',
                work_phone = '5555555555',
                personal_email = 'william.smith@example.com',
                firstname = 'Will',
                lastname = 'Smith',
                display_name = 'Will Smith',
                alias = 'will.smith',
                last_password_change_date = '2021-03-08T22:37:33.901Z',
                last_login_timestamp = 1656327185832,
                current_login_timestamp = 1656327185832,
                capabilities = [
                    'ORG_ADMIN'
                    ]
            )
        else:
            return AuthUser(
        )
        """

    def testAuthUser(self):
        """Test AuthUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
