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

from v2.models.create_workgroup_request import CreateWorkgroupRequest  # noqa: E501

class TestCreateWorkgroupRequest(unittest.TestCase):
    """CreateWorkgroupRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateWorkgroupRequest:
        """Test CreateWorkgroupRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateWorkgroupRequest`
        """
        model = CreateWorkgroupRequest()  # noqa: E501
        if include_optional:
            return CreateWorkgroupRequest(
                name = 'Test group 3',
                description = 'This is a test',
                owner = v2.models.create_workgroup_request_owner.createWorkgroup_request_owner(
                    id = '2c9180867624cbd7017642d8c8c81f67', )
            )
        else:
            return CreateWorkgroupRequest(
        )
        """

    def testCreateWorkgroupRequest(self):
        """Test CreateWorkgroupRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
