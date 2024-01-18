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

from sailpoint.beta.models.message_catalog_dto import MessageCatalogDto


class TestMessageCatalogDto(unittest.TestCase):
    """MessageCatalogDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MessageCatalogDto:
        """Test MessageCatalogDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MessageCatalogDto`
        """
        model = MessageCatalogDto()
        if include_optional:
            return MessageCatalogDto(
                locale = 'en_US',
                messages = [
                    sailpoint.beta.models.resource_bundle_message.ResourceBundleMessage(
                        key = 'recommender-api.V2_WEIGHT_FEATURE_PRODUCT_INTERPRETATION_LOW', 
                        format = '{0,,\"i18n hint: percentage\"}% of identities with the same {1,,\"i18n hint: name of category feature\"} have this access. This information had a low impact on the overall score.', )
                    ]
            )
        else:
            return MessageCatalogDto(
        )
        """

    def testMessageCatalogDto(self):
        """Test MessageCatalogDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
