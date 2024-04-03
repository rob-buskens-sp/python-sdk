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

from sailpoint.beta.models.event_bridge_config import EventBridgeConfig

class TestEventBridgeConfig(unittest.TestCase):
    """EventBridgeConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventBridgeConfig:
        """Test EventBridgeConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventBridgeConfig`
        """
        model = EventBridgeConfig()
        if include_optional:
            return EventBridgeConfig(
                aws_account = '123456789012',
                aws_region = 'us-west-1'
            )
        else:
            return EventBridgeConfig(
                aws_account = '123456789012',
                aws_region = 'us-west-1',
        )
        """

    def testEventBridgeConfig(self):
        """Test EventBridgeConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
