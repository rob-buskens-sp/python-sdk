# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.beta.api.mfa_controller_api import MFAControllerApi


class TestMFAControllerApi(unittest.TestCase):
    """MFAControllerApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MFAControllerApi()

    def tearDown(self) -> None:
        pass

    def test_create_send_token(self) -> None:
        """Test case for create_send_token

        Create and send user token
        """
        pass

    def test_ping_verification_status(self) -> None:
        """Test case for ping_verification_status

        Polling MFA method by VerificationPollRequest
        """
        pass

    def test_send_duo_verify_request(self) -> None:
        """Test case for send_duo_verify_request

        Verifying authentication via Duo method
        """
        pass

    def test_send_kba_answers(self) -> None:
        """Test case for send_kba_answers

        Authenticate KBA provided MFA method
        """
        pass

    def test_send_okta_verify_request(self) -> None:
        """Test case for send_okta_verify_request

        Verifying authentication via Okta method
        """
        pass

    def test_send_token_auth_request(self) -> None:
        """Test case for send_token_auth_request

        Authenticate Token provided MFA method
        """
        pass


if __name__ == '__main__':
    unittest.main()
