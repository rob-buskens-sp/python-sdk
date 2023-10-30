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
from beta.models.role_insights_insight import RoleInsightsInsight

class RoleInsightsEntitlementChanges(BaseModel):
    """
    RoleInsightsEntitlementChanges
    """
    name: Optional[StrictStr] = Field(None, description="Name of the entitlement")
    id: Optional[StrictStr] = Field(None, description="Id of the entitlement")
    description: Optional[StrictStr] = Field(None, description="Description for the entitlement")
    attribute: Optional[StrictStr] = Field(None, description="Attribute for the entitlement")
    value: Optional[StrictStr] = Field(None, description="Attribute value for the entitlement")
    source: Optional[StrictStr] = Field(None, description="Source or the application for the entitlement")
    insight: Optional[RoleInsightsInsight] = None
    __properties = ["name", "id", "description", "attribute", "value", "source", "insight"]

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
    def from_json(cls, json_str: str) -> RoleInsightsEntitlementChanges:
        """Create an instance of RoleInsightsEntitlementChanges from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of insight
        if self.insight:
            _dict['insight'] = self.insight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleInsightsEntitlementChanges:
        """Create an instance of RoleInsightsEntitlementChanges from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleInsightsEntitlementChanges.parse_obj(obj)

        _obj = RoleInsightsEntitlementChanges.parse_obj({
            "name": obj.get("name"),
            "id": obj.get("id"),
            "description": obj.get("description"),
            "attribute": obj.get("attribute"),
            "value": obj.get("value"),
            "source": obj.get("source"),
            "insight": RoleInsightsInsight.from_dict(obj.get("insight")) if obj.get("insight") is not None else None
        })
        return _obj


