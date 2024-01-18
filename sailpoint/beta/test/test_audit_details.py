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

from sailpoint.beta.models.audit_details import AuditDetails


class TestAuditDetails(unittest.TestCase):
    """AuditDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AuditDetails:
        """Test AuditDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AuditDetails`
        """
        model = AuditDetails()
        if include_optional:
            return AuditDetails(
                created = '2022-07-21T11:13:12.345Z',
                created_by = sailpoint.beta.models.identity_1.Identity_1(
                    id = '2c91808380aa05580180aaaaf1940410', 
                    name = 'William Wilson', ),
                modified = '2022-07-21T11:13:12.345Z',
                modified_by = sailpoint.beta.models.identity_1.Identity_1(
                    id = '2c91808380aa05580180aaaaf1940410', 
                    name = 'William Wilson', )
            )
        else:
            return AuditDetails(
        )
        """

    def testAuditDetails(self):
        """Test AuditDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
