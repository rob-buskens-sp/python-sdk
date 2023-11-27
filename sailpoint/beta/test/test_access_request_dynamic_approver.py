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

from sailpoint.beta.models.access_request_dynamic_approver import AccessRequestDynamicApprover  # noqa: E501


class TestAccessRequestDynamicApprover(unittest.TestCase):
    """AccessRequestDynamicApprover unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestDynamicApprover:
        """Test AccessRequestDynamicApprover
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestDynamicApprover`
        """
        model = AccessRequestDynamicApprover()  # noqa: E501
        if include_optional:
            return AccessRequestDynamicApprover(
                access_request_id = '4b4d982dddff4267ab12f0f1e72b5a6d',
                requested_for = sailpoint.beta.models.access_item_requested_for_dto.AccessItemRequestedForDto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
                requested_items = [
                    sailpoint.beta.models.access_request_dynamic_approver_requested_items_inner.AccessRequestDynamicApprover_requestedItems_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Engineering Access', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access for his day to day job activities.', )
                    ],
                requested_by = sailpoint.beta.models.access_item_requester_dto.AccessItemRequesterDto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', )
            )
        else:
            return AccessRequestDynamicApprover(
                access_request_id = '4b4d982dddff4267ab12f0f1e72b5a6d',
                requested_for = sailpoint.beta.models.access_item_requested_for_dto.AccessItemRequestedForDto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
                requested_items = [
                    sailpoint.beta.models.access_request_dynamic_approver_requested_items_inner.AccessRequestDynamicApprover_requestedItems_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Engineering Access', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access for his day to day job activities.', )
                    ],
                requested_by = sailpoint.beta.models.access_item_requester_dto.AccessItemRequesterDto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
        )
        """

    def testAccessRequestDynamicApprover(self):
        """Test AccessRequestDynamicApprover"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
