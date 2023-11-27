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

from sailpoint.v3.models.expansion_item import ExpansionItem  # noqa: E501


class TestExpansionItem(unittest.TestCase):
    """ExpansionItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExpansionItem:
        """Test ExpansionItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExpansionItem`
        """
        model = ExpansionItem()  # noqa: E501
        if include_optional:
            return ExpansionItem(
                account_id = '2c91808981f58ea601821c3e93482e6f',
                cause = 'Role',
                name = 'smartsheet-role',
                attribute_requests = [
                    sailpoint.v3.models.attribute_request.AttributeRequest(
                        name = 'groups', 
                        op = 'Add', 
                        value = '3203537556531076', )
                    ],
                source = None
            )
        else:
            return ExpansionItem(
        )
        """

    def testExpansionItem(self):
        """Test ExpansionItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
