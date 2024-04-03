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

from sailpoint.v3.models.non_employee_request import NonEmployeeRequest

class TestNonEmployeeRequest(unittest.TestCase):
    """NonEmployeeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NonEmployeeRequest:
        """Test NonEmployeeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NonEmployeeRequest`
        """
        model = NonEmployeeRequest()
        if include_optional:
            return NonEmployeeRequest(
                id = 'a0303682-5e4a-44f7-bdc2-6ce6112549c1',
                source_id = '2c91808568c529c60168cca6f90c1313',
                name = 'Retail',
                description = 'Source description',
                account_name = 'william.smith',
                first_name = 'William',
                last_name = 'Smith',
                email = 'william.smith@example.com',
                phone = '5555555555',
                manager = 'jane.doe',
                non_employee_source = sailpoint.v3.models.non_employee_source_lite.NonEmployeeSourceLite(
                    id = 'a0303682-5e4a-44f7-bdc2-6ce6112549c1', 
                    source_id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'Retail', 
                    description = 'Source description', ),
                data = {description=Auditing},
                approval_items = [
                    sailpoint.v3.models.non_employee_approval_item_base.NonEmployeeApprovalItemBase(
                        id = '2c1e388b-1e55-4b0a-ab5c-897f1204159c', 
                        approver = sailpoint.v3.models.non_employee_identity_reference_with_id.NonEmployeeIdentityReferenceWithId(
                            type = 'IDENTITY', 
                            id = '5168015d32f890ca15812c9180835d2e', ), 
                        account_name = 'test.account', 
                        approval_status = 'APPROVED', 
                        approval_order = 1, 
                        comment = 'I approve', 
                        modified = '2019-08-23T18:52:59.162Z', 
                        created = '2019-08-23T18:40:35.772Z', )
                    ],
                approval_status = 'APPROVED',
                comment = 'approved',
                completion_date = '2020-03-24T11:11:41.139-05:00',
                start_date = '2020-03-24T00:00-05:00',
                end_date = '2021-03-25T00:00-05:00',
                modified = '2020-03-24T11:11:41.139-05:00',
                created = '2020-03-24T11:11:41.139-05:00'
            )
        else:
            return NonEmployeeRequest(
        )
        """

    def testNonEmployeeRequest(self):
        """Test NonEmployeeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
