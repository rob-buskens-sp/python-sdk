# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from cc.models.list_applications200_response_inner_owner import ListApplications200ResponseInnerOwner  # noqa: E501

class TestListApplications200ResponseInnerOwner(unittest.TestCase):
    """ListApplications200ResponseInnerOwner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplications200ResponseInnerOwner:
        """Test ListApplications200ResponseInnerOwner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplications200ResponseInnerOwner`
        """
        model = ListApplications200ResponseInnerOwner()  # noqa: E501
        if include_optional:
            return ListApplications200ResponseInnerOwner(
                id = '',
                name = ''
            )
        else:
            return ListApplications200ResponseInnerOwner(
        )
        """

    def testListApplications200ResponseInnerOwner(self):
        """Test ListApplications200ResponseInnerOwner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
