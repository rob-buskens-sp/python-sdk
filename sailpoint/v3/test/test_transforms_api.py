# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.v3.api.transforms_api import TransformsApi


class TestTransformsApi(unittest.TestCase):
    """TransformsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransformsApi()

    def tearDown(self) -> None:
        pass

    def test_create_transform(self) -> None:
        """Test case for create_transform

        Create transform
        """
        pass

    def test_delete_transform(self) -> None:
        """Test case for delete_transform

        Delete a transform
        """
        pass

    def test_get_transform(self) -> None:
        """Test case for get_transform

        Transform by ID
        """
        pass

    def test_list_transforms(self) -> None:
        """Test case for list_transforms

        List transforms
        """
        pass

    def test_update_transform(self) -> None:
        """Test case for update_transform

        Update a transform
        """
        pass


if __name__ == '__main__':
    unittest.main()
