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

from sailpoint.v3.models.list_complete_workflow_library200_response_inner import ListCompleteWorkflowLibrary200ResponseInner

class TestListCompleteWorkflowLibrary200ResponseInner(unittest.TestCase):
    """ListCompleteWorkflowLibrary200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListCompleteWorkflowLibrary200ResponseInner:
        """Test ListCompleteWorkflowLibrary200ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListCompleteWorkflowLibrary200ResponseInner`
        """
        model = ListCompleteWorkflowLibrary200ResponseInner()
        if include_optional:
            return ListCompleteWorkflowLibrary200ResponseInner(
                id = 'sp:compare-boolean',
                name = 'Compare Boolean Values',
                type = 'OPERATOR',
                description = 'Compare two boolean values and decide what happens based on the result.',
                form_fields = [{description=Enter the JSONPath to a value from the input to compare to Variable B., helpText=, label=Variable A, name=variableA.$, required=true, type=text}, {helpText=Select an operation., label=Operation, name=operator, options=[{label=Equals, value=BooleanEquals}], required=true, type=select}, {description=Enter the JSONPath to a value from the input to compare to Variable A., helpText=, label=Variable B, name=variableB.$, required=false, type=text}, {description=Enter True or False., helpText=, label=Variable B, name=variableB, required=false, type=text}],
                is_dynamic_schema = False,
                output_schema = {definitions={}, properties={autoRevokeAllowed={$id=#sp:create-campaign/autoRevokeAllowed, default=true, examples=[false], title=autoRevokeAllowed, type=boolean}, deadline={$id=#sp:create-campaign/deadline, default=, examples=[2020-12-25T06:00:00.468Z], format=date-time, pattern=^.*$, title=deadline, type=string}, description={$id=#sp:create-campaign/description, default=, examples=[A review of everyone's access by their manager.], pattern=^.*$, title=description, type=string}, emailNotificationEnabled={$id=#sp:create-campaign/emailNotificationEnabled, default=true, examples=[false], title=emailNotificationEnabled, type=boolean}, filter={$id=#sp:create-campaign/filter, properties={id={$id=#sp:create-campaign/filter/id, default=, examples=[e0adaae69852e8fe8b8a3d48e5ce757c], pattern=^.*$, title=id, type=string}, type={$id=#sp:create-campaign/filter/type, default=, examples=[CAMPAIGN_FILTER], pattern=^.*$, title=type, type=string}}, title=filter, type=object}, id={$id=#sp:create-campaign/id, default=, examples=[2c918086719eec070171a7e3355a360a], pattern=^.*$, title=id, type=string}, name={$id=#sp:create-campaign/name, default=, examples=[Manager Review], pattern=^.*$, title=name, type=string}, recommendationsEnabled={$id=#sp:create-campaign/recommendationsEnabled, default=true, examples=[false], title=recommendationEnabled, type=boolean}, type={$id=#sp:create-campaign/type, default=, examples=[MANAGER], pattern=^.*$, title=type, type=string}}, title=sp:create-campaign, type=object},
                input_example = {changes=[{attribute=department, newValue=marketing, oldValue=sales}, {attribute=manager, newValue={id=ee769173319b41d19ccec6c235423236c, name=mean.guy, type=IDENTITY}, oldValue={id=ee769173319b41d19ccec6c235423237b, name=nice.guy, type=IDENTITY}}, {attribute=email, newValue=john.doe@gmail.com, oldValue=john.doe@hotmail.com}], identity={id=ee769173319b41d19ccec6cea52f237b, name=john.doe, type=IDENTITY}}
            )
        else:
            return ListCompleteWorkflowLibrary200ResponseInner(
        )
        """

    def testListCompleteWorkflowLibrary200ResponseInner(self):
        """Test ListCompleteWorkflowLibrary200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
