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

from sailpoint.v3.models.base_document import BaseDocument


class TestBaseDocument(unittest.TestCase):
    """BaseDocument unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BaseDocument:
        """Test BaseDocument
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseDocument`
        """
        model = BaseDocument()
        if include_optional:
            return BaseDocument(
                id = '2c91808375d8e80a0175e1f88a575222',
                name = 'john.doe',
                type = 'identity'
            )
        else:
            return BaseDocument(
                id = '2c91808375d8e80a0175e1f88a575222',
                name = 'john.doe',
                type = 'identity',
        )
        """

    def testBaseDocument(self):
        """Test BaseDocument"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
