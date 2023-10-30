# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from beta.api.certifications_api import CertificationsApi  # noqa: E501


class TestCertificationsApi(unittest.TestCase):
    """CertificationsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CertificationsApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_identity_certification_item_permissions(self) -> None:
        """Test case for get_identity_certification_item_permissions

        Permissions for Entitlement Certification Item  # noqa: E501
        """
        pass

    def test_get_identity_certification_pending_tasks(self) -> None:
        """Test case for get_identity_certification_pending_tasks

        Pending Certification Tasks  # noqa: E501
        """
        pass

    def test_get_identity_certification_task_status(self) -> None:
        """Test case for get_identity_certification_task_status

        Certification Task Status  # noqa: E501
        """
        pass

    def test_list_certification_reviewers(self) -> None:
        """Test case for list_certification_reviewers

        List of Reviewers for certification  # noqa: E501
        """
        pass

    def test_submit_reassign_certs_async(self) -> None:
        """Test case for submit_reassign_certs_async

        Reassign Certifications Asynchronously  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
