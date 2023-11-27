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

from sailpoint.v3.models.base_common_dto import BaseCommonDto  # noqa: E501


class TestBaseCommonDto(unittest.TestCase):
    """BaseCommonDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseCommonDto:
        """Test BaseCommonDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseCommonDto`
        """
        model = BaseCommonDto()  # noqa: E501
        if include_optional:
            return BaseCommonDto(
                id = 'id12345',
                name = 'aName',
                created = '2015-05-28T14:07:17Z',
                modified = '2015-05-28T14:07:17Z'
            )
        else:
            return BaseCommonDto(
                name = 'aName',
        )
        """

    def testBaseCommonDto(self):
        """Test BaseCommonDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
