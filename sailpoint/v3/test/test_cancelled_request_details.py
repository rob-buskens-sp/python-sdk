# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.v3.models.cancelled_request_details import CancelledRequestDetails  # noqa: E501


class TestCancelledRequestDetails(unittest.TestCase):
    """CancelledRequestDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CancelledRequestDetails:
        """Test CancelledRequestDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CancelledRequestDetails`
        """
        model = CancelledRequestDetails()  # noqa: E501
        if include_optional:
            return CancelledRequestDetails(
                comment = 'This request must be cancelled.',
                owner = sailpoint.v3.models.owner_dto.OwnerDto(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'Support', ),
                modified = '2019-12-20T09:17:12.192Z'
            )
        else:
            return CancelledRequestDetails(
        )
        """

    def testCancelledRequestDetails(self):
        """Test CancelledRequestDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
