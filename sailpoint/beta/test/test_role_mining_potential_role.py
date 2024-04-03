# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from sailpoint.beta.models.role_mining_potential_role import RoleMiningPotentialRole

class TestRoleMiningPotentialRole(unittest.TestCase):
    """RoleMiningPotentialRole unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoleMiningPotentialRole:
        """Test RoleMiningPotentialRole
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoleMiningPotentialRole`
        """
        model = RoleMiningPotentialRole()
        if include_optional:
            return RoleMiningPotentialRole(
                created_by = sailpoint.beta.models.entity_created_by_dto.EntityCreatedByDTO(
                    id = '2c918090761a5aac0176215c46a62d58', 
                    display_name = 'Ashley.Pierce', ),
                density = 75,
                description = 'Potential Role for Accounting dept',
                entitlement_count = 25,
                excluded_entitlements = [07a0b4e2, 13b4e2a0],
                freshness = 75,
                identity_count = 25,
                identity_distribution = [
                    sailpoint.beta.models.role_mining_identity_distribution.RoleMiningIdentityDistribution(
                        attribute_name = 'department', 
                        distribution = [{attributeValue=NM Tier 3, count=6}], )
                    ],
                identity_ids = [07a0b4e2, 13b4e2a0],
                name = 'Saved Potential Role - 07/10',
                provision_state = 'POTENTIAL',
                quality = 100,
                role_id = '07a0b4e2-7a76-44fa-bd0b-c64654b66519',
                saved = True,
                session = sailpoint.beta.models.role_mining_session_parameters_dto.RoleMiningSessionParametersDto(
                    id = '9f36f5e5-1e81-4eca-b087-548959d91c71', 
                    name = 'Saved RM Session - 07/10', 
                    min_num_identities_in_potential_role = 20, 
                    prune_threshold = 5, 
                    saved = True, 
                    scope = sailpoint.beta.models.role_mining_session_scope.RoleMiningSessionScope(
                        identity_ids = [2c918090761a5aac0176215c46a62d58, 2c918090761a5aac01722015c46a62d42], 
                        criteria = 'source.name:DataScienceDataset', 
                        attribute_filter_criteria = {displayName={untranslated=Location: Miami}, ariaLabel={untranslated=Location: Miami}, data={displayName={translateKey=IDN.IDENTITY_ATTRIBUTES.LOCATION}, name=location, operator=EQUALS, values=[Miami]}}, ), 
                    type = 'SPECIALIZED', 
                    state = 'CREATED', 
                    scoping_method = 'MANUAL', ),
                type = 'SPECIALIZED'
            )
        else:
            return RoleMiningPotentialRole(
        )
        """

    def testRoleMiningPotentialRole(self):
        """Test RoleMiningPotentialRole"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
