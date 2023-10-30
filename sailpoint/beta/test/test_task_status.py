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

from beta.models.task_status import TaskStatus  # noqa: E501

class TestTaskStatus(unittest.TestCase):
    """TaskStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskStatus:
        """Test TaskStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskStatus`
        """
        model = TaskStatus()  # noqa: E501
        if include_optional:
            return TaskStatus(
                id = 'id12345',
                type = 'QUARTZ',
                unique_name = 'Big Task',
                description = 'A Really Big Task',
                parent_name = 'Parent Task',
                launcher = 'sweep',
                created = '2020-07-11T21:23:15Z',
                modified = '2020-07-11T21:23:15Z',
                launched = '2020-07-11T21:23:15Z',
                completed = '2020-07-11T21:23:15Z',
                completion_status = 'Success',
                messages = [
                    beta.models.task_status_message.TaskStatusMessage(
                        type = 'INFO', 
                        localized_text = beta.models.localized_message.LocalizedMessage(
                            locale = 'An error has occurred!', 
                            message = 'Error has occurred!', ), 
                        key = 'akey', 
                        parameters = [{name=value}], )
                    ],
                returns = [
                    beta.models.task_return_details.TaskReturnDetails(
                        name = 'label', 
                        attribute_name = 'identityCount', )
                    ],
                attributes = {identityCount=0},
                progress = 'Started',
                percent_complete = 100
            )
        else:
            return TaskStatus(
                id = 'id12345',
                type = 'QUARTZ',
                unique_name = 'Big Task',
                description = 'A Really Big Task',
                parent_name = 'Parent Task',
                launcher = 'sweep',
                created = '2020-07-11T21:23:15Z',
                modified = '2020-07-11T21:23:15Z',
                launched = '2020-07-11T21:23:15Z',
                completed = '2020-07-11T21:23:15Z',
                completion_status = 'Success',
                messages = [
                    beta.models.task_status_message.TaskStatusMessage(
                        type = 'INFO', 
                        localized_text = beta.models.localized_message.LocalizedMessage(
                            locale = 'An error has occurred!', 
                            message = 'Error has occurred!', ), 
                        key = 'akey', 
                        parameters = [{name=value}], )
                    ],
                returns = [
                    beta.models.task_return_details.TaskReturnDetails(
                        name = 'label', 
                        attribute_name = 'identityCount', )
                    ],
                attributes = {identityCount=0},
                progress = 'Started',
                percent_complete = 100,
        )
        """

    def testTaskStatus(self):
        """Test TaskStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
