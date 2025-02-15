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

from sailpoint.v3.models.query import Query

class TestQuery(unittest.TestCase):
    """Query unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Query:
        """Test Query
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Query`
        """
        model = Query()
        if include_optional:
            return Query(
                query = 'name:a*',
                fields = [name],
                time_zone = 'America/Chicago',
                inner_hit = sailpoint.v3.models.inner_hit.InnerHit(
                    query = 'source.name:\"Active Directory\"', 
                    type = 'access', )
            )
        else:
            return Query(
        )
        """

    def testQuery(self):
        """Test Query"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
