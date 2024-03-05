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

from sailpoint.beta.models.entitlement_access_request_config import EntitlementAccessRequestConfig

class TestEntitlementAccessRequestConfig(unittest.TestCase):
    """EntitlementAccessRequestConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EntitlementAccessRequestConfig:
        """Test EntitlementAccessRequestConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EntitlementAccessRequestConfig`
        """
        model = EntitlementAccessRequestConfig()
        if include_optional:
            return EntitlementAccessRequestConfig(
                approval_schemes = [
                    sailpoint.beta.models.entitlement_approval_scheme.EntitlementApprovalScheme(
                        approver_type = 'GOVERNANCE_GROUP', 
                        approver_id = 'e3eab852-8315-467f-9de7-70eda97f63c8', )
                    ],
                request_comment_required = True,
                denial_comment_required = False
            )
        else:
            return EntitlementAccessRequestConfig(
        )
        """

    def testEntitlementAccessRequestConfig(self):
        """Test EntitlementAccessRequestConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
