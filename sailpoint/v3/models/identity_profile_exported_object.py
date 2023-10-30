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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from v3.models.base_reference_dto import BaseReferenceDto
from v3.models.identity_profile import IdentityProfile

class IdentityProfileExportedObject(BaseModel):
    """
    Identity Profile exported object  # noqa: E501
    """
    version: Optional[StrictInt] = Field(None, description="Version or object from the target service.")
    var_self: Optional[BaseReferenceDto] = Field(None, alias="self")
    object: Optional[IdentityProfile] = None
    __properties = ["version", "self", "object"]

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
    def from_json(cls, json_str: str) -> IdentityProfileExportedObject:
        """Create an instance of IdentityProfileExportedObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of object
        if self.object:
            _dict['object'] = self.object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityProfileExportedObject:
        """Create an instance of IdentityProfileExportedObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityProfileExportedObject.parse_obj(obj)

        _obj = IdentityProfileExportedObject.parse_obj({
            "version": obj.get("version"),
            "var_self": BaseReferenceDto.from_dict(obj.get("self")) if obj.get("self") is not None else None,
            "object": IdentityProfile.from_dict(obj.get("object")) if obj.get("object") is not None else None
        })
        return _obj


