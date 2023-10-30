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

from beta.models.password_sync_group import PasswordSyncGroup  # noqa: E501

class TestPasswordSyncGroup(unittest.TestCase):
    """PasswordSyncGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PasswordSyncGroup:
        """Test PasswordSyncGroup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PasswordSyncGroup`
        """
        model = PasswordSyncGroup()  # noqa: E501
        if include_optional:
            return PasswordSyncGroup(
                id = '6881f631-3bd5-4213-9c75-8e05cc3e35dd',
                name = 'Password Sync Group 1',
                password_policy_id = '2c91808d744ba0ce01746f93b6204501',
                source_ids = [2c918084660f45d6016617daa9210584, 2c918084660f45d6016617daa9210500]
            )
        else:
            return PasswordSyncGroup(
        )
        """

    def testPasswordSyncGroup(self):
        """Test PasswordSyncGroup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
