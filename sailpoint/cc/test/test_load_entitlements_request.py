# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.cc.models.load_entitlements_request import LoadEntitlementsRequest


class TestLoadEntitlementsRequest(unittest.TestCase):
    """LoadEntitlementsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoadEntitlementsRequest:
        """Test LoadEntitlementsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoadEntitlementsRequest`
        """
        model = LoadEntitlementsRequest()
        if include_optional:
            return LoadEntitlementsRequest(
                file = bytes(b'blah')
            )
        else:
            return LoadEntitlementsRequest(
        )
        """

    def testLoadEntitlementsRequest(self):
        """Test LoadEntitlementsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
