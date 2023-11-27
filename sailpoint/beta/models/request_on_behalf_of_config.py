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

from typing import Optional
from pydantic import BaseModel, Field, StrictBool


class RequestOnBehalfOfConfig(BaseModel):
    """
    RequestOnBehalfOfConfig
    """
    allow_request_on_behalf_of_anyone_by_anyone: Optional[StrictBool] = Field(
        None,
        alias="allowRequestOnBehalfOfAnyoneByAnyone",
        description="If anyone can request access for anyone.")
    allow_request_on_behalf_of_employee_by_manager: Optional[
        StrictBool] = Field(
            None,
            alias="allowRequestOnBehalfOfEmployeeByManager",
            description=
            "If a manager can request access for his/her direct reports.")
    __properties = [
        "allowRequestOnBehalfOfAnyoneByAnyone",
        "allowRequestOnBehalfOfEmployeeByManager"
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
    def from_json(cls, json_str: str) -> RequestOnBehalfOfConfig:
        """Create an instance of RequestOnBehalfOfConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestOnBehalfOfConfig:
        """Create an instance of RequestOnBehalfOfConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestOnBehalfOfConfig.parse_obj(obj)

        _obj = RequestOnBehalfOfConfig.parse_obj({
            "allow_request_on_behalf_of_anyone_by_anyone":
            obj.get("allowRequestOnBehalfOfAnyoneByAnyone"),
            "allow_request_on_behalf_of_employee_by_manager":
            obj.get("allowRequestOnBehalfOfEmployeeByManager")
        })
        return _obj
