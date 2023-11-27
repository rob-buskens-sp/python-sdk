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

from sailpoint.beta.models.evaluate_response import EvaluateResponse  # noqa: E501


class TestEvaluateResponse(unittest.TestCase):
    """EvaluateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EvaluateResponse:
        """Test EvaluateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EvaluateResponse`
        """
        model = EvaluateResponse()  # noqa: E501
        if include_optional:
            return EvaluateResponse(
                reassign_to_id = '869320b6b6f34a169b6178b1a865e66f',
                lookup_trail = [
                    sailpoint.beta.models.lookup_step.LookupStep(
                        reassigned_to_id = '869320b6b6f34a169b6178b1a865e66f', 
                        reassigned_from_id = '51948a8f306a4e7a9a6f8f5d032fa59e', 
                        reassignment_type = 'AUTOMATIC_REASSIGNMENT', )
                    ]
            )
        else:
            return EvaluateResponse(
        )
        """

    def testEvaluateResponse(self):
        """Test EvaluateResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
