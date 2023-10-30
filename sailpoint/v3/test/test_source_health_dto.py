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

from v3.models.source_health_dto import SourceHealthDto  # noqa: E501

class TestSourceHealthDto(unittest.TestCase):
    """SourceHealthDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SourceHealthDto:
        """Test SourceHealthDto
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SourceHealthDto`
        """
        model = SourceHealthDto()  # noqa: E501
        if include_optional:
            return SourceHealthDto(
                id = '2c91808568c529c60168cca6f90c1324',
                type = 'OpenLDAP - Direct',
                name = 'Source1234',
                org = 'denali-cjh',
                is_authoritative = False,
                is_cluster = False,
                hostname = 'megapod-useast1-secret-hostname.sailpoint.com',
                pod = 'megapod-useast1',
                iq_service_version = 'iqVersion123',
                status = 'SOURCE_STATE_UNCHECKED_SOURCE'
            )
        else:
            return SourceHealthDto(
        )
        """

    def testSourceHealthDto(self):
        """Test SourceHealthDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
