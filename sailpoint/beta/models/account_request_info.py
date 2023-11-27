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
from pydantic import BaseModel, Field, StrictStr
from sailpoint.beta.models.requestable_object_type import RequestableObjectType


class AccountRequestInfo(BaseModel):
    """
    If an account activity item is associated with an access request, captures details of that request.  # noqa: E501
    """
    requested_object_id: Optional[StrictStr] = Field(
        None, alias="requestedObjectId", description="Id of requested object")
    requested_object_name: Optional[StrictStr] = Field(
        None,
        alias="requestedObjectName",
        description="Human-readable name of requested object")
    requested_object_type: Optional[RequestableObjectType] = Field(
        None, alias="requestedObjectType")
    __properties = [
        "requestedObjectId", "requestedObjectName", "requestedObjectType"
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
    def from_json(cls, json_str: str) -> AccountRequestInfo:
        """Create an instance of AccountRequestInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountRequestInfo:
        """Create an instance of AccountRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountRequestInfo.parse_obj(obj)

        _obj = AccountRequestInfo.parse_obj({
            "requested_object_id":
            obj.get("requestedObjectId"),
            "requested_object_name":
            obj.get("requestedObjectName"),
            "requested_object_type":
            obj.get("requestedObjectType")
        })
        return _obj
