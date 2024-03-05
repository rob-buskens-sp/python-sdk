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

from sailpoint.beta.models.import_options import ImportOptions

class TestImportOptions(unittest.TestCase):
    """ImportOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImportOptions:
        """Test ImportOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImportOptions`
        """
        model = ImportOptions()
        if include_optional:
            return ImportOptions(
                exclude_types = [
                    'SOURCE'
                    ],
                include_types = [
                    'TRIGGER_SUBSCRIPTION'
                    ],
                object_options = {TRIGGER_SUBSCRIPTION={includedIds=[be9e116d-08e1-49fc-ab7f-fa585e96c9e4], includedNames=[Test 2]}},
                default_references = [
                    'TRIGGER_SUBSCRIPTION'
                    ],
                exclude_backup = False
            )
        else:
            return ImportOptions(
        )
        """

    def testImportOptions(self):
        """Test ImportOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
