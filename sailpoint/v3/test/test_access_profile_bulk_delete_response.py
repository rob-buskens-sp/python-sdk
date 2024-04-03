# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.access_profile_bulk_delete_response import AccessProfileBulkDeleteResponse

class TestAccessProfileBulkDeleteResponse(unittest.TestCase):
    """AccessProfileBulkDeleteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfileBulkDeleteResponse:
        """Test AccessProfileBulkDeleteResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfileBulkDeleteResponse`
        """
        model = AccessProfileBulkDeleteResponse()
        if include_optional:
            return AccessProfileBulkDeleteResponse(
                task_id = '2c9180867817ac4d017817c491119a20',
                pending = [2c91808876438bbb017668c21919ecca, 2c91808876438bb201766e129f151816],
                in_use = [
                    sailpoint.v3.models.access_profile_usage.AccessProfileUsage(
                        access_profile_id = '2c91808876438bbb017668c21919ecca', 
                        used_by = [
                            sailpoint.v3.models.access_profile_usage_used_by_inner.AccessProfileUsage_usedBy_inner(
                                type = 'ROLE', 
                                id = '2c8180857a9b3da0017aa03418480f9d', 
                                name = 'Manager Role', )
                            ], )
                    ]
            )
        else:
            return AccessProfileBulkDeleteResponse(
        )
        """

    def testAccessProfileBulkDeleteResponse(self):
        """Test AccessProfileBulkDeleteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
