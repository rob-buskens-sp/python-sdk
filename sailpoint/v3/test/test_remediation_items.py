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

from sailpoint.v3.models.remediation_items import RemediationItems


class TestRemediationItems(unittest.TestCase):
    """RemediationItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RemediationItems:
        """Test RemediationItems
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RemediationItems`
        """
        model = RemediationItems()
        if include_optional:
            return RemediationItems(
                id = '2c9180835d2e5168015d32f890ca1581',
                target_id = '2c9180835d2e5168015d32f890ca1581',
                target_name = 'john.smith',
                target_display_name = 'emailAddress',
                application_name = 'Active Directory',
                attribute_name = 'phoneNumber',
                attribute_operation = 'update',
                attribute_value = '512-555-1212',
                native_identity = 'jason.smith2'
            )
        else:
            return RemediationItems(
        )
        """

    def testRemediationItems(self):
        """Test RemediationItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
