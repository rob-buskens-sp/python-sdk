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

from sailpoint.beta.models.account_toggle_request import AccountToggleRequest


class TestAccountToggleRequest(unittest.TestCase):
    """AccountToggleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountToggleRequest:
        """Test AccountToggleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountToggleRequest`
        """
        model = AccountToggleRequest()
        if include_optional:
            return AccountToggleRequest(
                external_verification_id = '3f9180835d2e5168015d32f890ca1581',
                force_provisioning = False
            )
        else:
            return AccountToggleRequest(
        )
        """

    def testAccountToggleRequest(self):
        """Test AccountToggleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
