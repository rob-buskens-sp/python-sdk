# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import unittest
import datetime

from sailpoint.beta.models.status_response import StatusResponse


class TestStatusResponse(unittest.TestCase):
    """StatusResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StatusResponse:
        """Test StatusResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StatusResponse`
        """
        model = StatusResponse()
        if include_optional:
            return StatusResponse(
                id = '2c91808568c529c60168cca6f90c1313',
                name = 'ODS-AD-Test [source-999999]',
                status = 'SUCCESS',
                elapsed_millis = 1000,
                details = {useTLSForIQService=false, IQService={TLS Port=0, .NET CLR Version=4.0.30319.42000, SecondaryServiceStatus=Running, Port=5050, Host=AUTOMATION-AD, Name=IQService, IQServiceStatus=Running, SecondaryService=IQService-Instance1-Secondary, Version=IQService Sep-2020, secondaryPort=5051, OS Architecture=AMD64, Operating System=Microsoft Windows Server 2012 R2 Standard, highestDotNetVersion=4.8 or later, Build Time=09/22/2020 06:34 AM -0500}, IQServiceClientAuthEnabled=false, requestProcessedOn=1/19/2021 1:47:14 PM}
            )
        else:
            return StatusResponse(
        )
        """

    def testStatusResponse(self):
        """Test StatusResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
