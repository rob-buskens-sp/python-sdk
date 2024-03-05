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

from sailpoint.beta.models.search_form_definitions_by_tenant400_response import SearchFormDefinitionsByTenant400Response

class TestSearchFormDefinitionsByTenant400Response(unittest.TestCase):
    """SearchFormDefinitionsByTenant400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchFormDefinitionsByTenant400Response:
        """Test SearchFormDefinitionsByTenant400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchFormDefinitionsByTenant400Response`
        """
        model = SearchFormDefinitionsByTenant400Response()
        if include_optional:
            return SearchFormDefinitionsByTenant400Response(
                detail_code = '',
                messages = [
                    sailpoint.beta.models.error_message_is_the_standard_api_error_response_message_type/.ErrorMessage is the standard API error response message type.(
                        locale = 'en-US', 
                        locale_origin = 'DEFAULT', 
                        text = 'This is an error', )
                    ],
                status_code = 56,
                tracking_id = ''
            )
        else:
            return SearchFormDefinitionsByTenant400Response(
        )
        """

    def testSearchFormDefinitionsByTenant400Response(self):
        """Test SearchFormDefinitionsByTenant400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
