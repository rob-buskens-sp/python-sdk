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

from sailpoint.beta.models.trigger_example_input import TriggerExampleInput  # noqa: E501


class TestTriggerExampleInput(unittest.TestCase):
    """TriggerExampleInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TriggerExampleInput:
        """Test TriggerExampleInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TriggerExampleInput`
        """
        model = TriggerExampleInput()  # noqa: E501
        if include_optional:
            return TriggerExampleInput(
                access_request_id = '2c91808b6ef1d43e016efba0ce470904',
                requested_for = sailpoint.beta.models.access_item_requested_for_dto.AccessItemRequestedForDto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
                requested_items = [
                    sailpoint.beta.models.access_request_pre_approval_requested_items_inner.AccessRequestPreApproval_requestedItems_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Access to engineering database', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access to do his job.', )
                    ],
                requested_by = sailpoint.beta.models.access_item_requester_dto.AccessItemRequesterDto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                requested_items_status = [
                    sailpoint.beta.models.access_request_post_approval_requested_items_status_inner.AccessRequestPostApproval_requestedItemsStatus_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Access to engineering database', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access to do his job.', 
                        client_metadata = {applicationName=My application}, 
                        approval_info = [
                            sailpoint.beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner(
                                approval_comment = 'This access looks good.  Approved.', 
                                approval_decision = APPROVED, 
                                approver_name = 'Stephen.Austin', 
                                approver = sailpoint.beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner_approver(
                                    type = IDENTITY, ), )
                            ], )
                    ],
                source = sailpoint.beta.models.account_uncorrelated_source.AccountUncorrelated_source(
                    type = 'SOURCE', 
                    id = '2c6180835d191a86015d28455b4b231b', 
                    name = 'Corporate Directory', ),
                status = Success,
                started = '2020-06-29T22:01:50.474Z',
                completed = '2020-06-29T22:02:04.090Z',
                errors = [
                    'Connector AD Failed'
                    ],
                warnings = [
                    'Notification Skipped due to invalid email'
                    ],
                stats = sailpoint.beta.models.accounts_collected_for_aggregation_stats.AccountsCollectedForAggregation_stats(
                    scanned = 200, 
                    unchanged = 190, 
                    changed = 6, 
                    added = 4, 
                    removed = 3, ),
                identity = sailpoint.beta.models.identity_deleted_identity.IdentityDeleted_identity(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                account = sailpoint.beta.models.account_uncorrelated_account.AccountUncorrelated_account(
                    type = ACCOUNT, 
                    id = '4dd497e3723e439991cb6d0e478375dd', 
                    name = 'Sadie Jensen', 
                    native_identity = 'cn=john.doe,ou=users,dc=acme,dc=com', 
                    uuid = '1cb1f07d-3e5a-4431-becd-234fa4306108', ),
                changes = [
                    sailpoint.beta.models.identity_attributes_changed_changes_inner.IdentityAttributesChanged_changes_inner(
                        attribute = 'department', 
                        old_value = sales, 
                        new_value = marketing, )
                    ],
                attributes = {firstname=John, lastname=Doe, email=john.doe@gmail.com, department=Sales, displayName=John Doe, created=2020-04-27T16:48:33.597Z, employeeNumber=E009, uid=E009, inactive=true, phone=null, identificationNumber=E009},
                entitlement_count = 0,
                campaign = sailpoint.beta.models.campaign_generated_campaign.CampaignGenerated_campaign(
                    id = '2c91808576f886190176f88cac5a0010', 
                    name = 'Manager Access Campaign', 
                    description = 'Audit access for all employees.', 
                    created = '2021-02-16T03:04:45.815Z', 
                    modified = '2021-02-17T03:04:45.815Z', 
                    deadline = '2021-02-18T03:04:45.815Z', 
                    type = MANAGER, 
                    campaign_owner = sailpoint.beta.models.campaign_generated_campaign_campaign_owner.CampaignGenerated_campaign_campaignOwner(
                        id = '37f080867702c1910177031320c40n27', 
                        display_name = 'John Snow', 
                        email = 'john.snow@example.com', ), 
                    status = STAGED, ),
                certification = sailpoint.beta.models.certification_signed_off_certification.CertificationSignedOff_certification(
                    id = '2c91808576f886190176f88caf0d0067', 
                    name = 'Manager Access Review for Alice Baker', 
                    created = '2020-02-16T03:04:45.815Z', 
                    modified = '2020-02-16T03:06:45.815Z', ),
                tracking_number = '4b4d982dddff4267ab12f0f1e72b5a6d',
                sources = 'Corp AD, Corp LDAP, Corp Salesforce',
                action = 'IdentityRefresh',
                recipient = sailpoint.beta.models.provisioning_completed_recipient.ProvisioningCompleted_recipient(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                requester = sailpoint.beta.models.provisioning_completed_requester.ProvisioningCompleted_requester(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                account_requests = [
                    sailpoint.beta.models.provisioning_completed_account_requests_inner.ProvisioningCompleted_accountRequests_inner(
                        source = sailpoint.beta.models.provisioning_completed_account_requests_inner_source.ProvisioningCompleted_accountRequests_inner_source(
                            id = '4e4d982dddff4267ab12f0f1e72b5a6d', 
                            type = 'SOURCE', 
                            name = 'Corporate Active Directory', ), 
                        account_id = 'CN=Chewy.Bacca,ou=hardcorefigter,ou=wookies,dc=starwars,dc=com', 
                        account_operation = 'Modify', 
                        provisioning_result = SUCCESS, 
                        provisioning_target = 'Corp AD', 
                        ticket_id = '72619262', 
                        attribute_requests = [
                            sailpoint.beta.models.provisioning_completed_account_requests_inner_attribute_requests_inner.ProvisioningCompleted_accountRequests_inner_attributeRequests_inner(
                                attribute_name = 'memberOf', 
                                attribute_value = 'CN=jedi,DC=starwars,DC=com', 
                                operation = Add, )
                            ], )
                    ],
                file_name = 'Modified.zip',
                owner_email = 'test@sailpoint.com',
                owner_name = 'Cloud Support',
                query = 'modified:[now-7y/d TO now]',
                search_name = 'Modified Activity',
                search_results = sailpoint.beta.models.saved_search_complete_search_results.SavedSearchComplete_searchResults(
                    account = sailpoint.beta.models.saved_search_complete_search_results_account.SavedSearchComplete_searchResults_Account(
                        count = '3', 
                        noun = 'accounts', 
                        preview = [
                            []
                            ], ), 
                    entitlement = sailpoint.beta.models.saved_search_complete_search_results_entitlement.SavedSearchComplete_searchResults_Entitlement(
                        count = '2', 
                        noun = 'entitlements', 
                        preview = [
                            []
                            ], ), 
                    identity = sailpoint.beta.models.saved_search_complete_search_results_identity.SavedSearchComplete_searchResults_Identity(
                        count = '2', 
                        noun = 'identities', 
                        preview = [
                            []
                            ], ), ),
                signed_s3_url = 'https://sptcbu-org-data-useast1.s3.amazonaws.com/arsenal-john/reports/Events%20Export.2020-05-06%2018%2759%20GMT.3e580592-86e4-4953-8aea-49e6ef20a086.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200506T185919Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=AKIAV5E54XOGTS4Q4L7A%2F20200506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2e732bb97a12a1fd8a215613e3c31fcdae8ba1fb6a25916843ab5b51d2ddefbc',
                uuid = 'b7264868-7201-415f-9118-b581d431c688',
                id = '2c9180866166b5b0016167c32ef31a66',
                native_identifier = 'E009',
                source_id = '2c918082814e693601816e09471b29b6',
                source_name = 'Active Directory',
                identity_id = 'ee769173319b41d19ccec6c235423237b',
                identity_name = 'john.doe',
                name = 'Corporate Active Directory',
                type = 'DIRECT_CONNECT',
                created = '2020-06-29T22:01:50.474Z',
                connector = 'active-directory',
                actor = sailpoint.beta.models.source_updated_actor.SourceUpdated_actor(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                deleted = '2021-03-29T22:01:50.474Z',
                modified = '2021-03-29T22:01:50.474Z',
                application = sailpoint.beta.models.va_cluster_status_change_event_application.VAClusterStatusChangeEvent_application(
                    id = '2c9180866166b5b0016167c32ef31a66', 
                    name = 'Production VA Cluster', 
                    attributes = { }, ),
                health_check_result = sailpoint.beta.models.va_cluster_status_change_event_health_check_result.VAClusterStatusChangeEvent_healthCheckResult(
                    message = 'Test Connection failed with exception. Error message - java.lang Exception', 
                    result_type = 'SOURCE_STATE_ERROR_CLUSTER', 
                    status = Succeeded, ),
                previous_health_check_result = sailpoint.beta.models.va_cluster_status_change_event_previous_health_check_result.VAClusterStatusChangeEvent_previousHealthCheckResult(
                    message = 'Test Connection failed with exception. Error message - java.lang Exception', 
                    result_type = 'SOURCE_STATE_ERROR_CLUSTER', 
                    status = Failed, )
            )
        else:
            return TriggerExampleInput(
                access_request_id = '2c91808b6ef1d43e016efba0ce470904',
                requested_for = sailpoint.beta.models.access_item_requested_for_dto.AccessItemRequestedForDto(
                    type = 'IDENTITY', 
                    id = '2c4180a46faadee4016fb4e018c20626', 
                    name = 'Robert Robinson', ),
                requested_items = [
                    sailpoint.beta.models.access_request_pre_approval_requested_items_inner.AccessRequestPreApproval_requestedItems_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Access to engineering database', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access to do his job.', )
                    ],
                requested_by = sailpoint.beta.models.access_item_requester_dto.AccessItemRequesterDto(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                requested_items_status = [
                    sailpoint.beta.models.access_request_post_approval_requested_items_status_inner.AccessRequestPostApproval_requestedItemsStatus_inner(
                        id = '2c91808b6ef1d43e016efba0ce470904', 
                        name = 'Engineering Access', 
                        description = 'Access to engineering database', 
                        type = ACCESS_PROFILE, 
                        operation = Add, 
                        comment = 'William needs this access to do his job.', 
                        client_metadata = {applicationName=My application}, 
                        approval_info = [
                            sailpoint.beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner(
                                approval_comment = 'This access looks good.  Approved.', 
                                approval_decision = APPROVED, 
                                approver_name = 'Stephen.Austin', 
                                approver = sailpoint.beta.models.access_request_post_approval_requested_items_status_inner_approval_info_inner_approver.AccessRequestPostApproval_requestedItemsStatus_inner_approvalInfo_inner_approver(
                                    type = IDENTITY, ), )
                            ], )
                    ],
                source = sailpoint.beta.models.account_uncorrelated_source.AccountUncorrelated_source(
                    type = 'SOURCE', 
                    id = '2c6180835d191a86015d28455b4b231b', 
                    name = 'Corporate Directory', ),
                status = Success,
                started = '2020-06-29T22:01:50.474Z',
                completed = '2020-06-29T22:02:04.090Z',
                errors = [
                    'Connector AD Failed'
                    ],
                warnings = [
                    'Notification Skipped due to invalid email'
                    ],
                stats = sailpoint.beta.models.accounts_collected_for_aggregation_stats.AccountsCollectedForAggregation_stats(
                    scanned = 200, 
                    unchanged = 190, 
                    changed = 6, 
                    added = 4, 
                    removed = 3, ),
                identity = sailpoint.beta.models.identity_deleted_identity.IdentityDeleted_identity(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                account = sailpoint.beta.models.account_uncorrelated_account.AccountUncorrelated_account(
                    type = ACCOUNT, 
                    id = '4dd497e3723e439991cb6d0e478375dd', 
                    name = 'Sadie Jensen', 
                    native_identity = 'cn=john.doe,ou=users,dc=acme,dc=com', 
                    uuid = '1cb1f07d-3e5a-4431-becd-234fa4306108', ),
                changes = [
                    sailpoint.beta.models.identity_attributes_changed_changes_inner.IdentityAttributesChanged_changes_inner(
                        attribute = 'department', 
                        old_value = sales, 
                        new_value = marketing, )
                    ],
                attributes = {firstname=John, lastname=Doe, email=john.doe@gmail.com, department=Sales, displayName=John Doe, created=2020-04-27T16:48:33.597Z, employeeNumber=E009, uid=E009, inactive=true, phone=null, identificationNumber=E009},
                campaign = sailpoint.beta.models.campaign_generated_campaign.CampaignGenerated_campaign(
                    id = '2c91808576f886190176f88cac5a0010', 
                    name = 'Manager Access Campaign', 
                    description = 'Audit access for all employees.', 
                    created = '2021-02-16T03:04:45.815Z', 
                    modified = '2021-02-17T03:04:45.815Z', 
                    deadline = '2021-02-18T03:04:45.815Z', 
                    type = MANAGER, 
                    campaign_owner = sailpoint.beta.models.campaign_generated_campaign_campaign_owner.CampaignGenerated_campaign_campaignOwner(
                        id = '37f080867702c1910177031320c40n27', 
                        display_name = 'John Snow', 
                        email = 'john.snow@example.com', ), 
                    status = STAGED, ),
                certification = sailpoint.beta.models.certification_signed_off_certification.CertificationSignedOff_certification(
                    id = '2c91808576f886190176f88caf0d0067', 
                    name = 'Manager Access Review for Alice Baker', 
                    created = '2020-02-16T03:04:45.815Z', 
                    modified = '2020-02-16T03:06:45.815Z', ),
                tracking_number = '4b4d982dddff4267ab12f0f1e72b5a6d',
                sources = 'Corp AD, Corp LDAP, Corp Salesforce',
                recipient = sailpoint.beta.models.provisioning_completed_recipient.ProvisioningCompleted_recipient(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20642', 
                    name = 'Michael Michaels', ),
                account_requests = [
                    sailpoint.beta.models.provisioning_completed_account_requests_inner.ProvisioningCompleted_accountRequests_inner(
                        source = sailpoint.beta.models.provisioning_completed_account_requests_inner_source.ProvisioningCompleted_accountRequests_inner_source(
                            id = '4e4d982dddff4267ab12f0f1e72b5a6d', 
                            type = 'SOURCE', 
                            name = 'Corporate Active Directory', ), 
                        account_id = 'CN=Chewy.Bacca,ou=hardcorefigter,ou=wookies,dc=starwars,dc=com', 
                        account_operation = 'Modify', 
                        provisioning_result = SUCCESS, 
                        provisioning_target = 'Corp AD', 
                        ticket_id = '72619262', 
                        attribute_requests = [
                            sailpoint.beta.models.provisioning_completed_account_requests_inner_attribute_requests_inner.ProvisioningCompleted_accountRequests_inner_attributeRequests_inner(
                                attribute_name = 'memberOf', 
                                attribute_value = 'CN=jedi,DC=starwars,DC=com', 
                                operation = Add, )
                            ], )
                    ],
                file_name = 'Modified.zip',
                owner_email = 'test@sailpoint.com',
                owner_name = 'Cloud Support',
                query = 'modified:[now-7y/d TO now]',
                search_name = 'Modified Activity',
                search_results = sailpoint.beta.models.saved_search_complete_search_results.SavedSearchComplete_searchResults(
                    account = sailpoint.beta.models.saved_search_complete_search_results_account.SavedSearchComplete_searchResults_Account(
                        count = '3', 
                        noun = 'accounts', 
                        preview = [
                            []
                            ], ), 
                    entitlement = sailpoint.beta.models.saved_search_complete_search_results_entitlement.SavedSearchComplete_searchResults_Entitlement(
                        count = '2', 
                        noun = 'entitlements', 
                        preview = [
                            []
                            ], ), 
                    identity = sailpoint.beta.models.saved_search_complete_search_results_identity.SavedSearchComplete_searchResults_Identity(
                        count = '2', 
                        noun = 'identities', 
                        preview = [
                            []
                            ], ), ),
                signed_s3_url = 'https://sptcbu-org-data-useast1.s3.amazonaws.com/arsenal-john/reports/Events%20Export.2020-05-06%2018%2759%20GMT.3e580592-86e4-4953-8aea-49e6ef20a086.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200506T185919Z&X-Amz-SignedHeaders=host&X-Amz-Expires=899&X-Amz-Credential=AKIAV5E54XOGTS4Q4L7A%2F20200506%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2e732bb97a12a1fd8a215613e3c31fcdae8ba1fb6a25916843ab5b51d2ddefbc',
                id = '2c9180866166b5b0016167c32ef31a66',
                native_identifier = 'E009',
                source_id = '2c918082814e693601816e09471b29b6',
                source_name = 'Active Directory',
                identity_id = 'ee769173319b41d19ccec6c235423237b',
                identity_name = 'john.doe',
                name = 'Corporate Active Directory',
                type = 'DIRECT_CONNECT',
                created = '2020-06-29T22:01:50.474Z',
                connector = 'active-directory',
                actor = sailpoint.beta.models.source_updated_actor.SourceUpdated_actor(
                    type = 'IDENTITY', 
                    id = '2c7180a46faadee4016fb4e018c20648', 
                    name = 'William Wilson', ),
                deleted = '2021-03-29T22:01:50.474Z',
                modified = '2021-03-29T22:01:50.474Z',
                application = sailpoint.beta.models.va_cluster_status_change_event_application.VAClusterStatusChangeEvent_application(
                    id = '2c9180866166b5b0016167c32ef31a66', 
                    name = 'Production VA Cluster', 
                    attributes = { }, ),
                health_check_result = sailpoint.beta.models.va_cluster_status_change_event_health_check_result.VAClusterStatusChangeEvent_healthCheckResult(
                    message = 'Test Connection failed with exception. Error message - java.lang Exception', 
                    result_type = 'SOURCE_STATE_ERROR_CLUSTER', 
                    status = Succeeded, ),
                previous_health_check_result = sailpoint.beta.models.va_cluster_status_change_event_previous_health_check_result.VAClusterStatusChangeEvent_previousHealthCheckResult(
                    message = 'Test Connection failed with exception. Error message - java.lang Exception', 
                    result_type = 'SOURCE_STATE_ERROR_CLUSTER', 
                    status = Failed, ),
        )
        """

    def testTriggerExampleInput(self):
        """Test TriggerExampleInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
