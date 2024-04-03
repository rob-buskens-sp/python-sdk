# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from sailpoint.v3.api.personal_access_tokens_api import PersonalAccessTokensApi


class TestPersonalAccessTokensApi(unittest.TestCase):
    """PersonalAccessTokensApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PersonalAccessTokensApi()

    def tearDown(self) -> None:
        pass

    def test_create_personal_access_token(self) -> None:
        """Test case for create_personal_access_token

        Create Personal Access Token
        """
        pass

    def test_delete_personal_access_token(self) -> None:
        """Test case for delete_personal_access_token

        Delete Personal Access Token
        """
        pass

    def test_list_personal_access_tokens(self) -> None:
        """Test case for list_personal_access_tokens

        List Personal Access Tokens
        """
        pass

    def test_patch_personal_access_token(self) -> None:
        """Test case for patch_personal_access_token

        Patch Personal Access Token
        """
        pass


if __name__ == '__main__':
    unittest.main()
