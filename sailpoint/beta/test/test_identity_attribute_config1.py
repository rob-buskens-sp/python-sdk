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

from beta.models.identity_attribute_config1 import IdentityAttributeConfig1  # noqa: E501

class TestIdentityAttributeConfig1(unittest.TestCase):
    """IdentityAttributeConfig1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityAttributeConfig1:
        """Test IdentityAttributeConfig1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityAttributeConfig1`
        """
        model = IdentityAttributeConfig1()  # noqa: E501
        if include_optional:
            return IdentityAttributeConfig1(
                enabled = True,
                attribute_transforms = [
                    beta.models.identity_attribute_transform_1.IdentityAttributeTransform_1(
                        identity_attribute_name = 'email', 
                        transform_definition = beta.models.transform_definition_1.TransformDefinition_1(
                            type = 'accountAttribute', 
                            attributes = {attributeName=e-mail, sourceName=MySource, sourceId=2c9180877a826e68017a8c0b03da1a53}, ), )
                    ]
            )
        else:
            return IdentityAttributeConfig1(
        )
        """

    def testIdentityAttributeConfig1(self):
        """Test IdentityAttributeConfig1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
