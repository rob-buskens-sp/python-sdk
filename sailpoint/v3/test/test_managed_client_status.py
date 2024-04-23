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

from sailpoint.v3.models.managed_client_status import ManagedClientStatus

class TestManagedClientStatus(unittest.TestCase):
    """ManagedClientStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedClientStatus:
        """Test ManagedClientStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedClientStatus`
        """
        model = ManagedClientStatus()
        if include_optional:
            return ManagedClientStatus(
                body = {alertKey=, id=5678, clusterId=1234, ccg_etag=ccg_etag123xyz456, ccg_pin=NONE, cookbook_etag=20210420125956-20210511144538, hostname=megapod-useast1-secret-hostname.sailpoint.com, internal_ip=127.0.0.1, lastSeen=1620843964604, sinceSeen=14708, sinceSeenMillis=14708, localDev=false, stacktrace=, state=null, status=NORMAL, uuid=null, product=idn, va_version=null, platform_version=2, os_version=2345.3.1, os_type=flatcar, hypervisor=unknown},
                status = 'NORMAL',
                type = 'CCG',
                timestamp = '2020-01-01T00:00Z'
            )
        else:
            return ManagedClientStatus(
                body = {alertKey=, id=5678, clusterId=1234, ccg_etag=ccg_etag123xyz456, ccg_pin=NONE, cookbook_etag=20210420125956-20210511144538, hostname=megapod-useast1-secret-hostname.sailpoint.com, internal_ip=127.0.0.1, lastSeen=1620843964604, sinceSeen=14708, sinceSeenMillis=14708, localDev=false, stacktrace=, state=null, status=NORMAL, uuid=null, product=idn, va_version=null, platform_version=2, os_version=2345.3.1, os_type=flatcar, hypervisor=unknown},
                status = 'NORMAL',
                type = 'CCG',
                timestamp = '2020-01-01T00:00Z',
        )
        """

    def testManagedClientStatus(self):
        """Test ManagedClientStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
