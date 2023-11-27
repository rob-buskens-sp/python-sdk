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

from sailpoint.v3.models.approval_reminder_and_escalation_config import ApprovalReminderAndEscalationConfig  # noqa: E501


class TestApprovalReminderAndEscalationConfig(unittest.TestCase):
    """ApprovalReminderAndEscalationConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> ApprovalReminderAndEscalationConfig:
        """Test ApprovalReminderAndEscalationConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApprovalReminderAndEscalationConfig`
        """
        model = ApprovalReminderAndEscalationConfig()  # noqa: E501
        if include_optional:
            return ApprovalReminderAndEscalationConfig(
                days_until_escalation = 0,
                days_between_reminders = 0,
                max_reminders = 1,
                fallback_approver_ref = sailpoint.v3.models.identity_reference_with_name_and_email.IdentityReferenceWithNameAndEmail(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', 
                    name = 'Alison Ferguso', 
                    email = 'alison.ferguso@identitysoon.com', )
            )
        else:
            return ApprovalReminderAndEscalationConfig(
        )
        """

    def testApprovalReminderAndEscalationConfig(self):
        """Test ApprovalReminderAndEscalationConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
