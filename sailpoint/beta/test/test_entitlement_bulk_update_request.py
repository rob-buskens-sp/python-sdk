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

from sailpoint.beta.models.entitlement_bulk_update_request import EntitlementBulkUpdateRequest

class TestEntitlementBulkUpdateRequest(unittest.TestCase):
    """EntitlementBulkUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitlementBulkUpdateRequest:
        """Test EntitlementBulkUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitlementBulkUpdateRequest`
        """
        model = EntitlementBulkUpdateRequest()
        if include_optional:
            return EntitlementBulkUpdateRequest(
                entitlement_ids = [2c91808a7624751a01762f19d665220d, 2c91808a7624751a01762f19d67c220e, 2c91808a7624751a01762f19d692220f],
                json_patch = [{op=replace, path=/privileged, value=false}, {op=replace, path=/requestable, value=false}]
            )
        else:
            return EntitlementBulkUpdateRequest(
                entitlement_ids = [2c91808a7624751a01762f19d665220d, 2c91808a7624751a01762f19d67c220e, 2c91808a7624751a01762f19d692220f],
                json_patch = [{op=replace, path=/privileged, value=false}, {op=replace, path=/requestable, value=false}],
        )
        """

    def testEntitlementBulkUpdateRequest(self):
        """Test EntitlementBulkUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
