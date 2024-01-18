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

from sailpoint.beta.models.provisioning_criteria_level1 import ProvisioningCriteriaLevel1


class TestProvisioningCriteriaLevel1(unittest.TestCase):
    """ProvisioningCriteriaLevel1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProvisioningCriteriaLevel1:
        """Test ProvisioningCriteriaLevel1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProvisioningCriteriaLevel1`
        """
        model = ProvisioningCriteriaLevel1()
        if include_optional:
            return ProvisioningCriteriaLevel1(
                operation = 'EQUALS',
                attribute = 'email',
                value = 'carlee.cert1c9f9b6fd@mailinator.com',
                children = [
                    sailpoint.beta.models.provisioning_criteria_level2.ProvisioningCriteriaLevel2(
                        operation = 'EQUALS', 
                        attribute = 'email', 
                        value = 'carlee.cert1c9f9b6fd@mailinator.com', )
                    ]
            )
        else:
            return ProvisioningCriteriaLevel1(
        )
        """

    def testProvisioningCriteriaLevel1(self):
        """Test ProvisioningCriteriaLevel1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
