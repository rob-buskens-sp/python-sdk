# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.api.certification_summaries_api import CertificationSummariesApi


class TestCertificationSummariesApi(unittest.TestCase):
    """CertificationSummariesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificationSummariesApi()

    def tearDown(self) -> None:
        pass

    def test_get_identity_access_summaries(self) -> None:
        """Test case for get_identity_access_summaries

        Access Summaries
        """
        pass

    def test_get_identity_decision_summary(self) -> None:
        """Test case for get_identity_decision_summary

        Summary of Certification Decisions
        """
        pass

    def test_get_identity_summaries(self) -> None:
        """Test case for get_identity_summaries

        Identity Summaries for Campaign Certification
        """
        pass

    def test_get_identity_summary(self) -> None:
        """Test case for get_identity_summary

        Summary for Identity
        """
        pass


if __name__ == '__main__':
    unittest.main()
