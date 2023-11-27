# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.v3.api.certification_campaigns_api import CertificationCampaignsApi  # noqa: E501


class TestCertificationCampaignsApi(unittest.TestCase):
    """CertificationCampaignsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificationCampaignsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_complete_campaign(self) -> None:
        """Test case for complete_campaign

        Complete a Campaign  # noqa: E501
        """
        pass

    def test_create_campaign(self) -> None:
        """Test case for create_campaign

        Create a campaign  # noqa: E501
        """
        pass

    def test_create_campaign_template(self) -> None:
        """Test case for create_campaign_template

        Create a Campaign Template  # noqa: E501
        """
        pass

    def test_delete_campaign_template(self) -> None:
        """Test case for delete_campaign_template

        Delete a Campaign Template  # noqa: E501
        """
        pass

    def test_delete_campaign_template_schedule(self) -> None:
        """Test case for delete_campaign_template_schedule

        Deletes a Campaign Template's Schedule  # noqa: E501
        """
        pass

    def test_delete_campaigns(self) -> None:
        """Test case for delete_campaigns

        Deletes Campaigns  # noqa: E501
        """
        pass

    def test_get_active_campaigns(self) -> None:
        """Test case for get_active_campaigns

        List Campaigns  # noqa: E501
        """
        pass

    def test_get_campaign(self) -> None:
        """Test case for get_campaign

        Get a campaign  # noqa: E501
        """
        pass

    def test_get_campaign_reports(self) -> None:
        """Test case for get_campaign_reports

        Get Campaign Reports  # noqa: E501
        """
        pass

    def test_get_campaign_reports_config(self) -> None:
        """Test case for get_campaign_reports_config

        Get Campaign Reports Configuration  # noqa: E501
        """
        pass

    def test_get_campaign_template(self) -> None:
        """Test case for get_campaign_template

        Get a Campaign Template  # noqa: E501
        """
        pass

    def test_get_campaign_template_schedule(self) -> None:
        """Test case for get_campaign_template_schedule

        Gets a Campaign Template's Schedule  # noqa: E501
        """
        pass

    def test_list_campaign_templates(self) -> None:
        """Test case for list_campaign_templates

        List Campaign Templates  # noqa: E501
        """
        pass

    def test_move(self) -> None:
        """Test case for move

        Reassign Certifications  # noqa: E501
        """
        pass

    def test_patch_campaign_template(self) -> None:
        """Test case for patch_campaign_template

        Update a Campaign Template  # noqa: E501
        """
        pass

    def test_set_campaign_reports_config(self) -> None:
        """Test case for set_campaign_reports_config

        Set Campaign Reports Configuration  # noqa: E501
        """
        pass

    def test_set_campaign_template_schedule(self) -> None:
        """Test case for set_campaign_template_schedule

        Sets a Campaign Template's Schedule  # noqa: E501
        """
        pass

    def test_start_campaign(self) -> None:
        """Test case for start_campaign

        Activate a Campaign  # noqa: E501
        """
        pass

    def test_start_campaign_remediation_scan(self) -> None:
        """Test case for start_campaign_remediation_scan

        Run Campaign Remediation Scan  # noqa: E501
        """
        pass

    def test_start_campaign_report(self) -> None:
        """Test case for start_campaign_report

        Run Campaign Report  # noqa: E501
        """
        pass

    def test_start_generate_campaign_template(self) -> None:
        """Test case for start_generate_campaign_template

        Generate a Campaign from Template  # noqa: E501
        """
        pass

    def test_update_campaign(self) -> None:
        """Test case for update_campaign

        Update a Campaign  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
