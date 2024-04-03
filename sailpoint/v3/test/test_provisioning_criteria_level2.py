# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.v3.models.provisioning_criteria_level2 import ProvisioningCriteriaLevel2

class TestProvisioningCriteriaLevel2(unittest.TestCase):
    """ProvisioningCriteriaLevel2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProvisioningCriteriaLevel2:
        """Test ProvisioningCriteriaLevel2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProvisioningCriteriaLevel2`
        """
        model = ProvisioningCriteriaLevel2()
        if include_optional:
            return ProvisioningCriteriaLevel2(
                operation = 'EQUALS',
                attribute = 'email',
                value = 'carlee.cert1c9f9b6fd@mailinator.com',
                children = [
                    sailpoint.v3.models.provisioning_criteria_level3.ProvisioningCriteriaLevel3(
                        operation = 'EQUALS', 
                        attribute = 'email', 
                        value = 'carlee.cert1c9f9b6fd@mailinator.com', )
                    ]
            )
        else:
            return ProvisioningCriteriaLevel2(
        )
        """

    def testProvisioningCriteriaLevel2(self):
        """Test ProvisioningCriteriaLevel2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
