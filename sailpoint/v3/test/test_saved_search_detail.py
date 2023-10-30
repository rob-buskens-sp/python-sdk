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

from v3.models.saved_search_detail import SavedSearchDetail  # noqa: E501

class TestSavedSearchDetail(unittest.TestCase):
    """SavedSearchDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedSearchDetail:
        """Test SavedSearchDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavedSearchDetail`
        """
        model = SavedSearchDetail()  # noqa: E501
        if include_optional:
            return SavedSearchDetail(
                public = False,
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                indices = [identities],
                columns = {identity=[{field=displayName, header=Display Name}, {field=e-mail, header=Work Email}]},
                query = '@accounts(disabled:true)',
                fields = [disabled],
                sort = [displayName],
                filters = None
            )
        else:
            return SavedSearchDetail(
                indices = [identities],
                query = '@accounts(disabled:true)',
        )
        """

    def testSavedSearchDetail(self):
        """Test SavedSearchDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
