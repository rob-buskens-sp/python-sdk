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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from sailpoint.beta.models.provisioning_config import ProvisioningConfig


class ServiceDeskIntegrationTemplateDto(BaseModel):
    """
    ServiceDeskIntegrationTemplateDto
    """
    id: Optional[StrictStr] = Field(
        None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(..., description="Name of the Object")
    created: Optional[datetime] = Field(
        None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(
        None, description="Last modification date of the Object")
    type: StrictStr = Field(
        ...,
        description=
        "The 'type' property specifies the type of the Service Desk integration template."
    )
    attributes: Dict[str, Any] = Field(
        ...,
        description=
        "The 'attributes' property value is a map of attributes available for integrations using this Service Desk integration template."
    )
    provisioning_config: ProvisioningConfig = Field(...,
                                                    alias="provisioningConfig")
    __properties = [
        "id", "name", "created", "modified", "type", "attributes",
        "provisioningConfig"
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
    def from_json(cls, json_str: str) -> ServiceDeskIntegrationTemplateDto:
        """Create an instance of ServiceDeskIntegrationTemplateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "id",
                              "created",
                              "modified",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of provisioning_config
        if self.provisioning_config:
            _dict['provisioningConfig'] = self.provisioning_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceDeskIntegrationTemplateDto:
        """Create an instance of ServiceDeskIntegrationTemplateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceDeskIntegrationTemplateDto.parse_obj(obj)

        _obj = ServiceDeskIntegrationTemplateDto.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "type":
            obj.get("type")
            if obj.get("type") is not None else 'Web Service SDIM',
            "attributes":
            obj.get("attributes"),
            "provisioning_config":
            ProvisioningConfig.from_dict(obj.get("provisioningConfig"))
            if obj.get("provisioningConfig") is not None else None
        })
        return _obj
