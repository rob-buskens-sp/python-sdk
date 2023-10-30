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

from beta.models.sp_config_export_results import SpConfigExportResults  # noqa: E501

class TestSpConfigExportResults(unittest.TestCase):
    """SpConfigExportResults unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpConfigExportResults:
        """Test SpConfigExportResults
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpConfigExportResults`
        """
        model = SpConfigExportResults()  # noqa: E501
        if include_optional:
            return SpConfigExportResults(
                version = 1,
                timestamp = '2021-05-11T22:23:16Z',
                tenant = 'sample-tenant',
                description = 'Export Job 1 Test',
                options = beta.models.export_options.ExportOptions(
                    exclude_types = [
                        'SOURCE'
                        ], 
                    include_types = [
                        'TRIGGER_SUBSCRIPTION'
                        ], 
                    object_options = {TRIGGER_SUBSCRIPTION={includedIds=[be9e116d-08e1-49fc-ab7f-fa585e96c9e4], includedNames=[Test 2]}}, ),
                objects = [
                    beta.models.config_object_for_export_and_import.Config Object for Export and Import(
                        version = 1, 
                        self = beta.models.base_reference_dto.BaseReferenceDto(
                            type = 'IDENTITY', 
                            id = '2c91808568c529c60168cca6f90c1313', 
                            name = 'William Wilson', ), 
                        object = { }, )
                    ]
            )
        else:
            return SpConfigExportResults(
        )
        """

    def testSpConfigExportResults(self):
        """Test SpConfigExportResults"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
