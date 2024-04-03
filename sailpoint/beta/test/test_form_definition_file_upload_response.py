# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.form_definition_file_upload_response import FormDefinitionFileUploadResponse

class TestFormDefinitionFileUploadResponse(unittest.TestCase):
    """FormDefinitionFileUploadResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormDefinitionFileUploadResponse:
        """Test FormDefinitionFileUploadResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormDefinitionFileUploadResponse`
        """
        model = FormDefinitionFileUploadResponse()
        if include_optional:
            return FormDefinitionFileUploadResponse(
                created = '2023-07-12T20:14:57.74486Z',
                file_id = '01FHZXHK8PTP9FVK99Z66GXQTX.png',
                form_definition_id = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return FormDefinitionFileUploadResponse(
        )
        """

    def testFormDefinitionFileUploadResponse(self):
        """Test FormDefinitionFileUploadResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
