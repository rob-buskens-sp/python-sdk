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

from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from sailpoint.beta.models.non_employee_schema_attribute import NonEmployeeSchemaAttribute


class NonEmployeeSourceLiteWithSchemaAttributes(BaseModel):
    """
    NonEmployeeSourceLiteWithSchemaAttributes
    """
    id: Optional[StrictStr] = Field(None,
                                    description="Non-Employee source id.")
    source_id: Optional[StrictStr] = Field(
        None,
        alias="sourceId",
        description="Source Id associated with this non-employee source.")
    name: Optional[StrictStr] = Field(
        None,
        description="Source name associated with this non-employee source.")
    description: Optional[StrictStr] = Field(
        None,
        description=
        "Source description associated with this non-employee source.")
    schema_attributes: Optional[conlist(NonEmployeeSchemaAttribute)] = Field(
        None,
        alias="schemaAttributes",
        description=
        "List of schema attributes associated with this non-employee source.")
    __properties = [
        "id", "sourceId", "name", "description", "schemaAttributes"
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
    def from_json(cls,
                  json_str: str) -> NonEmployeeSourceLiteWithSchemaAttributes:
        """Create an instance of NonEmployeeSourceLiteWithSchemaAttributes from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in schema_attributes (list)
        _items = []
        if self.schema_attributes:
            for _item in self.schema_attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schemaAttributes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeSourceLiteWithSchemaAttributes:
        """Create an instance of NonEmployeeSourceLiteWithSchemaAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeSourceLiteWithSchemaAttributes.parse_obj(obj)

        _obj = NonEmployeeSourceLiteWithSchemaAttributes.parse_obj({
            "id":
            obj.get("id"),
            "source_id":
            obj.get("sourceId"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "schema_attributes": [
                NonEmployeeSchemaAttribute.from_dict(_item)
                for _item in obj.get("schemaAttributes")
            ] if obj.get("schemaAttributes") is not None else None
        })
        return _obj
