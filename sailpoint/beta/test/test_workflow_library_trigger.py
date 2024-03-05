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

from sailpoint.beta.models.workflow_library_trigger import WorkflowLibraryTrigger

class TestWorkflowLibraryTrigger(unittest.TestCase):
    """WorkflowLibraryTrigger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkflowLibraryTrigger:
        """Test WorkflowLibraryTrigger
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkflowLibraryTrigger`
        """
        model = WorkflowLibraryTrigger()
        if include_optional:
            return WorkflowLibraryTrigger(
                id = 'idn:identity-attributes-changed',
                type = EVENT,
                name = 'Identity Attributes Changed',
                description = 'One or more identity attributes changed.',
                is_dynamic_schema = False,
                input_example = {changes=[{attribute=department, newValue=marketing, oldValue=sales}, {attribute=manager, newValue={id=ee769173319b41d19ccec6c235423236c, name=mean.guy, type=IDENTITY}, oldValue={id=ee769173319b41d19ccec6c235423237b, name=nice.guy, type=IDENTITY}}, {attribute=email, newValue=john.doe@gmail.com, oldValue=john.doe@hotmail.com}], identity={id=ee769173319b41d19ccec6cea52f237b, name=john.doe, type=IDENTITY}},
                form_fields = []
            )
        else:
            return WorkflowLibraryTrigger(
        )
        """

    def testWorkflowLibraryTrigger(self):
        """Test WorkflowLibraryTrigger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
