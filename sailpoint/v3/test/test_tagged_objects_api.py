# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest

from sailpoint.v3.api.tagged_objects_api import TaggedObjectsApi


class TestTaggedObjectsApi(unittest.TestCase):
    """TaggedObjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TaggedObjectsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_tagged_object(self) -> None:
        """Test case for delete_tagged_object

        Delete Tagged Object
        """
        pass

    def test_delete_tags_to_many_object(self) -> None:
        """Test case for delete_tags_to_many_object

        Remove Tags from Multiple Objects
        """
        pass

    def test_get_tagged_object(self) -> None:
        """Test case for get_tagged_object

        Get Tagged Object
        """
        pass

    def test_list_tagged_objects(self) -> None:
        """Test case for list_tagged_objects

        List Tagged Objects
        """
        pass

    def test_list_tagged_objects_by_type(self) -> None:
        """Test case for list_tagged_objects_by_type

        List Tagged Objects
        """
        pass

    def test_put_tagged_object(self) -> None:
        """Test case for put_tagged_object

        Update Tagged Object
        """
        pass

    def test_set_tag_to_object(self) -> None:
        """Test case for set_tag_to_object

        Add Tag to Object
        """
        pass

    def test_set_tags_to_many_objects(self) -> None:
        """Test case for set_tags_to_many_objects

        Tag Multiple Objects
        """
        pass


if __name__ == '__main__':
    unittest.main()
