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
from sailpoint.beta.models.provisioning_criteria_level2 import ProvisioningCriteriaLevel2
from sailpoint.beta.models.provisioning_criteria_operation import ProvisioningCriteriaOperation


class ProvisioningCriteriaLevel1(BaseModel):
    """
    Defines matching criteria for an Account to be provisioned with a specific Access Profile  # noqa: E501
    """
    operation: Optional[ProvisioningCriteriaOperation] = None
    attribute: Optional[StrictStr] = Field(
        None,
        description=
        "Name of the Account attribute to be tested. If **operation** is one of EQUALS, NOT_EQUALS, CONTAINS, or HAS, this field is required. Otherwise, specifying it is an error."
    )
    value: Optional[StrictStr] = Field(
        None,
        description=
        "String value to test the Account attribute w/r/t the specified operation. If the operation is one of EQUALS, NOT_EQUALS, or CONTAINS, this field is required. Otherwise, specifying it is an error. If the Attribute is not String-typed, it will be converted to the appropriate type."
    )
    children: Optional[conlist(ProvisioningCriteriaLevel2)] = Field(
        None,
        description=
        "Array of child criteria. Required if the operation is AND or OR, otherwise it must be left null. A maximum of three levels of criteria are supported, including leaf nodes."
    )
    __properties = ["operation", "attribute", "value", "children"]

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
    def from_json(cls, json_str: str) -> ProvisioningCriteriaLevel1:
        """Create an instance of ProvisioningCriteriaLevel1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in children (list)
        _items = []
        if self.children:
            for _item in self.children:
                if _item:
                    _items.append(_item.to_dict())
            _dict['children'] = _items
        # set to None if attribute (nullable) is None
        # and __fields_set__ contains the field
        if self.attribute is None and "attribute" in self.__fields_set__:
            _dict['attribute'] = None

        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        # set to None if children (nullable) is None
        # and __fields_set__ contains the field
        if self.children is None and "children" in self.__fields_set__:
            _dict['children'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProvisioningCriteriaLevel1:
        """Create an instance of ProvisioningCriteriaLevel1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProvisioningCriteriaLevel1.parse_obj(obj)

        _obj = ProvisioningCriteriaLevel1.parse_obj({
            "operation":
            obj.get("operation"),
            "attribute":
            obj.get("attribute"),
            "value":
            obj.get("value"),
            "children": [
                ProvisioningCriteriaLevel2.from_dict(_item)
                for _item in obj.get("children")
            ] if obj.get("children") is not None else None
        })
        return _obj
