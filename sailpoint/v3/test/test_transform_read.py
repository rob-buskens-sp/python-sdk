# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.transform_read import TransformRead

class TestTransformRead(unittest.TestCase):
    """TransformRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransformRead:
        """Test TransformRead
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransformRead`
        """
        model = TransformRead()
        if include_optional:
            return TransformRead(
                name = 'Timestamp To Date',
                type = 'dateFormat',
                attributes = None,
                id = '2cd78adghjkja34jh2b1hkjhasuecd',
                internal = False
            )
        else:
            return TransformRead(
                name = 'Timestamp To Date',
                type = 'dateFormat',
                attributes = None,
                id = '2cd78adghjkja34jh2b1hkjhasuecd',
                internal = False,
        )
        """

    def testTransformRead(self):
        """Test TransformRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
