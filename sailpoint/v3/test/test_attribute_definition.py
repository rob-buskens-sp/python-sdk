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

from sailpoint.v3.models.attribute_definition import AttributeDefinition  # noqa: E501


class TestAttributeDefinition(unittest.TestCase):
    """AttributeDefinition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeDefinition:
        """Test AttributeDefinition
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeDefinition`
        """
        model = AttributeDefinition()  # noqa: E501
        if include_optional:
            return AttributeDefinition(
                name = 'sAMAccountName',
                type = 'STRING',
                var_schema = sailpoint.v3.models.attribute_definition_schema.AttributeDefinition_schema(
                    type = 'CONNECTOR_SCHEMA', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'group', ),
                description = 'SAM Account Name',
                is_multi = False,
                is_entitlement = False,
                is_group = False
            )
        else:
            return AttributeDefinition(
        )
        """

    def testAttributeDefinition(self):
        """Test AttributeDefinition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
