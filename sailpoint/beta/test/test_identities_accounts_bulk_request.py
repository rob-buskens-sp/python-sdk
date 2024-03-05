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

from sailpoint.beta.models.identities_accounts_bulk_request import IdentitiesAccountsBulkRequest

class TestIdentitiesAccountsBulkRequest(unittest.TestCase):
    """IdentitiesAccountsBulkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentitiesAccountsBulkRequest:
        """Test IdentitiesAccountsBulkRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentitiesAccountsBulkRequest`
        """
        model = IdentitiesAccountsBulkRequest()
        if include_optional:
            return IdentitiesAccountsBulkRequest(
                identity_ids = [2c91808384203c2d018437e631158308, 2c9180858082150f0180893dbaf553fe]
            )
        else:
            return IdentitiesAccountsBulkRequest(
        )
        """

    def testIdentitiesAccountsBulkRequest(self):
        """Test IdentitiesAccountsBulkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
