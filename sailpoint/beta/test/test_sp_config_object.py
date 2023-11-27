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

from sailpoint.beta.models.sp_config_object import SpConfigObject  # noqa: E501


class TestSpConfigObject(unittest.TestCase):
    """SpConfigObject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpConfigObject:
        """Test SpConfigObject
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpConfigObject`
        """
        model = SpConfigObject()  # noqa: E501
        if include_optional:
            return SpConfigObject(
                object_type = 'TRIGGER_SUBSCRIPTION',
                resolve_by_id_url = sailpoint.beta.models.resolver_url_format_for_object_configuration/.Resolver URL Format for Object Configuration.(
                    url = 'ets://trigger-subscriptions/$id', 
                    query = sailpoint.beta.models.query.query(), ),
                resolve_by_name_url = [
                    sailpoint.beta.models.resolver_url_format_for_object_configuration/.Resolver URL Format for Object Configuration.(
                        url = 'ets://trigger-subscriptions/$id', 
                        query = sailpoint.beta.models.query.query(), )
                    ],
                export_url = sailpoint.beta.models.resolver_url_format_for_object_configuration/.Resolver URL Format for Object Configuration.(
                    url = 'ets://trigger-subscriptions/$id', 
                    query = sailpoint.beta.models.query.query(), ),
                export_right = 'idn:trigger-service-subscriptions:read',
                export_limit = 10,
                import_url = sailpoint.beta.models.resolver_url_format_for_object_configuration/.Resolver URL Format for Object Configuration.(
                    url = 'ets://trigger-subscriptions/$id', 
                    query = sailpoint.beta.models.query.query(), ),
                import_right = 'idn:trigger-service-subscriptions:create',
                import_limit = 10,
                reference_extractors = [$.owner],
                signature_required = False
            )
        else:
            return SpConfigObject(
        )
        """

    def testSpConfigObject(self):
        """Test SpConfigObject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
