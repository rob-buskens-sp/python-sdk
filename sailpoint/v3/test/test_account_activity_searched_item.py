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

from v3.models.account_activity_searched_item import AccountActivitySearchedItem  # noqa: E501

class TestAccountActivitySearchedItem(unittest.TestCase):
    """AccountActivitySearchedItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountActivitySearchedItem:
        """Test AccountActivitySearchedItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountActivitySearchedItem`
        """
        model = AccountActivitySearchedItem()  # noqa: E501
        if include_optional:
            return AccountActivitySearchedItem(
                id = '2c91808375d8e80a0175e1f88a575222',
                name = 'john.doe',
                type = 'identity',
                action = 'Identity Refresh.',
                created = '2018-06-25T20:22:28.104Z',
                modified = '2018-06-25T20:22:28.104Z',
                stage = 'Completed',
                origin = '',
                status = 'Complete',
                requester = None,
                recipient = None,
                tracking_number = '61aad0c9e8134eca89e76a35e0cabe3f',
                errors = [
                    ''
                    ],
                warnings = [
                    ''
                    ],
                approvals = [
                    v3.models.approval.Approval(
                        comments = [
                            v3.models.approval_comment.ApprovalComment(
                                comment = 'This request was autoapproved by our automated ETS subscriber.', 
                                commenter = 'Automated AR Approval', 
                                date = '2018-06-25T20:22:28.104Z', )
                            ], 
                        created = '2018-06-25T20:22:28.104Z', 
                        modified = '2018-06-25T20:22:28.104Z', 
                        owner = null, 
                        result = 'Finished', 
                        type = '', )
                    ],
                original_requests = [
                    v3.models.original_request.OriginalRequest(
                        account_id = 'CN=Abby Smith,OU=Austin,OU=Americas,OU=Demo,DC=seri,DC=acme,DC=com', 
                        attribute_requests = [
                            v3.models.attribute_request.AttributeRequest(
                                name = 'groups', 
                                op = 'Add', 
                                value = '3203537556531076', )
                            ], 
                        op = 'add', 
                        source = null, )
                    ],
                expansion_items = [
                    v3.models.expansion_item.ExpansionItem(
                        account_id = '2c91808981f58ea601821c3e93482e6f', 
                        cause = 'Role', 
                        name = 'smartsheet-role', 
                        attribute_requests = [
                            v3.models.attribute_request.AttributeRequest(
                                name = 'groups', 
                                op = 'Add', 
                                value = '3203537556531076', )
                            ], 
                        source = null, )
                    ],
                account_requests = [
                    v3.models.account_request.AccountRequest(
                        account_id = 'John.Doe', 
                        attribute_requests = [
                            v3.models.attribute_request.AttributeRequest(
                                name = 'groups', 
                                op = 'Add', 
                                value = '3203537556531076', )
                            ], 
                        op = 'Modify', 
                        provisioning_target = null, 
                        result = v3.models.account_request_result.AccountRequest_result(
                            errors = [
                                '[ConnectorError] [
  {
    "code": "unrecognized_keys",
    "keys": [
      "groups"
    ],
    "path": [],
    "message": "Unrecognized key(s) in object: 'groups'"
  }
] (requestId: 5e9d6df5-9b1b-47d9-9bf1-dc3a2893299e)'
                                ], 
                            status = 'failed', 
                            ticket_id = '', ), 
                        source = null, )
                    ],
                sources = 'smartsheet-test, airtable-v4, IdentityNow'
            )
        else:
            return AccountActivitySearchedItem(
                id = '2c91808375d8e80a0175e1f88a575222',
                name = 'john.doe',
                type = 'identity',
        )
        """

    def testAccountActivitySearchedItem(self):
        """Test AccountActivitySearchedItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
