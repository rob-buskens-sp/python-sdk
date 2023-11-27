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

from sailpoint.beta.models.template_dto_default import TemplateDtoDefault  # noqa: E501


class TestTemplateDtoDefault(unittest.TestCase):
    """TemplateDtoDefault unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TemplateDtoDefault:
        """Test TemplateDtoDefault
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TemplateDtoDefault`
        """
        model = TemplateDtoDefault()  # noqa: E501
        if include_optional:
            return TemplateDtoDefault(
                key = 'cloud_manual_work_item_summary',
                name = 'Task Manager Subscription',
                medium = 'EMAIL',
                locale = 'en',
                subject = 'You have $numberOfPendingTasks $taskTasks to complete in ${__global.productName}.',
                header = '',
                body = 'Please go to the task manager',
                footer = '',
                var_from = '$__global.emailFromAddress',
                reply_to = '$__global.emailFromAddress',
                description = 'Daily digest - sent if number of outstanding tasks for task owner > 0'
            )
        else:
            return TemplateDtoDefault(
        )
        """

    def testTemplateDtoDefault(self):
        """Test TemplateDtoDefault"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
