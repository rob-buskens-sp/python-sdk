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

from beta.models.non_employee_source import NonEmployeeSource  # noqa: E501

class TestNonEmployeeSource(unittest.TestCase):
    """NonEmployeeSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NonEmployeeSource:
        """Test NonEmployeeSource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeSource`
        """
        model = NonEmployeeSource()  # noqa: E501
        if include_optional:
            return NonEmployeeSource(
                id = 'a0303682-5e4a-44f7-bdc2-6ce6112549c1',
                source_id = '2c91808568c529c60168cca6f90c1313',
                name = 'Retail',
                description = 'Source description',
                approvers = [
                    beta.models.identity_reference_with_id.IdentityReferenceWithId(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', )
                    ],
                account_managers = [
                    beta.models.identity_reference_with_id.IdentityReferenceWithId(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', )
                    ],
                modified = '2019-08-23T18:52:59.162Z',
                created = '2019-08-23T18:40:35.772Z',
                non_employee_count = 2
            )
        else:
            return NonEmployeeSource(
        )
        """

    def testNonEmployeeSource(self):
        """Test NonEmployeeSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
