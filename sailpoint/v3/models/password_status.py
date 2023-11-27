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

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator


class PasswordStatus(BaseModel):
    """
    PasswordStatus
    """
    request_id: Optional[StrictStr] = Field(
        None, alias="requestId", description="The password change request ID")
    state: Optional[StrictStr] = Field(None,
                                       description="Password change state")
    errors: Optional[conlist(StrictStr)] = Field(
        None, description="The errors during the password change request")
    source_ids: Optional[conlist(StrictStr)] = Field(
        None,
        alias="sourceIds",
        description="List of source IDs in the password change request")
    __properties = ["requestId", "state", "errors", "sourceIds"]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('IN_PROGRESS', 'FINISHED', 'FAILED'):
            raise ValueError(
                "must be one of enum values ('IN_PROGRESS', 'FINISHED', 'FAILED')"
            )
        return value

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
    def from_json(cls, json_str: str) -> PasswordStatus:
        """Create an instance of PasswordStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if request_id (nullable) is None
        # and __fields_set__ contains the field
        if self.request_id is None and "request_id" in self.__fields_set__:
            _dict['requestId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PasswordStatus:
        """Create an instance of PasswordStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PasswordStatus.parse_obj(obj)

        _obj = PasswordStatus.parse_obj({
            "request_id": obj.get("requestId"),
            "state": obj.get("state"),
            "errors": obj.get("errors"),
            "source_ids": obj.get("sourceIds")
        })
        return _obj
