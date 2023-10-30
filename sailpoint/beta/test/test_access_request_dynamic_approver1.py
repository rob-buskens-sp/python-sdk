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

from beta.models.access_request_dynamic_approver1 import AccessRequestDynamicApprover1  # noqa: E501

class TestAccessRequestDynamicApprover1(unittest.TestCase):
    """AccessRequestDynamicApprover1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessRequestDynamicApprover1:
        """Test AccessRequestDynamicApprover1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessRequestDynamicApprover1`
        """
        model = AccessRequestDynamicApprover1()  # noqa: E501
        if include_optional:
            return AccessRequestDynamicApprover1(
                id = '2c91808b6ef1d43e016efba0ce470906',
                name = 'Adam Adams',
                type = IDENTITY
            )
        else:
            return AccessRequestDynamicApprover1(
                id = '2c91808b6ef1d43e016efba0ce470906',
                name = 'Adam Adams',
                type = IDENTITY,
        )
        """

    def testAccessRequestDynamicApprover1(self):
        """Test AccessRequestDynamicApprover1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
