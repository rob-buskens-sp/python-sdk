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

from sailpoint.v3.models.non_employee_schema_attribute_body import NonEmployeeSchemaAttributeBody

class TestNonEmployeeSchemaAttributeBody(unittest.TestCase):
    """NonEmployeeSchemaAttributeBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NonEmployeeSchemaAttributeBody:
        """Test NonEmployeeSchemaAttributeBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeSchemaAttributeBody`
        """
        model = NonEmployeeSchemaAttributeBody()
        if include_optional:
            return NonEmployeeSchemaAttributeBody(
                type = 'TEXT',
                label = 'Account Name',
                technical_name = 'account.name',
                help_text = 'The unique identifier for the account',
                placeholder = 'Enter a unique user name for this account.',
                required = True
            )
        else:
            return NonEmployeeSchemaAttributeBody(
                type = 'TEXT',
                label = 'Account Name',
                technical_name = 'account.name',
        )
        """

    def testNonEmployeeSchemaAttributeBody(self):
        """Test NonEmployeeSchemaAttributeBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
