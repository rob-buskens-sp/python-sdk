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

from sailpoint.beta.models.get_personal_access_token_response import GetPersonalAccessTokenResponse


class TestGetPersonalAccessTokenResponse(unittest.TestCase):
    """GetPersonalAccessTokenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> GetPersonalAccessTokenResponse:
        """Test GetPersonalAccessTokenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetPersonalAccessTokenResponse`
        """
        model = GetPersonalAccessTokenResponse()
        if include_optional:
            return GetPersonalAccessTokenResponse(
                id = '86f1dc6fe8f54414950454cbb11278fa',
                name = 'NodeJS Integration',
                scope = [demo:personal-access-token-scope:first, demo:personal-access-token-scope:second],
                owner = sailpoint.beta.models.pat_owner.PatOwner(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                created = '2017-07-11T18:45:37.098Z',
                last_used = '2017-07-11T18:45:37.098Z'
            )
        else:
            return GetPersonalAccessTokenResponse(
                id = '86f1dc6fe8f54414950454cbb11278fa',
                name = 'NodeJS Integration',
                scope = [demo:personal-access-token-scope:first, demo:personal-access-token-scope:second],
                owner = sailpoint.beta.models.pat_owner.PatOwner(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                created = '2017-07-11T18:45:37.098Z',
        )
        """

    def testGetPersonalAccessTokenResponse(self):
        """Test GetPersonalAccessTokenResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
