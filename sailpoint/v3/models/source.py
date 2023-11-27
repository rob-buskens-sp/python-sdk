# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from sailpoint.v3.models.manager_correlation_mapping import ManagerCorrelationMapping
from sailpoint.v3.models.source_account_correlation_config import SourceAccountCorrelationConfig
from sailpoint.v3.models.source_account_correlation_rule import SourceAccountCorrelationRule
from sailpoint.v3.models.source_before_provisioning_rule import SourceBeforeProvisioningRule
from sailpoint.v3.models.source_cluster import SourceCluster
from sailpoint.v3.models.source_feature import SourceFeature
from sailpoint.v3.models.source_management_workgroup import SourceManagementWorkgroup
from sailpoint.v3.models.source_manager_correlation_rule import SourceManagerCorrelationRule
from sailpoint.v3.models.source_owner import SourceOwner
from sailpoint.v3.models.source_password_policies_inner import SourcePasswordPoliciesInner
from sailpoint.v3.models.source_schemas_inner import SourceSchemasInner


class Source(BaseModel):
    """
    Source
    """
    id: Optional[StrictStr] = Field(None, description="the id of the Source")
    name: StrictStr = Field(...,
                            description="Human-readable name of the source")
    description: Optional[StrictStr] = Field(
        None, description="Human-readable description of the source")
    owner: SourceOwner = Field(...)
    cluster: Optional[SourceCluster] = None
    account_correlation_config: Optional[
        SourceAccountCorrelationConfig] = Field(
            None, alias="accountCorrelationConfig")
    account_correlation_rule: Optional[SourceAccountCorrelationRule] = Field(
        None, alias="accountCorrelationRule")
    manager_correlation_mapping: Optional[ManagerCorrelationMapping] = Field(
        None, alias="managerCorrelationMapping")
    manager_correlation_rule: Optional[SourceManagerCorrelationRule] = Field(
        None, alias="managerCorrelationRule")
    before_provisioning_rule: Optional[SourceBeforeProvisioningRule] = Field(
        None, alias="beforeProvisioningRule")
    schemas: Optional[conlist(SourceSchemasInner)] = Field(
        None, description="List of references to Schema objects")
    password_policies: Optional[conlist(SourcePasswordPoliciesInner)] = Field(
        None,
        alias="passwordPolicies",
        description=
        "List of references to the associated PasswordPolicy objects.")
    features: Optional[conlist(SourceFeature)] = Field(
        None,
        description="Optional features that can be supported by a source.")
    type: Optional[StrictStr] = Field(
        None,
        description=
        "Specifies the type of system being managed e.g. Active Directory, Workday, etc.. If you are creating a Delimited File source, you must set the `provisionasCsv` query parameter to `true`. "
    )
    connector: StrictStr = Field(..., description="Connector script name.")
    connector_class: Optional[StrictStr] = Field(
        None,
        alias="connectorClass",
        description=
        "The fully qualified name of the Java class that implements the connector interface."
    )
    connector_attributes: Optional[Dict[str, Any]] = Field(
        None,
        alias="connectorAttributes",
        description=
        "Connector specific configuration; will differ from type to type.")
    delete_threshold: Optional[StrictInt] = Field(
        None,
        alias="deleteThreshold",
        description=
        "Number from 0 to 100 that specifies when to skip the delete phase.")
    authoritative: Optional[StrictBool] = Field(
        False,
        description=
        "When true indicates the source is referenced by an IdentityProfile.")
    management_workgroup: Optional[SourceManagementWorkgroup] = Field(
        None, alias="managementWorkgroup")
    healthy: Optional[StrictBool] = Field(
        False, description="When true indicates a healthy source")
    status: Optional[StrictStr] = Field(
        None,
        description=
        "A status identifier, giving specific information on why a source is healthy or not"
    )
    since: Optional[StrictStr] = Field(
        None,
        description=
        "Timestamp showing when a source health check was last performed")
    connector_id: Optional[StrictStr] = Field(
        None, alias="connectorId", description="The id of connector")
    connector_name: Optional[StrictStr] = Field(
        None,
        alias="connectorName",
        description=
        "The name of the connector that was chosen on source creation")
    connection_type: Optional[StrictStr] = Field(
        None,
        alias="connectionType",
        description="The type of connection (direct or file)")
    connector_implementation_id: Optional[StrictStr] = Field(
        None,
        alias="connectorImplementationId",
        description="The connector implementation id")
    __properties = [
        "id", "name", "description", "owner", "cluster",
        "accountCorrelationConfig", "accountCorrelationRule",
        "managerCorrelationMapping", "managerCorrelationRule",
        "beforeProvisioningRule", "schemas", "passwordPolicies", "features",
        "type", "connector", "connectorClass", "connectorAttributes",
        "deleteThreshold", "authoritative", "managementWorkgroup", "healthy",
        "status", "since", "connectorId", "connectorName", "connectionType",
        "connectorImplementationId"
    ]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Source:
        """Create an instance of Source from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={
            "id",
        }, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_correlation_config
        if self.account_correlation_config:
            _dict[
                'accountCorrelationConfig'] = self.account_correlation_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of account_correlation_rule
        if self.account_correlation_rule:
            _dict[
                'accountCorrelationRule'] = self.account_correlation_rule.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of manager_correlation_mapping
        if self.manager_correlation_mapping:
            _dict[
                'managerCorrelationMapping'] = self.manager_correlation_mapping.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of manager_correlation_rule
        if self.manager_correlation_rule:
            _dict[
                'managerCorrelationRule'] = self.manager_correlation_rule.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of before_provisioning_rule
        if self.before_provisioning_rule:
            _dict[
                'beforeProvisioningRule'] = self.before_provisioning_rule.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in schemas (list)
        _items = []
        if self.schemas:
            for _item in self.schemas:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schemas'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in password_policies (list)
        _items = []
        if self.password_policies:
            for _item in self.password_policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['passwordPolicies'] = _items
        # override the default output from pydantic by calling `to_dict()` of management_workgroup
        if self.management_workgroup:
            _dict['managementWorkgroup'] = self.management_workgroup.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Source:
        """Create an instance of Source from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Source.parse_obj(obj)

        _obj = Source.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "owner":
            SourceOwner.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "cluster":
            SourceCluster.from_dict(obj.get("cluster"))
            if obj.get("cluster") is not None else None,
            "account_correlation_config":
            SourceAccountCorrelationConfig.from_dict(
                obj.get("accountCorrelationConfig"))
            if obj.get("accountCorrelationConfig") is not None else None,
            "account_correlation_rule":
            SourceAccountCorrelationRule.from_dict(
                obj.get("accountCorrelationRule"))
            if obj.get("accountCorrelationRule") is not None else None,
            "manager_correlation_mapping":
            ManagerCorrelationMapping.from_dict(
                obj.get("managerCorrelationMapping"))
            if obj.get("managerCorrelationMapping") is not None else None,
            "manager_correlation_rule":
            SourceManagerCorrelationRule.from_dict(
                obj.get("managerCorrelationRule"))
            if obj.get("managerCorrelationRule") is not None else None,
            "before_provisioning_rule":
            SourceBeforeProvisioningRule.from_dict(
                obj.get("beforeProvisioningRule"))
            if obj.get("beforeProvisioningRule") is not None else None,
            "schemas": [
                SourceSchemasInner.from_dict(_item)
                for _item in obj.get("schemas")
            ] if obj.get("schemas") is not None else None,
            "password_policies": [
                SourcePasswordPoliciesInner.from_dict(_item)
                for _item in obj.get("passwordPolicies")
            ] if obj.get("passwordPolicies") is not None else None,
            "features":
            obj.get("features"),
            "type":
            obj.get("type"),
            "connector":
            obj.get("connector"),
            "connector_class":
            obj.get("connectorClass"),
            "connector_attributes":
            obj.get("connectorAttributes"),
            "delete_threshold":
            obj.get("deleteThreshold"),
            "authoritative":
            obj.get("authoritative")
            if obj.get("authoritative") is not None else False,
            "management_workgroup":
            SourceManagementWorkgroup.from_dict(obj.get("managementWorkgroup"))
            if obj.get("managementWorkgroup") is not None else None,
            "healthy":
            obj.get("healthy") if obj.get("healthy") is not None else False,
            "status":
            obj.get("status"),
            "since":
            obj.get("since"),
            "connector_id":
            obj.get("connectorId"),
            "connector_name":
            obj.get("connectorName"),
            "connection_type":
            obj.get("connectionType"),
            "connector_implementation_id":
            obj.get("connectorImplementationId")
        })
        return _obj
