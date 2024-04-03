# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.identity_summary import IdentitySummary

class TestIdentitySummary(unittest.TestCase):
    """IdentitySummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentitySummary:
        """Test IdentitySummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentitySummary`
        """
        model = IdentitySummary()
        if include_optional:
            return IdentitySummary(
                id = 'ff80818155fe8c080155fe8d925b0316',
                name = 'SailPoint Services',
                identity_id = 'c15b9f5cca5a4e9599eaa0e64fa921bd',
                completed = True
            )
        else:
            return IdentitySummary(
        )
        """

    def testIdentitySummary(self):
        """Test IdentitySummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
