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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from beta.models.attribute_definition_schema import AttributeDefinitionSchema
from beta.models.attribute_definition_type import AttributeDefinitionType

class AttributeDefinition(BaseModel):
    """
    AttributeDefinition
    """
    name: Optional[StrictStr] = Field(None, description="The name of the attribute.")
    type: Optional[AttributeDefinitionType] = None
    var_schema: Optional[AttributeDefinitionSchema] = Field(None, alias="schema")
    description: Optional[StrictStr] = Field(None, description="A human-readable description of the attribute.")
    is_multi: Optional[StrictBool] = Field(False, alias="isMulti", description="Flag indicating whether or not the attribute is multi-valued.")
    is_entitlement: Optional[StrictBool] = Field(False, alias="isEntitlement", description="Flag indicating whether or not the attribute is an entitlement.")
    is_group: Optional[StrictBool] = Field(False, alias="isGroup", description="Flag indicating whether or not the attribute represents a group. This can only be `true` if `isEntitlement` is also `true` **and** there is a schema defined for the attribute. ")
    __properties = ["name", "type", "schema", "description", "isMulti", "isEntitlement", "isGroup"]

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
    def from_json(cls, json_str: str) -> AttributeDefinition:
        """Create an instance of AttributeDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_schema
        if self.var_schema:
            _dict['schema'] = self.var_schema.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AttributeDefinition:
        """Create an instance of AttributeDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AttributeDefinition.parse_obj(obj)

        _obj = AttributeDefinition.parse_obj({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "var_schema": AttributeDefinitionSchema.from_dict(obj.get("schema")) if obj.get("schema") is not None else None,
            "description": obj.get("description"),
            "is_multi": obj.get("isMulti") if obj.get("isMulti") is not None else False,
            "is_entitlement": obj.get("isEntitlement") if obj.get("isEntitlement") is not None else False,
            "is_group": obj.get("isGroup") if obj.get("isGroup") is not None else False
        })
        return _obj


