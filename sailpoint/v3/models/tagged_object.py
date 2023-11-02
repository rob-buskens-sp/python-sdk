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
from pydantic import BaseModel, Field, StrictStr, conlist
from v3.models.tagged_object_dto import TaggedObjectDto

class TaggedObject(BaseModel):
    """
    Tagged object.  # noqa: E501
    """
    object_ref: Optional[TaggedObjectDto] = Field(None, alias="objectRef")
    tags: Optional[conlist(StrictStr)] = Field(None, description="Labels to be applied to an Object")
    __properties = ["objectRef", "tags"]

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
    def from_json(cls, json_str: str) -> TaggedObject:
        """Create an instance of TaggedObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of object_ref
        if self.object_ref:
            _dict['objectRef'] = self.object_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaggedObject:
        """Create an instance of TaggedObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaggedObject.parse_obj(obj)

        _obj = TaggedObject.parse_obj({
            "object_ref": TaggedObjectDto.from_dict(obj.get("objectRef")) if obj.get("objectRef") is not None else None,
            "tags": obj.get("tags")
        })
        return _obj


