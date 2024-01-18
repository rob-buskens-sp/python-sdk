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

from sailpoint.beta.models.account_request_info import AccountRequestInfo


class TestAccountRequestInfo(unittest.TestCase):
    """AccountRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountRequestInfo:
        """Test AccountRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountRequestInfo`
        """
        model = AccountRequestInfo()
        if include_optional:
            return AccountRequestInfo(
                requested_object_id = '2c91808563ef85690164001c31140c0c',
                requested_object_name = 'Treasury Analyst',
                requested_object_type = 'ACCESS_PROFILE'
            )
        else:
            return AccountRequestInfo(
        )
        """

    def testAccountRequestInfo(self):
        """Test AccountRequestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
