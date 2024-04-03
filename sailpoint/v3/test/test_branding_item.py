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

from sailpoint.v3.models.branding_item import BrandingItem

class TestBrandingItem(unittest.TestCase):
    """BrandingItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BrandingItem:
        """Test BrandingItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BrandingItem`
        """
        model = BrandingItem()
        if include_optional:
            return BrandingItem(
                name = 'default',
                product_name = 'product name',
                action_button_color = '0074D9',
                active_link_color = '011E69',
                navigation_color = '011E69',
                email_from_address = 'no-reply@sailpoint.com',
                standard_logo_url = '',
                login_informational_message = ''
            )
        else:
            return BrandingItem(
        )
        """

    def testBrandingItem(self):
        """Test BrandingItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
