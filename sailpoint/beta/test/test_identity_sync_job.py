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

from sailpoint.beta.models.identity_sync_job import IdentitySyncJob  # noqa: E501


class TestIdentitySyncJob(unittest.TestCase):
    """IdentitySyncJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentitySyncJob:
        """Test IdentitySyncJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentitySyncJob`
        """
        model = IdentitySyncJob()  # noqa: E501
        if include_optional:
            return IdentitySyncJob(
                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                status = 'IN_PROGRESS',
                payload = sailpoint.beta.models.identity_sync_payload.IdentitySyncPayload(
                    type = 'SYNCHRONIZE_IDENTITY_ATTRIBUTES', 
                    data_json = '{"identityId":"2c918083746f642c01746f990884012a"}', )
            )
        else:
            return IdentitySyncJob(
                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                status = 'IN_PROGRESS',
                payload = sailpoint.beta.models.identity_sync_payload.IdentitySyncPayload(
                    type = 'SYNCHRONIZE_IDENTITY_ATTRIBUTES', 
                    data_json = '{"identityId":"2c918083746f642c01746f990884012a"}', ),
        )
        """

    def testIdentitySyncJob(self):
        """Test IdentitySyncJob"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
