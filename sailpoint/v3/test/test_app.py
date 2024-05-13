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

from sailpoint.v3.models.app import App

class TestApp(unittest.TestCase):
    """App unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> App:
        """Test App
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `App`
        """
        model = App()
        if include_optional:
            return App(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'John Doe',
                source = sailpoint.v3.models.reference_1.Reference_1(
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'John Doe', ),
                account = sailpoint.v3.models.app_all_of_account.App_allOf_account(
                    id = '2c9180837dfe6949017e21f3d8cd6d49', 
                    account_id = 'CN=Carol Adams,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=sailpointdemo,DC=com', )
            )
        else:
            return App(
        )
        """

    def testApp(self):
        """Test App"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
