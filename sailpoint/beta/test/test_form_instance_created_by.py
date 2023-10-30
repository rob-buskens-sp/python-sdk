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

from beta.models.form_instance_created_by import FormInstanceCreatedBy  # noqa: E501

class TestFormInstanceCreatedBy(unittest.TestCase):
    """FormInstanceCreatedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FormInstanceCreatedBy:
        """Test FormInstanceCreatedBy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FormInstanceCreatedBy`
        """
        model = FormInstanceCreatedBy()  # noqa: E501
        if include_optional:
            return FormInstanceCreatedBy(
                id = '00000000-0000-0000-0000-000000000000',
                type = 'WORKFLOW_EXECUTION'
            )
        else:
            return FormInstanceCreatedBy(
        )
        """

    def testFormInstanceCreatedBy(self):
        """Test FormInstanceCreatedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
