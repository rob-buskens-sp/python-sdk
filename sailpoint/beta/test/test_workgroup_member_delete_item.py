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

from sailpoint.beta.models.workgroup_member_delete_item import WorkgroupMemberDeleteItem

class TestWorkgroupMemberDeleteItem(unittest.TestCase):
    """WorkgroupMemberDeleteItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkgroupMemberDeleteItem:
        """Test WorkgroupMemberDeleteItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkgroupMemberDeleteItem`
        """
        model = WorkgroupMemberDeleteItem()
        if include_optional:
            return WorkgroupMemberDeleteItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '204',
                description = '
> Identity deleted from Governance Group members list.

> Referenced Governance Group Member with Identity Id "bc3a744678534eb78a8002ee2085df64" was not found.
'
            )
        else:
            return WorkgroupMemberDeleteItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '204',
        )
        """

    def testWorkgroupMemberDeleteItem(self):
        """Test WorkgroupMemberDeleteItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
