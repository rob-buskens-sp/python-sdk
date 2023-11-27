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

from sailpoint.beta.models.managed_client import ManagedClient  # noqa: E501


class TestManagedClient(unittest.TestCase):
    """ManagedClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedClient:
        """Test ManagedClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedClient`
        """
        model = ManagedClient()  # noqa: E501
        if include_optional:
            return ManagedClient(
                id = 'aClientId',
                alert_key = 'anAlertKey',
                api_gateway_base_url = 'https://denali-xxx.api.cloud.sailpoint.com',
                cc_id = 2248,
                client_id = 'aClientApiId',
                cluster_id = 'aClusterId',
                cookbook = 'va-cookbook-info',
                description = 'A short description of the ManagedClient',
                ip_address = '123.456.78.90',
                last_seen = '2020-01-01T00:00Z',
                name = 'aName',
                since_last_seen = '15000',
                status = 'NORMAL',
                type = 'VA',
                va_download_url = 'aUrl',
                va_version = 'va-megapod-useast1-610-1621372012',
                secret = 'ef878e15eaa8c8d3e2fa52f41125e2a0eeadadc6a14f931a33ad3e1b62d56381'
            )
        else:
            return ManagedClient(
                client_id = 'aClientApiId',
                cluster_id = 'aClusterId',
                description = 'A short description of the ManagedClient',
                type = 'VA',
        )
        """

    def testManagedClient(self):
        """Test ManagedClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
