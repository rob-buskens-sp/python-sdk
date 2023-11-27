# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.v3.models.entitlement_dto import EntitlementDto  # noqa: E501


class TestEntitlementDto(unittest.TestCase):
    """EntitlementDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitlementDto:
        """Test EntitlementDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitlementDto`
        """
        model = EntitlementDto()  # noqa: E501
        if include_optional:
            return EntitlementDto(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z',
                attribute = 'authorizationType',
                value = 'CN=Users,dc=sailpoint,dc=com',
                description = 'Active Directory DC',
                attributes = {GroupType=Security, sAMAccountName=Buyer},
                source_schema_object_type = 'group',
                privileged = False,
                cloud_governed = False,
                source = sailpoint.v3.models.entitlement_source.EntitlementSource(
                    type = 'SOURCE', 
                    id = '2c9180835d191a86015d28455b4b232a', 
                    name = 'HR Active Directory', )
            )
        else:
            return EntitlementDto(
                name = 'aName',
        )
        """

    def testEntitlementDto(self):
        """Test EntitlementDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
