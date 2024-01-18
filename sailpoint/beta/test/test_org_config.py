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

from sailpoint.beta.models.org_config import OrgConfig


class TestOrgConfig(unittest.TestCase):
    """OrgConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrgConfig:
        """Test OrgConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrgConfig`
        """
        model = OrgConfig()
        if include_optional:
            return OrgConfig(
                org_name = 'acme-solar',
                time_zone = 'America/Toronto',
                lcs_change_honors_source_enable_feature = False,
                arm_customer_id = 'DE38E75A-5FF6-4A65-5DC7-08D64426B09E',
                arm_sap_system_id_mappings = '[{sourceId=2c91808c791a94e501792388b0d62659, systemId=1556}, {sourceId=2_2c91808c791a94e501792388b0d62659, systemId=2_1556}, {sourceId=3_2c91808c791a94e501792388b0d62659, systemId=3_1556}]',
                arm_auth = 'epiYNTRYA2S7swisDWk1Zv4VMNgvqEjiBh5_ufuCWsma2m-5XADijqBg0ijXLby5nS6lxZNXabhGnAPGeDGc4V3jQKrhwV-UHypRLs8ZLgOjiQNus9NimS0uPdKomRW6TFWqXyfnYd-znNgbbVuwUy9GyD9ebDVJSntPastxSx7UcyGuWBqfNZYpuxKRWe_7TVY60qL55jUqyz8N4XUbbdcxdbZ0uik6ut-Bv90MKTbZexBW_PR4qcgIkaEs4kIenLyBxnGziYo7AO0tJ8bGHO8FJRkibCpAQIt7PISLo7Gg_Xf9j10dKq2YDgy4pPTvz3fE2ZHYnXCXvXFSA-vVag==',
                arm_db = 'EU',
                arm_sso_url = 'https://your-arm-sso-url',
                iai_enable_certification_recommendations = True,
                sod_report_configs = [
                    sailpoint.beta.models.report_config_dto.ReportConfigDTO(
                        column_name = 'SOD Business Name', 
                        required = True, 
                        included = False, 
                        order = 2, )
                    ]
            )
        else:
            return OrgConfig(
        )
        """

    def testOrgConfig(self):
        """Test OrgConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
