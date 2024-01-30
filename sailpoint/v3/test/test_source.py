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

from sailpoint.v3.models.source import Source


class TestSource(unittest.TestCase):
    """Source unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Source:
        """Test Source
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Source`
        """
        model = Source()
        if include_optional:
            return Source(
                id = '2c91808568c529c60168cca6f90c1324',
                name = 'My Source',
                description = 'This is the corporate directory.',
                owner = sailpoint.v3.models.source_owner.Source_owner(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'MyName', ),
                cluster = sailpoint.v3.models.source_cluster.Source_cluster(
                    type = 'CLUSTER', 
                    id = '2c9180866166b5b0016167c32ef31a66', 
                    name = 'Corporate Cluster', ),
                account_correlation_config = sailpoint.v3.models.source_account_correlation_config.Source_accountCorrelationConfig(
                    type = 'ACCOUNT_CORRELATION_CONFIG', 
                    id = '2c9180855d191c59015d28583727245a', 
                    name = 'Directory [source-62867] Account Correlation', ),
                account_correlation_rule = sailpoint.v3.models.source_account_correlation_rule.Source_accountCorrelationRule(
                    type = 'RULE', 
                    id = '2c918085708c274401708c2a8a760001', 
                    name = 'Example Rule', ),
                manager_correlation_mapping = sailpoint.v3.models.manager_correlation_mapping.ManagerCorrelationMapping(
                    account_attribute = 'manager', 
                    identity_attribute = 'manager', ),
                manager_correlation_rule = sailpoint.v3.models.source_manager_correlation_rule.Source_managerCorrelationRule(
                    type = 'RULE', 
                    id = '2c918085708c274401708c2a8a760001', 
                    name = 'Example Rule', ),
                before_provisioning_rule = sailpoint.v3.models.source_before_provisioning_rule.Source_beforeProvisioningRule(
                    type = 'RULE', 
                    id = '2c918085708c274401708c2a8a760001', 
                    name = 'Example Rule', ),
                schemas = [{type=CONNECTOR_SCHEMA, id=2c9180835d191a86015d28455b4b232a, name=account}, {type=CONNECTOR_SCHEMA, id=2c9180835d191a86015d28455b4b232b, name=group}],
                password_policies = [{type=PASSWORD_POLICY, id=2c9180855d191c59015d291ceb053980, name=Corporate Password Policy}, {type=PASSWORD_POLICY, id=2c9180855d191c59015d291ceb057777, name=Vendor Password Policy}],
                features = [SYNC_PROVISIONING, MANAGER_LOOKUP, SEARCH, PROVISIONING, AUTHENTICATE, GROUP_PROVISIONING, PASSWORD],
                type = 'OpenLDAP - Direct',
                connector = 'active-directory',
                connector_class = 'sailpoint.connector.LDAPConnector',
                connector_attributes = {healthCheckTimeout=30, authSearchAttributes=[cn, uid, mail]},
                delete_threshold = 10,
                authoritative = False,
                management_workgroup = sailpoint.v3.models.source_management_workgroup.Source_managementWorkgroup(
                    type = 'GOVERNANCE_GROUP', 
                    id = '2c91808568c529c60168cca6f90c2222', 
                    name = 'My Management Workgroup', ),
                healthy = True,
                status = 'SOURCE_STATE_HEALTHY',
                since = '2021-09-28T15:48:29.3801666300Z',
                connector_id = 'active-directory',
                connector_name = 'Active Directory',
                connection_type = 'file',
                connector_implementation_id = 'delimited-file',
                created = '2022-02-08T14:50:03.827Z',
                modified = '2024-01-23T18:08:50.897Z'
            )
        else:
            return Source(
                name = 'My Source',
                owner = sailpoint.v3.models.source_owner.Source_owner(
                    type = 'IDENTITY', 
                    id = '2c91808568c529c60168cca6f90c1313', 
                    name = 'MyName', ),
                connector = 'active-directory',
        )
        """

    def testSource(self):
        """Test Source"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
