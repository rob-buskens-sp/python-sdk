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

from sailpoint.beta.models.client_log_configuration import ClientLogConfiguration  # noqa: E501


class TestClientLogConfiguration(unittest.TestCase):
    """ClientLogConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientLogConfiguration:
        """Test ClientLogConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientLogConfiguration`
        """
        model = ClientLogConfiguration()  # noqa: E501
        if include_optional:
            return ClientLogConfiguration(
                client_id = 'aClientId',
                duration_minutes = 120,
                expiration = '2020-12-15T19:13:36.079Z',
                root_level = 'INFO',
                log_levels = INFO
            )
        else:
            return ClientLogConfiguration(
                duration_minutes = 120,
                root_level = 'INFO',
        )
        """

    def testClientLogConfiguration(self):
        """Test ClientLogConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
