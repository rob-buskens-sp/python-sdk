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
from sailpoint.beta.models.identity_reference_with_id import IdentityReferenceWithId


class NonEmployeeRequestLite(BaseModel):
    """
    NonEmployeeRequestLite
    """
    id: Optional[StrictStr] = Field(None,
                                    description="Non-Employee request id.")
    requester: Optional[IdentityReferenceWithId] = None
    __properties = ["id", "requester"]

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
    def from_json(cls, json_str: str) -> NonEmployeeRequestLite:
        """Create an instance of NonEmployeeRequestLite from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeRequestLite:
        """Create an instance of NonEmployeeRequestLite from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeRequestLite.parse_obj(obj)

        _obj = NonEmployeeRequestLite.parse_obj({
            "id":
            obj.get("id"),
            "requester":
            IdentityReferenceWithId.from_dict(obj.get("requester"))
            if obj.get("requester") is not None else None
        })
        return _obj
