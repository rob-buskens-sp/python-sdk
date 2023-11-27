# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.cc.models.get_application200_response import GetApplication200Response  # noqa: E501


class TestGetApplication200Response(unittest.TestCase):
    """GetApplication200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetApplication200Response:
        """Test GetApplication200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetApplication200Response`
        """
        model = GetApplication200Response()  # noqa: E501
        if include_optional:
            return GetApplication200Response(
                id = '',
                app_id = '',
                service_id = '',
                service_app_id = '',
                name = '',
                description = '',
                app_center_enabled = True,
                provision_request_enabled = True,
                control_type = '',
                mobile = True,
                private_app = True,
                script_name = '',
                status = '',
                icon = '',
                health = sailpoint.cc.models.list_applications_200_response_inner_health.listApplications_200_response_inner_health(
                    status = '', 
                    last_changed = '', 
                    since = 1.337, 
                    healthy = True, ),
                enable_sso = True,
                sso_method = '',
                has_links = True,
                has_automations = True,
                step_up_auth_data = None,
                step_up_auth_type = '',
                usage_analytics = True,
                usage_cert_required = True,
                usage_cert_text = None,
                launchpad_enabled = True,
                password_managed = True,
                owner = sailpoint.cc.models.list_applications_200_response_inner_owner.listApplications_200_response_inner_owner(
                    id = '', 
                    name = '', ),
                date_created = 1.337,
                last_updated = 1.337,
                default_access_profile = None,
                service = '',
                selected_sso_method = '',
                supported_sso_methods = 1.337,
                off_network_blocked_roles = None,
                supported_off_network = '',
                account_service_id = 1.337,
                launcher_count = 1.337,
                account_service_name = '',
                account_service_external_id = '',
                account_service_match_all_accounts = True,
                external_id = '',
                account_service_use_for_password_management = True,
                account_service_policy_id = '',
                account_service_policy_name = '',
                require_strong_authn = True,
                account_service_policies = [
                    sailpoint.cc.models.list_applications_200_response_inner_account_service_policies_inner.listApplications_200_response_inner_accountServicePolicies_inner(
                        policy_id = '', 
                        policy_name = '', 
                        selectors = sailpoint.cc.models.selectors.selectors(), )
                    ],
                xsd_version = '',
                app_profiles = [
                    sailpoint.cc.models.list_applications_200_response_inner_app_profiles_inner.listApplications_200_response_inner_appProfiles_inner(
                        id = 1.337, 
                        filename = '', 
                        created_by = '', 
                        date_created = '', 
                        xsd_version = '', )
                    ],
                password_service_id = 1.337,
                access_profile_ids = None
            )
        else:
            return GetApplication200Response(
        )
        """

    def testGetApplication200Response(self):
        """Test GetApplication200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
