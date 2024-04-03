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

from sailpoint.beta.models.resource_objects_response import ResourceObjectsResponse

class TestResourceObjectsResponse(unittest.TestCase):
    """ResourceObjectsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResourceObjectsResponse:
        """Test ResourceObjectsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResourceObjectsResponse`
        """
        model = ResourceObjectsResponse()
        if include_optional:
            return ResourceObjectsResponse(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'ODS-AD-Test [source-999999]',
                object_count = 25,
                elapsed_millis = 1055,
                resource_objects = [
                    sailpoint.beta.models.resource_object.Resource Object(
                        instance = '', 
                        identity = 'CN=Aaron Carr,OU=test1,DC=test2,DC=test', 
                        uuid = '{abf7bd9b-68b4-4d21-9b70-870c58ebf844}', 
                        previous_identity = '', 
                        name = 'Aaron Carr', 
                        object_type = 'account', 
                        incomplete = False, 
                        incremental = False, 
                        delete = False, 
                        remove = False, 
                        missing = [missFieldOne, missFieldTwo], 
                        attributes = {telephoneNumber=12-(345)678-9012, mail=example@test.com, displayName=Aaron Carr}, 
                        final_update = False, )
                    ]
            )
        else:
            return ResourceObjectsResponse(
        )
        """

    def testResourceObjectsResponse(self):
        """Test ResourceObjectsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
