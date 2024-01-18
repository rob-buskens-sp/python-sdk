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

from sailpoint.beta.models.managed_client_status_agg_response import ManagedClientStatusAggResponse


class TestManagedClientStatusAggResponse(unittest.TestCase):
    """ManagedClientStatusAggResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self,
                      include_optional) -> ManagedClientStatusAggResponse:
        """Test ManagedClientStatusAggResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedClientStatusAggResponse`
        """
        model = ManagedClientStatusAggResponse()
        if include_optional:
            return ManagedClientStatusAggResponse(
                body = {body={id=1528, clientId=1528, clusterId=1533, orgType=test, vaDownloadUrl=https://sptcbu-va-images.s3.amazonaws.com/va-latest.zip, clusterJobCount=1, configuration={clusterType=sqsCluster, clusterExternalId=2c91808876dd79120176f758af765c58, debug=false, failureThreshold=0, gmtOffset=-6, scheduleUpgrade=false, va_version=va-megapod-useast1-595-1627543540, jobType=VA_UPGRADE, cookbook=va-megapod-useast1-595-1627543540}, connectorServices=[{id=540696, name=EndToEnd-ADSource, connector_host=host.example.com, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540698, name=EndToEnd-AzureADSource, connector_host=null, connector_port=null, connector_(boolean)useSSL=null, connectorFileUploadHistory=null}, {id=540710, name=EndToEnd-OpenLDAP, connector_host=10.0.2.64, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540713, name=Dynamic-ADSource, connector_host=host.example.com, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540716, name=EndToEnd-JdbcADSource, connector_host=10.0.5.187, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540717, name=EndToEnd-JdbcSource, connector_host=null, connector_port=null, connector_(boolean)useSSL=null, connectorFileUploadHistory=[{serviceId=540717, date=2021-02-05T22:58:15Z, file=temp7081703651350031905mysql-connector-java-8.0.11.jar}]}], jobs=[{uuid=872b622f-5ab5-4836-9172-e3bb77f05b2c, cookbook=872b622f-5ab5-4836-9172-e3bb77f05b2c, state=FINISHED, type=VA_UPGRADE, targetId=1528, managedProcessConfiguration={charon={version=345, path=sailpoint/charon, description=null, dependencies=null}, ccg={version=415_583_79.0.0, path=sailpoint/ccg, description=null, dependencies=null}, toolbox={version=6, path=sailpoint/toolbox, description=null, dependencies=null}, fluent={version=50, path=fluent/va, description=null, dependencies=null}, va_agent={version=89, path=sailpoint/va_agent, description=null, dependencies=null}}}], queue={name=megapod-useast1-denali-lwt-cluster-1533, region=us-east-1}, maintenance={window=true, windowStartTime=2021-07-29T00:00:00Z, windowClusterTime=2021-07-29T01:35:24Z, windowFinishTime=2021-07-29T04:00:00Z}}},
                status = 'NORMAL',
                type = 'CCG',
                timestamp = '2020-01-01T00:00Z'
            )
        else:
            return ManagedClientStatusAggResponse(
                body = {body={id=1528, clientId=1528, clusterId=1533, orgType=test, vaDownloadUrl=https://sptcbu-va-images.s3.amazonaws.com/va-latest.zip, clusterJobCount=1, configuration={clusterType=sqsCluster, clusterExternalId=2c91808876dd79120176f758af765c58, debug=false, failureThreshold=0, gmtOffset=-6, scheduleUpgrade=false, va_version=va-megapod-useast1-595-1627543540, jobType=VA_UPGRADE, cookbook=va-megapod-useast1-595-1627543540}, connectorServices=[{id=540696, name=EndToEnd-ADSource, connector_host=host.example.com, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540698, name=EndToEnd-AzureADSource, connector_host=null, connector_port=null, connector_(boolean)useSSL=null, connectorFileUploadHistory=null}, {id=540710, name=EndToEnd-OpenLDAP, connector_host=10.0.2.64, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540713, name=Dynamic-ADSource, connector_host=host.example.com, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540716, name=EndToEnd-JdbcADSource, connector_host=10.0.5.187, connector_port=389, connector_(boolean)useSSL=false, connectorFileUploadHistory=null}, {id=540717, name=EndToEnd-JdbcSource, connector_host=null, connector_port=null, connector_(boolean)useSSL=null, connectorFileUploadHistory=[{serviceId=540717, date=2021-02-05T22:58:15Z, file=temp7081703651350031905mysql-connector-java-8.0.11.jar}]}], jobs=[{uuid=872b622f-5ab5-4836-9172-e3bb77f05b2c, cookbook=872b622f-5ab5-4836-9172-e3bb77f05b2c, state=FINISHED, type=VA_UPGRADE, targetId=1528, managedProcessConfiguration={charon={version=345, path=sailpoint/charon, description=null, dependencies=null}, ccg={version=415_583_79.0.0, path=sailpoint/ccg, description=null, dependencies=null}, toolbox={version=6, path=sailpoint/toolbox, description=null, dependencies=null}, fluent={version=50, path=fluent/va, description=null, dependencies=null}, va_agent={version=89, path=sailpoint/va_agent, description=null, dependencies=null}}}], queue={name=megapod-useast1-denali-lwt-cluster-1533, region=us-east-1}, maintenance={window=true, windowStartTime=2021-07-29T00:00:00Z, windowClusterTime=2021-07-29T01:35:24Z, windowFinishTime=2021-07-29T04:00:00Z}}},
                status = 'NORMAL',
                type = 'CCG',
                timestamp = '2020-01-01T00:00Z',
        )
        """

    def testManagedClientStatusAggResponse(self):
        """Test ManagedClientStatusAggResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
