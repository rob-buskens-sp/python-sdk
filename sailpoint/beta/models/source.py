# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.manager_correlation_mapping import ManagerCorrelationMapping
from sailpoint.beta.models.source_account_correlation_config import SourceAccountCorrelationConfig
from sailpoint.beta.models.source_account_correlation_rule import SourceAccountCorrelationRule
from sailpoint.beta.models.source_before_provisioning_rule import SourceBeforeProvisioningRule
from sailpoint.beta.models.source_cluster import SourceCluster
from sailpoint.beta.models.source_feature import SourceFeature
from sailpoint.beta.models.source_management_workgroup import SourceManagementWorkgroup
from sailpoint.beta.models.source_manager_correlation_rule import SourceManagerCorrelationRule
from sailpoint.beta.models.source_owner import SourceOwner
from sailpoint.beta.models.source_password_policies_inner import SourcePasswordPoliciesInner
from sailpoint.beta.models.source_schemas_inner import SourceSchemasInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Source(BaseModel):
    """
    Source
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="the id of the Source")
    name: StrictStr = Field(description="Human-readable name of the source")
    description: Optional[StrictStr] = Field(default=None, description="Human-readable description of the source")
    owner: SourceOwner
    cluster: Optional[SourceCluster] = None
    account_correlation_config: Optional[SourceAccountCorrelationConfig] = Field(default=None, alias="accountCorrelationConfig")
    account_correlation_rule: Optional[SourceAccountCorrelationRule] = Field(default=None, alias="accountCorrelationRule")
    manager_correlation_mapping: Optional[ManagerCorrelationMapping] = Field(default=None, alias="managerCorrelationMapping")
    manager_correlation_rule: Optional[SourceManagerCorrelationRule] = Field(default=None, alias="managerCorrelationRule")
    before_provisioning_rule: Optional[SourceBeforeProvisioningRule] = Field(default=None, alias="beforeProvisioningRule")
    schemas: Optional[List[SourceSchemasInner]] = Field(default=None, description="List of references to Schema objects")
    password_policies: Optional[List[SourcePasswordPoliciesInner]] = Field(default=None, description="List of references to the associated PasswordPolicy objects.", alias="passwordPolicies")
    features: Optional[List[SourceFeature]] = Field(default=None, description="Optional features that can be supported by a source.")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the type of system being managed e.g. Active Directory, Workday, etc.. If you are creating a Delimited File source, you must set the `provisionasCsv` query parameter to `true`. ")
    connector: StrictStr = Field(description="Connector script name.")
    connector_class: Optional[StrictStr] = Field(default=None, description="The fully qualified name of the Java class that implements the connector interface.", alias="connectorClass")
    connector_attributes: Optional[Dict[str, Any]] = Field(default=None, description="Connector specific configuration; will differ from type to type.", alias="connectorAttributes")
    delete_threshold: Optional[StrictInt] = Field(default=None, description="Number from 0 to 100 that specifies when to skip the delete phase.", alias="deleteThreshold")
    authoritative: Optional[StrictBool] = Field(default=False, description="When true indicates the source is referenced by an IdentityProfile.")
    management_workgroup: Optional[SourceManagementWorkgroup] = Field(default=None, alias="managementWorkgroup")
    healthy: Optional[StrictBool] = Field(default=False, description="When true indicates a healthy source")
    status: Optional[StrictStr] = Field(default=None, description="A status identifier, giving specific information on why a source is healthy or not")
    since: Optional[StrictStr] = Field(default=None, description="Timestamp showing when a source health check was last performed")
    connector_id: Optional[StrictStr] = Field(default=None, description="The id of connector", alias="connectorId")
    connector_name: Optional[StrictStr] = Field(default=None, description="The name of the connector that was chosen on source creation", alias="connectorName")
    connection_type: Optional[StrictStr] = Field(default=None, description="The type of connection (direct or file)", alias="connectionType")
    connector_implementation_id: Optional[StrictStr] = Field(default=None, description="The connector implementation id", alias="connectorImplementationId")
    created: Optional[datetime] = Field(default=None, description="The date-time when the source was created")
    modified: Optional[datetime] = Field(default=None, description="The date-time when the source was last modified")
    credential_provider_enabled: Optional[StrictBool] = Field(default=False, description="Enables credential provider for this source. If credentialProvider is turned on  then source can use credential provider(s) to fetch credentials.", alias="credentialProviderEnabled")
    category: Optional[StrictStr] = Field(default=None, description="The category of source (e.g. null, CredentialProvider)")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "owner", "cluster", "accountCorrelationConfig", "accountCorrelationRule", "managerCorrelationMapping", "managerCorrelationRule", "beforeProvisioningRule", "schemas", "passwordPolicies", "features", "type", "connector", "connectorClass", "connectorAttributes", "deleteThreshold", "authoritative", "managementWorkgroup", "healthy", "status", "since", "connectorId", "connectorName", "connectionType", "connectorImplementationId", "created", "modified", "credentialProviderEnabled", "category"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Source from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_correlation_config
        if self.account_correlation_config:
            _dict['accountCorrelationConfig'] = self.account_correlation_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_correlation_rule
        if self.account_correlation_rule:
            _dict['accountCorrelationRule'] = self.account_correlation_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manager_correlation_mapping
        if self.manager_correlation_mapping:
            _dict['managerCorrelationMapping'] = self.manager_correlation_mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of manager_correlation_rule
        if self.manager_correlation_rule:
            _dict['managerCorrelationRule'] = self.manager_correlation_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of before_provisioning_rule
        if self.before_provisioning_rule:
            _dict['beforeProvisioningRule'] = self.before_provisioning_rule.to_dict()
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
        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Source from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "owner": SourceOwner.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "cluster": SourceCluster.from_dict(obj.get("cluster")) if obj.get("cluster") is not None else None,
            "accountCorrelationConfig": SourceAccountCorrelationConfig.from_dict(obj.get("accountCorrelationConfig")) if obj.get("accountCorrelationConfig") is not None else None,
            "accountCorrelationRule": SourceAccountCorrelationRule.from_dict(obj.get("accountCorrelationRule")) if obj.get("accountCorrelationRule") is not None else None,
            "managerCorrelationMapping": ManagerCorrelationMapping.from_dict(obj.get("managerCorrelationMapping")) if obj.get("managerCorrelationMapping") is not None else None,
            "managerCorrelationRule": SourceManagerCorrelationRule.from_dict(obj.get("managerCorrelationRule")) if obj.get("managerCorrelationRule") is not None else None,
            "beforeProvisioningRule": SourceBeforeProvisioningRule.from_dict(obj.get("beforeProvisioningRule")) if obj.get("beforeProvisioningRule") is not None else None,
            "schemas": [SourceSchemasInner.from_dict(_item) for _item in obj.get("schemas")] if obj.get("schemas") is not None else None,
            "passwordPolicies": [SourcePasswordPoliciesInner.from_dict(_item) for _item in obj.get("passwordPolicies")] if obj.get("passwordPolicies") is not None else None,
            "features": obj.get("features"),
            "type": obj.get("type"),
            "connector": obj.get("connector"),
            "connectorClass": obj.get("connectorClass"),
            "connectorAttributes": obj.get("connectorAttributes"),
            "deleteThreshold": obj.get("deleteThreshold"),
            "authoritative": obj.get("authoritative") if obj.get("authoritative") is not None else False,
            "managementWorkgroup": SourceManagementWorkgroup.from_dict(obj.get("managementWorkgroup")) if obj.get("managementWorkgroup") is not None else None,
            "healthy": obj.get("healthy") if obj.get("healthy") is not None else False,
            "status": obj.get("status"),
            "since": obj.get("since"),
            "connectorId": obj.get("connectorId"),
            "connectorName": obj.get("connectorName"),
            "connectionType": obj.get("connectionType"),
            "connectorImplementationId": obj.get("connectorImplementationId"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "credentialProviderEnabled": obj.get("credentialProviderEnabled") if obj.get("credentialProviderEnabled") is not None else False,
            "category": obj.get("category")
        })
        return _obj


