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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist


class AccessProfileBulkDeleteRequest(BaseModel):
    """
    AccessProfileBulkDeleteRequest
    """
    access_profile_ids: Optional[conlist(StrictStr)] = Field(
        None,
        alias="accessProfileIds",
        description="List of IDs of Access Profiles to be deleted.")
    best_effort_only: Optional[StrictBool] = Field(
        None,
        alias="bestEffortOnly",
        description=
        "If **true**, silently skip over any of the specified Access Profiles if they cannot be deleted because they are in use. If **false**, no deletions will be attempted if any of the Access Profiles are in use."
    )
    __properties = ["accessProfileIds", "bestEffortOnly"]

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
    def from_json(cls, json_str: str) -> AccessProfileBulkDeleteRequest:
        """Create an instance of AccessProfileBulkDeleteRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessProfileBulkDeleteRequest:
        """Create an instance of AccessProfileBulkDeleteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessProfileBulkDeleteRequest.parse_obj(obj)

        _obj = AccessProfileBulkDeleteRequest.parse_obj({
            "access_profile_ids":
            obj.get("accessProfileIds"),
            "best_effort_only":
            obj.get("bestEffortOnly")
        })
        return _obj
