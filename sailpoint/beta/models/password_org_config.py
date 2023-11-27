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
from pydantic import BaseModel, Field, StrictBool, conint


class PasswordOrgConfig(BaseModel):
    """
    PasswordOrgConfig
    """
    custom_instructions_enabled: Optional[StrictBool] = Field(
        False,
        alias="customInstructionsEnabled",
        description=
        "Indicator whether custom password instructions feature is enabled. The default value is false."
    )
    digit_token_enabled: Optional[StrictBool] = Field(
        False,
        alias="digitTokenEnabled",
        description=
        "Indicator whether \"digit token\" feature is enabled. The default value is false."
    )
    digit_token_duration_minutes: Optional[conint(
        strict=True, le=60, ge=1
    )] = Field(
        5,
        alias="digitTokenDurationMinutes",
        description=
        "The duration of \"digit token\" in minutes. The default value is 5.")
    digit_token_length: Optional[conint(strict=True, le=18, ge=6)] = Field(
        6,
        alias="digitTokenLength",
        description="The length of \"digit token\". The default value is 6.")
    __properties = [
        "customInstructionsEnabled", "digitTokenEnabled",
        "digitTokenDurationMinutes", "digitTokenLength"
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
    def from_json(cls, json_str: str) -> PasswordOrgConfig:
        """Create an instance of PasswordOrgConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PasswordOrgConfig:
        """Create an instance of PasswordOrgConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PasswordOrgConfig.parse_obj(obj)

        _obj = PasswordOrgConfig.parse_obj({
            "custom_instructions_enabled":
            obj.get("customInstructionsEnabled")
            if obj.get("customInstructionsEnabled") is not None else False,
            "digit_token_enabled":
            obj.get("digitTokenEnabled")
            if obj.get("digitTokenEnabled") is not None else False,
            "digit_token_duration_minutes":
            obj.get("digitTokenDurationMinutes")
            if obj.get("digitTokenDurationMinutes") is not None else 5,
            "digit_token_length":
            obj.get("digitTokenLength")
            if obj.get("digitTokenLength") is not None else 6
        })
        return _obj
