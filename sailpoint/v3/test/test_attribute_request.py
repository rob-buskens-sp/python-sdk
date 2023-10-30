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

from v3.models.attribute_request import AttributeRequest  # noqa: E501

class TestAttributeRequest(unittest.TestCase):
    """AttributeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AttributeRequest:
        """Test AttributeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AttributeRequest`
        """
        model = AttributeRequest()  # noqa: E501
        if include_optional:
            return AttributeRequest(
                name = 'groups',
                op = 'Add',
                value = '3203537556531076'
            )
        else:
            return AttributeRequest(
        )
        """

    def testAttributeRequest(self):
        """Test AttributeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
