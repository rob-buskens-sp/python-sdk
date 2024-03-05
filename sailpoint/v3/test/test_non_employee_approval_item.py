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

from sailpoint.v3.models.non_employee_approval_item import NonEmployeeApprovalItem

class TestNonEmployeeApprovalItem(unittest.TestCase):
    """NonEmployeeApprovalItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NonEmployeeApprovalItem:
        """Test NonEmployeeApprovalItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeApprovalItem`
        """
        model = NonEmployeeApprovalItem()
        if include_optional:
            return NonEmployeeApprovalItem(
                id = '2c1e388b-1e55-4b0a-ab5c-897f1204159c',
                approver = sailpoint.v3.models.non_employee_identity_reference_with_id.NonEmployeeIdentityReferenceWithId(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', ),
                account_name = 'test.account',
                approval_status = 'APPROVED',
                approval_order = 1,
                comment = 'I approve',
                modified = '2019-08-23T18:52:59.162Z',
                created = '2019-08-23T18:40:35.772Z',
                non_employee_request = sailpoint.v3.models.non_employee_request_lite.NonEmployeeRequestLite(
                    id = 'ac110005-7156-1150-8171-5b292e3e0084', 
                    requester = sailpoint.v3.models.non_employee_identity_reference_with_id.NonEmployeeIdentityReferenceWithId(
                        type = 'IDENTITY', 
                        id = '5168015d32f890ca15812c9180835d2e', ), )
            )
        else:
            return NonEmployeeApprovalItem(
        )
        """

    def testNonEmployeeApprovalItem(self):
        """Test NonEmployeeApprovalItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
