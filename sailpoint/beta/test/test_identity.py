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

from beta.models.identity import Identity  # noqa: E501

class TestIdentity(unittest.TestCase):
    """Identity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Identity:
        """Test Identity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Identity`
        """
        model = Identity()  # noqa: E501
        if include_optional:
            return Identity(
                id = 'id12345',
                name = 'aName',
                created = '2023-01-03T21:16:22.432Z',
                modified = '2023-01-03T21:16:22.432Z',
                alias = 'walter.white',
                email_address = 'sender@example.com',
                processing_state = 'ERROR',
                identity_status = 'LOCKED',
                manager_ref = beta.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                is_manager = True,
                last_refresh = '2020-11-22T15:42:31.123Z',
                attributes = {"uid":"Walter White","firstname":"walter","cloudStatus":"UNREGISTERED","displayName":"Walter White","identificationNumber":"942","lastSyncDate":1470348809380,"email":"walter@gmail.com","lastname":"white"},
                lifecycle_state = beta.models.lifecycle_state_dto.LifecycleStateDto(
                    state_name = 'active', 
                    manually_updated = True, )
            )
        else:
            return Identity(
                name = 'aName',
        )
        """

    def testIdentity(self):
        """Test Identity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
