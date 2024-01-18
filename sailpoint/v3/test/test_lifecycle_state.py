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

from sailpoint.v3.models.lifecycle_state import LifecycleState


class TestLifecycleState(unittest.TestCase):
    """LifecycleState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LifecycleState:
        """Test LifecycleState
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LifecycleState`
        """
        model = LifecycleState()
        if include_optional:
            return LifecycleState(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z',
                enabled = True,
                technical_name = 'Technical Name',
                description = 'Lifecycle description',
                identity_count = 42,
                email_notification_option = sailpoint.v3.models.email_notification_option.EmailNotificationOption(
                    notify_managers = True, 
                    notify_all_admins = True, 
                    notify_specific_users = True, 
                    email_address_list = [test@test.com, test2@test.com], ),
                account_actions = [
                    sailpoint.v3.models.account_action.AccountAction(
                        action = 'ENABLE', 
                        source_ids = [2c918084660f45d6016617daa9210584, 2c918084660f45d6016617daa9210500], )
                    ],
                access_profile_ids = [2c918084660f45d6016617daa9210584, 2c918084660f45d6016617daa9210500]
            )
        else:
            return LifecycleState(
                name = 'aName',
                technical_name = 'Technical Name',
        )
        """

    def testLifecycleState(self):
        """Test LifecycleState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
