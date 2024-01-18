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

from sailpoint.v3.models.create_o_auth_client_request import CreateOAuthClientRequest


class TestCreateOAuthClientRequest(unittest.TestCase):
    """CreateOAuthClientRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOAuthClientRequest:
        """Test CreateOAuthClientRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOAuthClientRequest`
        """
        model = CreateOAuthClientRequest()
        if include_optional:
            return CreateOAuthClientRequest(
                business_name = 'Acme-Solar',
                homepage_url = 'http://localhost:12345',
                name = 'Demo API Client',
                description = 'An API client used for the authorization_code, refresh_token, and client_credentials flows',
                access_token_validity_seconds = 750,
                refresh_token_validity_seconds = 86400,
                redirect_uris = [http://localhost:12345],
                grant_types = [AUTHORIZATION_CODE, CLIENT_CREDENTIALS, REFRESH_TOKEN],
                access_type = 'OFFLINE',
                type = 'CONFIDENTIAL',
                internal = False,
                enabled = True,
                strong_auth_supported = False,
                claims_supported = False,
                scope = [demo:api-client-scope:first, demo:api-client-scope:second]
            )
        else:
            return CreateOAuthClientRequest(
                name = 'Demo API Client',
                description = 'An API client used for the authorization_code, refresh_token, and client_credentials flows',
                access_token_validity_seconds = 750,
                grant_types = [AUTHORIZATION_CODE, CLIENT_CREDENTIALS, REFRESH_TOKEN],
                access_type = 'OFFLINE',
                enabled = True,
        )
        """

    def testCreateOAuthClientRequest(self):
        """Test CreateOAuthClientRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
