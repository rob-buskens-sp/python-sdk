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

from sailpoint.v3.models.reassignment_trail_dto import ReassignmentTrailDTO

class TestReassignmentTrailDTO(unittest.TestCase):
    """ReassignmentTrailDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReassignmentTrailDTO:
        """Test ReassignmentTrailDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReassignmentTrailDTO`
        """
        model = ReassignmentTrailDTO()
        if include_optional:
            return ReassignmentTrailDTO(
                previous_owner = 'ef38f94347e94562b5bb8424a56397d8',
                new_owner = 'ef38f94347e94562b5bb8424a56397a3',
                reassignment_type = 'AUTOMATIC_REASSIGNMENT'
            )
        else:
            return ReassignmentTrailDTO(
        )
        """

    def testReassignmentTrailDTO(self):
        """Test ReassignmentTrailDTO"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
