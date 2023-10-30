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

from beta.models.cancelable_account_activity import CancelableAccountActivity  # noqa: E501

class TestCancelableAccountActivity(unittest.TestCase):
    """CancelableAccountActivity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CancelableAccountActivity:
        """Test CancelableAccountActivity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CancelableAccountActivity`
        """
        model = CancelableAccountActivity()  # noqa: E501
        if include_optional:
            return CancelableAccountActivity(
                id = '2c9180835d2e5168015d32f890ca1581',
                name = '2c9180835d2e5168015d32f890ca1581',
                created = '2017-07-11T18:45:37.098Z',
                modified = '2018-06-25T20:22:28.104Z',
                completed = '2018-10-19T13:49:37.385Z',
                completion_status = 'SUCCESS',
                type = 'appRequest',
                requester_identity_summary = beta.models.identity_summary.IdentitySummary(
                    id = 'ff80818155fe8c080155fe8d925b0316', 
                    name = 'SailPoint Services', 
                    identity_id = 'c15b9f5cca5a4e9599eaa0e64fa921bd', 
                    completed = True, ),
                target_identity_summary = beta.models.identity_summary.IdentitySummary(
                    id = 'ff80818155fe8c080155fe8d925b0316', 
                    name = 'SailPoint Services', 
                    identity_id = 'c15b9f5cca5a4e9599eaa0e64fa921bd', 
                    completed = True, ),
                errors = [sailpoint.connector.ConnectorException: java.lang.InterruptedException: Timeout waiting for response to message 0 from client 57a4ab97-ab3f-4aef-9fe2-0eaf15c73d26 after 60 seconds.],
                warnings = [
                    ''
                    ],
                items = [
                    beta.models.account_activity_item.AccountActivityItem(
                        id = '48c545831b264409a81befcabb0e3c5a', 
                        name = '48c545831b264409a81befcabb0e3c5a', 
                        requested = '2017-07-11T18:45:37.098Z', 
                        approval_status = 'FINISHED', 
                        provisioning_status = 'PENDING', 
                        requester_comment = beta.models.comment.Comment(
                            commenter_id = '2c918084660f45d6016617daa9210584', 
                            commenter_name = 'Adam Kennedy', 
                            body = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat.', 
                            date = '2017-07-11T18:45:37.098Z', ), 
                        reviewer_identity_summary = beta.models.identity_summary.IdentitySummary(
                            id = 'ff80818155fe8c080155fe8d925b0316', 
                            name = 'SailPoint Services', 
                            identity_id = 'c15b9f5cca5a4e9599eaa0e64fa921bd', 
                            completed = True, ), 
                        reviewer_comment = beta.models.comment.Comment(
                            commenter_id = '2c918084660f45d6016617daa9210584', 
                            commenter_name = 'Adam Kennedy', 
                            body = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat.', 
                            date = '2017-07-11T18:45:37.098Z', ), 
                        operation = 'ADD', 
                        attribute = 'detectedRoles', 
                        value = 'Treasury Analyst [AccessProfile-1529010191212]', 
                        native_identity = 'Sandie.Camero', 
                        source_id = '2c91808363ef85290164000587130c0c', 
                        account_request_info = beta.models.account_request_info.AccountRequestInfo(
                            requested_object_id = '2c91808563ef85690164001c31140c0c', 
                            requested_object_name = 'Treasury Analyst', 
                            requested_object_type = 'ACCESS_PROFILE', ), 
                        client_metadata = {customKey1=custom value 1, customKey2=custom value 2}, 
                        remove_date = '2020-07-11T00:00Z', )
                    ],
                execution_status = 'COMPLETED',
                client_metadata = {
                    'key' : ''
                    },
                cancelable = True,
                cancel_comment = beta.models.comment.Comment(
                    commenter_id = '2c918084660f45d6016617daa9210584', 
                    commenter_name = 'Adam Kennedy', 
                    body = 'Et quam massa maximus vivamus nisi ut urna tincidunt metus elementum erat.', 
                    date = '2017-07-11T18:45:37.098Z', )
            )
        else:
            return CancelableAccountActivity(
        )
        """

    def testCancelableAccountActivity(self):
        """Test CancelableAccountActivity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
