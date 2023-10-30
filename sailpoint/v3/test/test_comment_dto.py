# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from v3.models.comment_dto import CommentDto  # noqa: E501

class TestCommentDto(unittest.TestCase):
    """CommentDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommentDto:
        """Test CommentDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommentDto`
        """
        model = CommentDto()  # noqa: E501
        if include_optional:
            return CommentDto(
                comment = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat',
                author = v3.models.comment_dto_author.CommentDto_author(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'Adam Kennedy', ),
                created = '2017-07-11T18:45:37.098Z'
            )
        else:
            return CommentDto(
        )
        """

    def testCommentDto(self):
        """Test CommentDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
