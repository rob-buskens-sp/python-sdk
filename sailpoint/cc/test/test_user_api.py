# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from cc.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_get_identity(self) -> None:
        """Test case for get_identity

        Get Single Identity  # noqa: E501
        """
        pass

    def test_update_user_permissions(self) -> None:
        """Test case for update_user_permissions

        Update User Permissions  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
