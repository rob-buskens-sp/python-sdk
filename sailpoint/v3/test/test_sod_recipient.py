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

from sailpoint.v3.models.sod_recipient import SodRecipient


class TestSodRecipient(unittest.TestCase):
    """SodRecipient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SodRecipient:
        """Test SodRecipient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodRecipient`
        """
        model = SodRecipient()
        if include_optional:
            return SodRecipient(
                type = 'IDENTITY',
                id = '2c7180a46faadee4016fb4e018c20642',
                name = 'Michael Michaels'
            )
        else:
            return SodRecipient(
        )
        """

    def testSodRecipient(self):
        """Test SodRecipient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
