# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.account_attributes_create_attributes import AccountAttributesCreateAttributes

class TestAccountAttributesCreateAttributes(unittest.TestCase):
    """AccountAttributesCreateAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountAttributesCreateAttributes:
        """Test AccountAttributesCreateAttributes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountAttributesCreateAttributes`
        """
        model = AccountAttributesCreateAttributes()
        if include_optional:
            return AccountAttributesCreateAttributes(
                source_id = '34bfcbe116c9407464af37acbaf7a4dc'
            )
        else:
            return AccountAttributesCreateAttributes(
                source_id = '34bfcbe116c9407464af37acbaf7a4dc',
        )
        """

    def testAccountAttributesCreateAttributes(self):
        """Test AccountAttributesCreateAttributes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
