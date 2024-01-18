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

from sailpoint.beta.models.subscription_post_request import SubscriptionPostRequest


class TestSubscriptionPostRequest(unittest.TestCase):
    """SubscriptionPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionPostRequest:
        """Test SubscriptionPostRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionPostRequest`
        """
        model = SubscriptionPostRequest()
        if include_optional:
            return SubscriptionPostRequest(
                name = 'Access request subscription',
                description = 'Access requested to site xyz',
                trigger_id = 'idn:access-requested',
                type = 'HTTP',
                response_deadline = 'PT1H',
                http_config = sailpoint.beta.models.http_config.HttpConfig(
                    url = 'https://www.example.com', 
                    http_dispatch_mode = 'SYNC', 
                    http_authentication_type = 'NO_AUTH', 
                    basic_auth_config = sailpoint.beta.models.basic_auth_config.BasicAuthConfig(
                        user_name = 'user@example.com', 
                        password = '', ), 
                    bearer_token_auth_config = sailpoint.beta.models.bearer_token_auth_config.BearerTokenAuthConfig(
                        bearer_token = '', ), ),
                event_bridge_config = sailpoint.beta.models.event_bridge_config.EventBridgeConfig(
                    aws_account = '123456789012', 
                    aws_region = 'us-west-1', ),
                enabled = True,
                filter = '$[?($.identityId == "201327fda1c44704ac01181e963d463c")]'
            )
        else:
            return SubscriptionPostRequest(
                name = 'Access request subscription',
                trigger_id = 'idn:access-requested',
                type = 'HTTP',
        )
        """

    def testSubscriptionPostRequest(self):
        """Test SubscriptionPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
