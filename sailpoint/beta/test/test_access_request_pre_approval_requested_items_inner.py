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

from beta.models.access_request_pre_approval_requested_items_inner import AccessRequestPreApprovalRequestedItemsInner  # noqa: E501

class TestAccessRequestPreApprovalRequestedItemsInner(unittest.TestCase):
    """AccessRequestPreApprovalRequestedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestPreApprovalRequestedItemsInner:
        """Test AccessRequestPreApprovalRequestedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestPreApprovalRequestedItemsInner`
        """
        model = AccessRequestPreApprovalRequestedItemsInner()  # noqa: E501
        if include_optional:
            return AccessRequestPreApprovalRequestedItemsInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                description = 'Access to engineering database',
                type = ACCESS_PROFILE,
                operation = Add,
                comment = 'William needs this access to do his job.'
            )
        else:
            return AccessRequestPreApprovalRequestedItemsInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                type = ACCESS_PROFILE,
                operation = Add,
        )
        """

    def testAccessRequestPreApprovalRequestedItemsInner(self):
        """Test AccessRequestPreApprovalRequestedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
