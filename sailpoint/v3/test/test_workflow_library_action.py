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

from sailpoint.v3.models.workflow_library_action import WorkflowLibraryAction

class TestWorkflowLibraryAction(unittest.TestCase):
    """WorkflowLibraryAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowLibraryAction:
        """Test WorkflowLibraryAction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowLibraryAction`
        """
        model = WorkflowLibraryAction()
        if include_optional:
            return WorkflowLibraryAction(
                id = 'sp:create-campaign',
                name = 'Create Certification Campaign',
                type = 'ACTION',
                description = 'Generates a certification campaign.',
                form_fields = [
                    sailpoint.v3.models.workflow_library_form_fields.WorkflowLibraryFormFields(
                        help_text = 'The name to give to this certification campaign.', 
                        label = 'Campaign Name', 
                        name = 'name', 
                        required = False, 
                        type = text, )
                    ],
                is_dynamic_schema = False,
                output_schema = {definitions={}, properties={autoRevokeAllowed={$id=#sp:create-campaign/autoRevokeAllowed, default=true, examples=[false], title=autoRevokeAllowed, type=boolean}, deadline={$id=#sp:create-campaign/deadline, default=, examples=[2020-12-25T06:00:00.468Z], format=date-time, pattern=^.*$, title=deadline, type=string}, description={$id=#sp:create-campaign/description, default=, examples=[A review of everyone's access by their manager.], pattern=^.*$, title=description, type=string}, emailNotificationEnabled={$id=#sp:create-campaign/emailNotificationEnabled, default=true, examples=[false], title=emailNotificationEnabled, type=boolean}, filter={$id=#sp:create-campaign/filter, properties={id={$id=#sp:create-campaign/filter/id, default=, examples=[e0adaae69852e8fe8b8a3d48e5ce757c], pattern=^.*$, title=id, type=string}, type={$id=#sp:create-campaign/filter/type, default=, examples=[CAMPAIGN_FILTER], pattern=^.*$, title=type, type=string}}, title=filter, type=object}, id={$id=#sp:create-campaign/id, default=, examples=[2c918086719eec070171a7e3355a360a], pattern=^.*$, title=id, type=string}, name={$id=#sp:create-campaign/name, default=, examples=[Manager Review], pattern=^.*$, title=name, type=string}, recommendationsEnabled={$id=#sp:create-campaign/recommendationsEnabled, default=true, examples=[false], title=recommendationEnabled, type=boolean}, type={$id=#sp:create-campaign/type, default=, examples=[MANAGER], pattern=^.*$, title=type, type=string}}, title=sp:create-campaign, type=object}
            )
        else:
            return WorkflowLibraryAction(
        )
        """

    def testWorkflowLibraryAction(self):
        """Test WorkflowLibraryAction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
