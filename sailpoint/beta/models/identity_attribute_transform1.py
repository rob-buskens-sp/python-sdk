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
from sailpoint.beta.models.transform_definition1 import TransformDefinition1


class IdentityAttributeTransform1(BaseModel):
    """
    Defines a transformation definition for an identity attribute.  # noqa: E501
    """
    identity_attribute_name: Optional[StrictStr] = Field(
        None,
        alias="identityAttributeName",
        description="Name of the identity attribute.")
    transform_definition: Optional[TransformDefinition1] = Field(
        None, alias="transformDefinition")
    __properties = ["identityAttributeName", "transformDefinition"]

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
    def from_json(cls, json_str: str) -> IdentityAttributeTransform1:
        """Create an instance of IdentityAttributeTransform1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transform_definition
        if self.transform_definition:
            _dict['transformDefinition'] = self.transform_definition.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityAttributeTransform1:
        """Create an instance of IdentityAttributeTransform1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityAttributeTransform1.parse_obj(obj)

        _obj = IdentityAttributeTransform1.parse_obj({
            "identity_attribute_name":
            obj.get("identityAttributeName"),
            "transform_definition":
            TransformDefinition1.from_dict(obj.get("transformDefinition"))
            if obj.get("transformDefinition") is not None else None
        })
        return _obj
