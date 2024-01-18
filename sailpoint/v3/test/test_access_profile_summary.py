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

from sailpoint.v3.models.access_profile_summary import AccessProfileSummary


class TestAccessProfileSummary(unittest.TestCase):
    """AccessProfileSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessProfileSummary:
        """Test AccessProfileSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessProfileSummary`
        """
        model = AccessProfileSummary()
        if include_optional:
            return AccessProfileSummary(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'John Doe',
                display_name = 'John Q. Doe',
                type = 'IDENTITY',
                description = '',
                source = sailpoint.v3.models.reference.Reference(
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'John Doe', ),
                owner = None,
                revocable = True
            )
        else:
            return AccessProfileSummary(
        )
        """

    def testAccessProfileSummary(self):
        """Test AccessProfileSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
