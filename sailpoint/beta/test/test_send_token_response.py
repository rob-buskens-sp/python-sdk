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

from sailpoint.beta.models.send_token_response import SendTokenResponse


class TestSendTokenResponse(unittest.TestCase):
    """SendTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SendTokenResponse:
        """Test SendTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SendTokenResponse`
        """
        model = SendTokenResponse()
        if include_optional:
            return SendTokenResponse(
                request_id = '089899f13a8f4da7824996191587bab9',
                status = 'SUCCESS',
                error_message = 'Unable to sent text message'
            )
        else:
            return SendTokenResponse(
        )
        """

    def testSendTokenResponse(self):
        """Test SendTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
