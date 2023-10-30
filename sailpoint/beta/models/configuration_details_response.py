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
from typing import Optional
from pydantic import BaseModel, Field
from beta.models.audit_details import AuditDetails
from beta.models.config_type_enum import ConfigTypeEnum
from beta.models.identity1 import Identity1

class ConfigurationDetailsResponse(BaseModel):
    """
    The request body of Reassignment Configuration Details for a specific identity and config type  # noqa: E501
    """
    config_type: Optional[ConfigTypeEnum] = Field(None, alias="configType")
    target_identity: Optional[Identity1] = Field(None, alias="targetIdentity")
    start_date: Optional[datetime] = Field(None, alias="startDate", description="The date from which to start reassigning work items")
    end_date: Optional[datetime] = Field(None, alias="endDate", description="The date from which to stop reassigning work items.  If this is an empty string it indicates a permanent reassignment.")
    audit_details: Optional[AuditDetails] = Field(None, alias="auditDetails")
    __properties = ["configType", "targetIdentity", "startDate", "endDate", "auditDetails"]

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
    def from_json(cls, json_str: str) -> ConfigurationDetailsResponse:
        """Create an instance of ConfigurationDetailsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of target_identity
        if self.target_identity:
            _dict['targetIdentity'] = self.target_identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audit_details
        if self.audit_details:
            _dict['auditDetails'] = self.audit_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationDetailsResponse:
        """Create an instance of ConfigurationDetailsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationDetailsResponse.parse_obj(obj)

        _obj = ConfigurationDetailsResponse.parse_obj({
            "config_type": obj.get("configType"),
            "target_identity": Identity1.from_dict(obj.get("targetIdentity")) if obj.get("targetIdentity") is not None else None,
            "start_date": obj.get("startDate"),
            "end_date": obj.get("endDate"),
            "audit_details": AuditDetails.from_dict(obj.get("auditDetails")) if obj.get("auditDetails") is not None else None
        })
        return _obj


