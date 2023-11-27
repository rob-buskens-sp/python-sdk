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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from sailpoint.v3.models.attribute_definition import AttributeDefinition
from sailpoint.v3.models.source_feature import SourceFeature


class ModelSchema(BaseModel):
    """
    ModelSchema
    """
    id: Optional[StrictStr] = Field(None, description="The id of the Schema.")
    name: Optional[StrictStr] = Field(None,
                                      description="The name of the Schema.")
    native_object_type: Optional[StrictStr] = Field(
        None,
        alias="nativeObjectType",
        description=
        "The name of the object type on the native system that the schema represents."
    )
    identity_attribute: Optional[StrictStr] = Field(
        None,
        alias="identityAttribute",
        description=
        "The name of the attribute used to calculate the unique identifier for an object in the schema."
    )
    display_attribute: Optional[StrictStr] = Field(
        None,
        alias="displayAttribute",
        description=
        "The name of the attribute used to calculate the display value for an object in the schema."
    )
    hierarchy_attribute: Optional[StrictStr] = Field(
        None,
        alias="hierarchyAttribute",
        description=
        "The name of the attribute whose values represent other objects in a hierarchy. Only relevant to group schemas."
    )
    include_permissions: Optional[StrictBool] = Field(
        None,
        alias="includePermissions",
        description=
        "Flag indicating whether or not the include permissions with the object data when aggregating the schema."
    )
    features: Optional[conlist(SourceFeature)] = Field(
        None, description="The features that the schema supports.")
    configuration: Optional[Dict[str, Any]] = Field(
        None,
        description=
        "Holds any extra configuration data that the schema may require.")
    attributes: Optional[conlist(AttributeDefinition)] = Field(
        None, description="The attribute definitions which form the schema.")
    created: Optional[datetime] = Field(
        None, description="The date the Schema was created.")
    modified: Optional[datetime] = Field(
        None, description="The date the Schema was last modified.")
    __properties = [
        "id", "name", "nativeObjectType", "identityAttribute",
        "displayAttribute", "hierarchyAttribute", "includePermissions",
        "features", "configuration", "attributes", "created", "modified"
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
    def from_json(cls, json_str: str) -> ModelSchema:
        """Create an instance of ModelSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ModelSchema:
        """Create an instance of ModelSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ModelSchema.parse_obj(obj)

        _obj = ModelSchema.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "native_object_type":
            obj.get("nativeObjectType"),
            "identity_attribute":
            obj.get("identityAttribute"),
            "display_attribute":
            obj.get("displayAttribute"),
            "hierarchy_attribute":
            obj.get("hierarchyAttribute"),
            "include_permissions":
            obj.get("includePermissions"),
            "features":
            obj.get("features"),
            "configuration":
            obj.get("configuration"),
            "attributes": [
                AttributeDefinition.from_dict(_item)
                for _item in obj.get("attributes")
            ] if obj.get("attributes") is not None else None,
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified")
        })
        return _obj
