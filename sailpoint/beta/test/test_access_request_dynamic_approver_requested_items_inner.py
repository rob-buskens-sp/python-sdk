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

from sailpoint.beta.models.access_request_dynamic_approver_requested_items_inner import AccessRequestDynamicApproverRequestedItemsInner

class TestAccessRequestDynamicApproverRequestedItemsInner(unittest.TestCase):
    """AccessRequestDynamicApproverRequestedItemsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestDynamicApproverRequestedItemsInner:
        """Test AccessRequestDynamicApproverRequestedItemsInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestDynamicApproverRequestedItemsInner`
        """
        model = AccessRequestDynamicApproverRequestedItemsInner()
        if include_optional:
            return AccessRequestDynamicApproverRequestedItemsInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                description = 'Engineering Access',
                type = ACCESS_PROFILE,
                operation = Add,
                comment = 'William needs this access for his day to day job activities.'
            )
        else:
            return AccessRequestDynamicApproverRequestedItemsInner(
                id = '2c91808b6ef1d43e016efba0ce470904',
                name = 'Engineering Access',
                type = ACCESS_PROFILE,
                operation = Add,
        )
        """

    def testAccessRequestDynamicApproverRequestedItemsInner(self):
        """Test AccessRequestDynamicApproverRequestedItemsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
