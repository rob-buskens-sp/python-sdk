# coding: utf-8

"""
    SailPoint SaaS API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.v2.models.bulk_delete_work_groups200_response import BulkDeleteWorkGroups200Response


class TestBulkDeleteWorkGroups200Response(unittest.TestCase):
    """BulkDeleteWorkGroups200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> BulkDeleteWorkGroups200Response:
        """Test BulkDeleteWorkGroups200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BulkDeleteWorkGroups200Response`
        """
        model = BulkDeleteWorkGroups200Response()
        if include_optional:
            return BulkDeleteWorkGroups200Response(
                deleted = [
                    '4518f275-e7de-40b8-9951-b67d6273421c'
                    ],
                in_use = [
                    '12538dlg-60d0-44b4-9273-d1ba578ef384'
                    ],
                not_found = [
                    '12538ecf-60d0-44b4-9273-d1ba578ef384'
                    ]
            )
        else:
            return BulkDeleteWorkGroups200Response(
        )
        """

    def testBulkDeleteWorkGroups200Response(self):
        """Test BulkDeleteWorkGroups200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
