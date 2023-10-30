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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from beta.models.condition_effect import ConditionEffect
from beta.models.condition_rule import ConditionRule

class FormCondition(BaseModel):
    """
    Represent a form conditional.  # noqa: E501
    """
    rule_operator: Optional[StrictStr] = Field(None, alias="ruleOperator", description="ConditionRuleLogicalOperatorType value. AND ConditionRuleLogicalOperatorTypeAnd OR ConditionRuleLogicalOperatorTypeOr")
    rules: Optional[conlist(ConditionRule)] = Field(None, description="List of rules.")
    effects: Optional[conlist(ConditionEffect)] = Field(None, description="List of effects.")
    __properties = ["ruleOperator", "rules", "effects"]

    @validator('rule_operator')
    def rule_operator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('AND', 'OR'):
            raise ValueError("must be one of enum values ('AND', 'OR')")
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
    def from_json(cls, json_str: str) -> FormCondition:
        """Create an instance of FormCondition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in effects (list)
        _items = []
        if self.effects:
            for _item in self.effects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['effects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FormCondition:
        """Create an instance of FormCondition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FormCondition.parse_obj(obj)

        _obj = FormCondition.parse_obj({
            "rule_operator": obj.get("ruleOperator"),
            "rules": [ConditionRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None,
            "effects": [ConditionEffect.from_dict(_item) for _item in obj.get("effects")] if obj.get("effects") is not None else None
        })
        return _obj


