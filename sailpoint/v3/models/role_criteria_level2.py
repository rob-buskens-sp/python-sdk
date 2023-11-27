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
from sailpoint.v3.models.role_criteria_key import RoleCriteriaKey
from sailpoint.v3.models.role_criteria_level3 import RoleCriteriaLevel3
from sailpoint.v3.models.role_criteria_operation import RoleCriteriaOperation


class RoleCriteriaLevel2(BaseModel):
    """
    Defines STANDARD type Role membership  # noqa: E501
    """
    operation: Optional[RoleCriteriaOperation] = None
    key: Optional[RoleCriteriaKey] = None
    string_value: Optional[StrictStr] = Field(
        None,
        alias="stringValue",
        description=
        "String value to test the Identity attribute, Account attribute, or Entitlement specified in the key w/r/t the specified operation. If this criteria is a leaf node, that is, if the operation is one of EQUALS, NOT_EQUALS, CONTAINS, STARTS_WITH, or ENDS_WITH, this field is required. Otherwise, specifying it is an error."
    )
    children: Optional[conlist(RoleCriteriaLevel3)] = Field(
        None,
        description=
        "Array of child criteria. Required if the operation is AND or OR, otherwise it must be left null. A maximum of three levels of criteria are supported, including leaf nodes. Additionally, AND nodes can only be children or OR nodes and vice-versa."
    )
    __properties = ["operation", "key", "stringValue", "children"]

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
    def from_json(cls, json_str: str) -> RoleCriteriaLevel2:
        """Create an instance of RoleCriteriaLevel2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of key
        if self.key:
            _dict['key'] = self.key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item in self.children:
                if _item:
                    _items.append(_item.to_dict())
            _dict['children'] = _items
        # set to None if key (nullable) is None
        # and __fields_set__ contains the field
        if self.key is None and "key" in self.__fields_set__:
            _dict['key'] = None

        # set to None if string_value (nullable) is None
        # and __fields_set__ contains the field
        if self.string_value is None and "string_value" in self.__fields_set__:
            _dict['stringValue'] = None

        # set to None if children (nullable) is None
        # and __fields_set__ contains the field
        if self.children is None and "children" in self.__fields_set__:
            _dict['children'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleCriteriaLevel2:
        """Create an instance of RoleCriteriaLevel2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleCriteriaLevel2.parse_obj(obj)

        _obj = RoleCriteriaLevel2.parse_obj({
            "operation":
            obj.get("operation"),
            "key":
            RoleCriteriaKey.from_dict(obj.get("key"))
            if obj.get("key") is not None else None,
            "string_value":
            obj.get("stringValue"),
            "children": [
                RoleCriteriaLevel3.from_dict(_item)
                for _item in obj.get("children")
            ] if obj.get("children") is not None else None
        })
        return _obj
