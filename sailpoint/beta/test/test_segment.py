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

from sailpoint.beta.models.segment import Segment

class TestSegment(unittest.TestCase):
    """Segment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Segment:
        """Test Segment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Segment`
        """
        model = Segment()
        if include_optional:
            return Segment(
                id = '0f11f2a4-7c94-4bf3-a2bd-742580fe3bde',
                name = 'segment-xyz',
                created = '2020-01-01T00:00Z',
                modified = '2020-01-01T00:00Z',
                description = 'This segment represents xyz',
                owner = sailpoint.beta.models.owner_reference_segments.OwnerReferenceSegments(
                    type = 'IDENTITY', 
                    id = '2c9180a46faadee4016fb4e018c20639', 
                    name = 'support', ),
                visibility_criteria = sailpoint.beta.models.visibility_criteria.VisibilityCriteria(
                    expression = sailpoint.beta.models.expression.Expression(
                        operator = 'EQUALS', 
                        attribute = 'location', 
                        value = sailpoint.beta.models.value.Value(
                            type = 'STRING', ), 
                        children = [], ), ),
                active = True
            )
        else:
            return Segment(
        )
        """

    def testSegment(self):
        """Test Segment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
