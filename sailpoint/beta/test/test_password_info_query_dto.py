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

from sailpoint.beta.models.password_info_query_dto import PasswordInfoQueryDTO


class TestPasswordInfoQueryDTO(unittest.TestCase):
    """PasswordInfoQueryDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordInfoQueryDTO:
        """Test PasswordInfoQueryDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordInfoQueryDTO`
        """
        model = PasswordInfoQueryDTO()
        if include_optional:
            return PasswordInfoQueryDTO(
                user_name = 'Abby.Smith',
                source_name = 'My-AD'
            )
        else:
            return PasswordInfoQueryDTO(
        )
        """

    def testPasswordInfoQueryDTO(self):
        """Test PasswordInfoQueryDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
