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

from beta.models.sod_policy_schedule import SodPolicySchedule  # noqa: E501

class TestSodPolicySchedule(unittest.TestCase):
    """SodPolicySchedule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SodPolicySchedule:
        """Test SodPolicySchedule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SodPolicySchedule`
        """
        model = SodPolicySchedule()  # noqa: E501
        if include_optional:
            return SodPolicySchedule(
                name = 'SCH-1584312283015',
                created = '2020-01-01T00:00Z',
                modified = '2020-01-01T00:00Z',
                description = 'Schedule for policy xyz',
                schedule = beta.models.schedule_1.Schedule_1(
                    type = 'WEEKLY', 
                    days = null, 
                    hours = null, 
                    expiration = '2018-06-25T20:22:28.104Z', 
                    time_zone_id = 'GMT-06:00', ),
                recipients = [
                    beta.models.base_reference_dto.BaseReferenceDto(
                        type = 'IDENTITY', 
                        id = '2c91808568c529c60168cca6f90c1313', 
                        name = 'William Wilson', )
                    ],
                email_empty_results = False,
                creator_id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                modifier_id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde'
            )
        else:
            return SodPolicySchedule(
        )
        """

    def testSodPolicySchedule(self):
        """Test SodPolicySchedule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
