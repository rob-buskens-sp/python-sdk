# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.client_log_configuration import ClientLogConfiguration
from sailpoint.beta.models.managed_client_type import ManagedClientType
from sailpoint.beta.models.managed_cluster_attributes import ManagedClusterAttributes
from sailpoint.beta.models.managed_cluster_key_pair import ManagedClusterKeyPair
from sailpoint.beta.models.managed_cluster_redis import ManagedClusterRedis
from sailpoint.beta.models.managed_cluster_types import ManagedClusterTypes
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ManagedCluster(BaseModel):
    """
    Managed Cluster
    """

  # noqa: E501
    id: StrictStr = Field(description="ManagedCluster ID")
    name: Optional[StrictStr] = Field(default=None,
                                      description="ManagedCluster name")
    pod: Optional[StrictStr] = Field(default=None,
                                     description="ManagedCluster pod")
    org: Optional[StrictStr] = Field(default=None,
                                     description="ManagedCluster org")
    type: Optional[ManagedClusterTypes] = None
    configuration: Optional[Dict[str, StrictStr]] = Field(
        default=None, description="ManagedProcess configuration map")
    key_pair: Optional[ManagedClusterKeyPair] = Field(default=None,
                                                      alias="keyPair")
    attributes: Optional[ManagedClusterAttributes] = None
    description: Optional[StrictStr] = Field(
        default=None, description="ManagedCluster description")
    redis: Optional[ManagedClusterRedis] = None
    client_type: Optional[ManagedClientType] = Field(alias="clientType")
    ccg_version: StrictStr = Field(
        description="CCG version used by the ManagedCluster",
        alias="ccgVersion")
    pinned_config: Optional[StrictBool] = Field(
        default=False,
        description=
        "boolean flag indiacting whether or not the cluster configuration is pinned",
        alias="pinnedConfig")
    log_configuration: Optional[ClientLogConfiguration] = Field(
        default=None, alias="logConfiguration")
    operational: Optional[StrictBool] = Field(
        default=False,
        description="Whether or not the cluster is operational or not")
    status: Optional[StrictStr] = Field(default=None,
                                        description="Cluster status")
    public_key_certificate: Optional[StrictStr] = Field(
        default=None,
        description="Public key certificate",
        alias="publicKeyCertificate")
    public_key_thumbprint: Optional[StrictStr] = Field(
        default=None,
        description="Public key thumbprint",
        alias="publicKeyThumbprint")
    public_key: Optional[StrictStr] = Field(default=None,
                                            description="Public key",
                                            alias="publicKey")
    alert_key: Optional[StrictStr] = Field(
        default=None,
        description="Key describing any immediate cluster alerts",
        alias="alertKey")
    client_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="List of clients in a cluster",
        alias="clientIds")
    service_count: Optional[StrictInt] = Field(
        default=0,
        description="Number of services bound to a cluster",
        alias="serviceCount")
    cc_id: Optional[StrictStr] = Field(
        default='0',
        description=
        "CC ID only used in calling CC, will be removed without notice when Migration to CEGS is finished",
        alias="ccId")
    __properties: ClassVar[List[str]] = [
        "id", "name", "pod", "org", "type", "configuration", "keyPair",
        "attributes", "description", "redis", "clientType", "ccgVersion",
        "pinnedConfig", "logConfiguration", "operational", "status",
        "publicKeyCertificate", "publicKeyThumbprint", "publicKey", "alertKey",
        "clientIds", "serviceCount", "ccId"
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManagedCluster from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of key_pair
        if self.key_pair:
            _dict['keyPair'] = self.key_pair.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of redis
        if self.redis:
            _dict['redis'] = self.redis.to_dict()
        # override the default output from pydantic by calling `to_dict()` of log_configuration
        if self.log_configuration:
            _dict['logConfiguration'] = self.log_configuration.to_dict()
        # set to None if client_type (nullable) is None
        # and model_fields_set contains the field
        if self.client_type is None and "client_type" in self.model_fields_set:
            _dict['clientType'] = None

        # set to None if log_configuration (nullable) is None
        # and model_fields_set contains the field
        if self.log_configuration is None and "log_configuration" in self.model_fields_set:
            _dict['logConfiguration'] = None

        # set to None if public_key_certificate (nullable) is None
        # and model_fields_set contains the field
        if self.public_key_certificate is None and "public_key_certificate" in self.model_fields_set:
            _dict['publicKeyCertificate'] = None

        # set to None if public_key_thumbprint (nullable) is None
        # and model_fields_set contains the field
        if self.public_key_thumbprint is None and "public_key_thumbprint" in self.model_fields_set:
            _dict['publicKeyThumbprint'] = None

        # set to None if public_key (nullable) is None
        # and model_fields_set contains the field
        if self.public_key is None and "public_key" in self.model_fields_set:
            _dict['publicKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ManagedCluster from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "pod":
            obj.get("pod"),
            "org":
            obj.get("org"),
            "type":
            obj.get("type"),
            "configuration":
            obj.get("configuration"),
            "keyPair":
            ManagedClusterKeyPair.from_dict(obj.get("keyPair"))
            if obj.get("keyPair") is not None else None,
            "attributes":
            ManagedClusterAttributes.from_dict(obj.get("attributes"))
            if obj.get("attributes") is not None else None,
            "description":
            obj.get("description"),
            "redis":
            ManagedClusterRedis.from_dict(obj.get("redis"))
            if obj.get("redis") is not None else None,
            "clientType":
            obj.get("clientType"),
            "ccgVersion":
            obj.get("ccgVersion"),
            "pinnedConfig":
            obj.get("pinnedConfig")
            if obj.get("pinnedConfig") is not None else False,
            "logConfiguration":
            ClientLogConfiguration.from_dict(obj.get("logConfiguration"))
            if obj.get("logConfiguration") is not None else None,
            "operational":
            obj.get("operational")
            if obj.get("operational") is not None else False,
            "status":
            obj.get("status"),
            "publicKeyCertificate":
            obj.get("publicKeyCertificate"),
            "publicKeyThumbprint":
            obj.get("publicKeyThumbprint"),
            "publicKey":
            obj.get("publicKey"),
            "alertKey":
            obj.get("alertKey"),
            "clientIds":
            obj.get("clientIds"),
            "serviceCount":
            obj.get("serviceCount")
            if obj.get("serviceCount") is not None else 0,
            "ccId":
            obj.get("ccId") if obj.get("ccId") is not None else '0'
        })
        return _obj
