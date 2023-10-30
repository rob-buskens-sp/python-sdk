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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from beta.models.role_insights_insight import RoleInsightsInsight
from beta.models.role_insights_role import RoleInsightsRole

class RoleInsight(BaseModel):
    """
    RoleInsight
    """
    id: Optional[StrictStr] = Field(None, description="Insight id")
    number_of_updates: Optional[StrictInt] = Field(None, alias="numberOfUpdates", description="Total number of updates for this role")
    created_date: Optional[datetime] = Field(None, alias="createdDate", description="The date-time insights were last created for this role.")
    role: Optional[RoleInsightsRole] = None
    insight: Optional[RoleInsightsInsight] = None
    __properties = ["id", "numberOfUpdates", "createdDate", "role", "insight"]

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
    def from_json(cls, json_str: str) -> RoleInsight:
        """Create an instance of RoleInsight from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of insight
        if self.insight:
            _dict['insight'] = self.insight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleInsight:
        """Create an instance of RoleInsight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleInsight.parse_obj(obj)

        _obj = RoleInsight.parse_obj({
            "id": obj.get("id"),
            "number_of_updates": obj.get("numberOfUpdates"),
            "created_date": obj.get("createdDate"),
            "role": RoleInsightsRole.from_dict(obj.get("role")) if obj.get("role") is not None else None,
            "insight": RoleInsightsInsight.from_dict(obj.get("insight")) if obj.get("insight") is not None else None
        })
        return _obj


