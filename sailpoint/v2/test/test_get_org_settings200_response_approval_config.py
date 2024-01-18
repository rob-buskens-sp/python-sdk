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

from sailpoint.v2.models.get_org_settings200_response_approval_config import GetOrgSettings200ResponseApprovalConfig


class TestGetOrgSettings200ResponseApprovalConfig(unittest.TestCase):
    """GetOrgSettings200ResponseApprovalConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self, include_optional) -> GetOrgSettings200ResponseApprovalConfig:
        """Test GetOrgSettings200ResponseApprovalConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetOrgSettings200ResponseApprovalConfig`
        """
        model = GetOrgSettings200ResponseApprovalConfig()
        if include_optional:
            return GetOrgSettings200ResponseApprovalConfig(
                days_till_escalation = 56,
                days_between_reminders = 56,
                max_reminders = 56,
                fallback_approver = ''
            )
        else:
            return GetOrgSettings200ResponseApprovalConfig(
                days_till_escalation = 56,
                days_between_reminders = 56,
                max_reminders = 56,
                fallback_approver = '',
        )
        """

    def testGetOrgSettings200ResponseApprovalConfig(self):
        """Test GetOrgSettings200ResponseApprovalConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
