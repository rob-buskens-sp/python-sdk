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

from sailpoint.beta.models.access_profile_update_item import AccessProfileUpdateItem

class TestAccessProfileUpdateItem(unittest.TestCase):
    """AccessProfileUpdateItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfileUpdateItem:
        """Test AccessProfileUpdateItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfileUpdateItem`
        """
        model = AccessProfileUpdateItem()
        if include_optional:
            return AccessProfileUpdateItem(
                id = '2c7180a46faadee4016fb4e018c20642',
                requestable = False,
                status = '201',
                description = '
> Access profile is updated successfully.

> Referenced Access profile with Id "2c7180a46faadee4016fb4e018c20642" was not found.
'
            )
        else:
            return AccessProfileUpdateItem(
                id = '2c7180a46faadee4016fb4e018c20642',
                requestable = False,
                status = '201',
        )
        """

    def testAccessProfileUpdateItem(self):
        """Test AccessProfileUpdateItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
