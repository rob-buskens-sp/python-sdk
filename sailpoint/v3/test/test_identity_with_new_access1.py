# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.identity_with_new_access1 import IdentityWithNewAccess1

class TestIdentityWithNewAccess1(unittest.TestCase):
    """IdentityWithNewAccess1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityWithNewAccess1:
        """Test IdentityWithNewAccess1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityWithNewAccess1`
        """
        model = IdentityWithNewAccess1()
        if include_optional:
            return IdentityWithNewAccess1(
                identity_id = '2c91809050db617d0150e0bf3215385e',
                access_refs = [
                    null
                    ],
                client_metadata = {clientName=client1, clientId=2c91808f7892918f0178b78da4a305a1}
            )
        else:
            return IdentityWithNewAccess1(
                identity_id = '2c91809050db617d0150e0bf3215385e',
                access_refs = [
                    null
                    ],
        )
        """

    def testIdentityWithNewAccess1(self):
        """Test IdentityWithNewAccess1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
