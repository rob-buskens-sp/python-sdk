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

from sailpoint.beta.models.non_employee_request_without_approval_item import NonEmployeeRequestWithoutApprovalItem  # noqa: E501


class TestNonEmployeeRequestWithoutApprovalItem(unittest.TestCase):
    """NonEmployeeRequestWithoutApprovalItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
            self, include_optional) -> NonEmployeeRequestWithoutApprovalItem:
        """Test NonEmployeeRequestWithoutApprovalItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeRequestWithoutApprovalItem`
        """
        model = NonEmployeeRequestWithoutApprovalItem()  # noqa: E501
        if include_optional:
            return NonEmployeeRequestWithoutApprovalItem(
                id = '',
                requester = sailpoint.beta.models.identity_reference_with_id.IdentityReferenceWithId(
                    type = 'IDENTITY', 
                    id = '5168015d32f890ca15812c9180835d2e', ),
                account_name = 'william.smith',
                first_name = 'William',
                last_name = 'Smith',
                email = 'william.smith@example.com',
                phone = '5555555555',
                manager = 'jane.doe',
                non_employee_source = None,
                data = {
                    'key' : ''
                    },
                approval_status = 'APPROVED',
                comment = '',
                completion_date = '2020-03-24T11:11:41.139-05:00',
                start_date = 'Mon Mar 23 20:00:00 EDT 2020',
                end_date = 'Wed Mar 24 20:00:00 EDT 2021',
                modified = '2020-03-24T11:11:41.139-05:00',
                created = '2020-03-24T11:11:41.139-05:00'
            )
        else:
            return NonEmployeeRequestWithoutApprovalItem(
        )
        """

    def testNonEmployeeRequestWithoutApprovalItem(self):
        """Test NonEmployeeRequestWithoutApprovalItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
