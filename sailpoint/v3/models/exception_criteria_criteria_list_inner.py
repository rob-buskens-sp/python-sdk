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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from v3.models.dto_type import DtoType

class ExceptionCriteriaCriteriaListInner(BaseModel):
    """
    The types of objects supported for SOD violations  # noqa: E501
    """
    type: Optional[Dict[str, Any]] = Field(None, description="The type of object that is referenced")
    id: Optional[StrictStr] = Field(None, description="ID of the object to which this reference applies")
    name: Optional[StrictStr] = Field(None, description="Human-readable display name of the object to which this reference applies")
    existing: Optional[StrictBool] = Field(False, description="Whether the subject identity already had that access or not")
    __properties = ["type", "id", "name", "existing"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ENTITLEMENT'):
            raise ValueError("must be one of enum values ('ENTITLEMENT')")
        return value

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
    def from_json(cls, json_str: str) -> ExceptionCriteriaCriteriaListInner:
        """Create an instance of ExceptionCriteriaCriteriaListInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExceptionCriteriaCriteriaListInner:
        """Create an instance of ExceptionCriteriaCriteriaListInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ExceptionCriteriaCriteriaListInner.parse_obj(obj)

        _obj = ExceptionCriteriaCriteriaListInner.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "existing": obj.get("existing") if obj.get("existing") is not None else False
        })
        return _obj


