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

from sailpoint.v3.models.identity_with_new_access_access_refs_inner import IdentityWithNewAccessAccessRefsInner

class TestIdentityWithNewAccessAccessRefsInner(unittest.TestCase):
    """IdentityWithNewAccessAccessRefsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityWithNewAccessAccessRefsInner:
        """Test IdentityWithNewAccessAccessRefsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityWithNewAccessAccessRefsInner`
        """
        model = IdentityWithNewAccessAccessRefsInner()
        if include_optional:
            return IdentityWithNewAccessAccessRefsInner(
                type = 'ENTITLEMENT',
                id = '2c91809773dee32014e13e122092014e',
                name = 'CN=entitlement.490efde5,OU=OrgCo,OU=ServiceDept,DC=HQAD,DC=local'
            )
        else:
            return IdentityWithNewAccessAccessRefsInner(
        )
        """

    def testIdentityWithNewAccessAccessRefsInner(self):
        """Test IdentityWithNewAccessAccessRefsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
