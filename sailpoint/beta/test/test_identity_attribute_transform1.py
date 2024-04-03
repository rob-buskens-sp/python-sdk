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

from sailpoint.beta.models.identity_attribute_transform1 import IdentityAttributeTransform1

class TestIdentityAttributeTransform1(unittest.TestCase):
    """IdentityAttributeTransform1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityAttributeTransform1:
        """Test IdentityAttributeTransform1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityAttributeTransform1`
        """
        model = IdentityAttributeTransform1()
        if include_optional:
            return IdentityAttributeTransform1(
                identity_attribute_name = 'email',
                transform_definition = sailpoint.beta.models.transform_definition_1.TransformDefinition_1(
                    type = 'accountAttribute', 
                    attributes = {attributeName=e-mail, sourceName=MySource, sourceId=2c9180877a826e68017a8c0b03da1a53}, )
            )
        else:
            return IdentityAttributeTransform1(
        )
        """

    def testIdentityAttributeTransform1(self):
        """Test IdentityAttributeTransform1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
