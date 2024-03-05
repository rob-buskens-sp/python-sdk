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

from sailpoint.beta.models.workgroup_delete_item import WorkgroupDeleteItem

class TestWorkgroupDeleteItem(unittest.TestCase):
    """WorkgroupDeleteItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkgroupDeleteItem:
        """Test WorkgroupDeleteItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkgroupDeleteItem`
        """
        model = WorkgroupDeleteItem()
        if include_optional:
            return WorkgroupDeleteItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '204',
                description = '
> Governance Group deleted successfully.

> Unable to delete Governance Group f80bba83-98c4-4ec2-81c8-373c00e9663b because it is in use.

> Referenced Governance Group 2b711763-ed35-42a2-a80c-8f1ce0dc4a7f was not found.
'
            )
        else:
            return WorkgroupDeleteItem(
                id = '464ae7bf791e49fdb74606a2e4a89635',
                status = '204',
        )
        """

    def testWorkgroupDeleteItem(self):
        """Test WorkgroupDeleteItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
