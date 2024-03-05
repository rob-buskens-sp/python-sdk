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

from sailpoint.beta.models.requestable_object import RequestableObject

class TestRequestableObject(unittest.TestCase):
    """RequestableObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RequestableObject:
        """Test RequestableObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RequestableObject`
        """
        model = RequestableObject()
        if include_optional:
            return RequestableObject(
                id = '2c9180835d2e5168015d32f890ca1581',
                name = 'Applied Research Access',
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-06-25T20:22:28.104Z',
                description = 'Access to research information, lab results, and schematics.',
                type = 'ACCESS_PROFILE',
                request_status = None,
                identity_request_id = '',
                owner_ref = sailpoint.beta.models.identity_reference_with_name_and_email.IdentityReferenceWithNameAndEmail(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', 
                    name = 'Alison Ferguso', 
                    email = 'alison.ferguso@identitysoon.com', ),
                request_comments_required = False
            )
        else:
            return RequestableObject(
        )
        """

    def testRequestableObject(self):
        """Test RequestableObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
