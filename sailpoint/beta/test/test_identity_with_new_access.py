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

from beta.models.identity_with_new_access import IdentityWithNewAccess  # noqa: E501

class TestIdentityWithNewAccess(unittest.TestCase):
    """IdentityWithNewAccess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityWithNewAccess:
        """Test IdentityWithNewAccess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityWithNewAccess`
        """
        model = IdentityWithNewAccess()  # noqa: E501
        if include_optional:
            return IdentityWithNewAccess(
                identity_id = '2c91808568c529c60168cca6f90c1313',
                access_refs = [{type=ENTITLEMENT, id=2c918087682f9a86016839c050861ab1, name=CN=Information Access,OU=test,OU=test-service,DC=TestAD,DC=local}, {type=ENTITLEMENT, id=2c918087682f9a86016839c0509c1ab2, name=CN=Information Technology,OU=test,OU=test-service,DC=TestAD,DC=local}]
            )
        else:
            return IdentityWithNewAccess(
                identity_id = '2c91808568c529c60168cca6f90c1313',
                access_refs = [{type=ENTITLEMENT, id=2c918087682f9a86016839c050861ab1, name=CN=Information Access,OU=test,OU=test-service,DC=TestAD,DC=local}, {type=ENTITLEMENT, id=2c918087682f9a86016839c0509c1ab2, name=CN=Information Technology,OU=test,OU=test-service,DC=TestAD,DC=local}],
        )
        """

    def testIdentityWithNewAccess(self):
        """Test IdentityWithNewAccess"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
