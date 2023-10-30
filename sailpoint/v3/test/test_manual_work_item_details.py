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

from v3.models.manual_work_item_details import ManualWorkItemDetails  # noqa: E501

class TestManualWorkItemDetails(unittest.TestCase):
    """ManualWorkItemDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManualWorkItemDetails:
        """Test ManualWorkItemDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManualWorkItemDetails`
        """
        model = ManualWorkItemDetails()  # noqa: E501
        if include_optional:
            return ManualWorkItemDetails(
                forwarded = True,
                original_owner = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                current_owner = v3.models.base_reference_dto.BaseReferenceDto(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'William Wilson', ),
                modified = '2019-08-23T18:52:57.398Z',
                status = 'PENDING',
                forward_history = [
                    v3.models.approval_forward_history.ApprovalForwardHistory(
                        old_approver_name = 'Frank Mir', 
                        new_approver_name = 'Al Volta', 
                        comment = 'Forwarding from Frank to Al', 
                        modified = '2019-08-23T18:52:57.398Z', 
                        forwarder_name = 'William Wilson', 
                        reassignment_type = 'AUTOMATIC_REASSIGNMENT', )
                    ]
            )
        else:
            return ManualWorkItemDetails(
        )
        """

    def testManualWorkItemDetails(self):
        """Test ManualWorkItemDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
