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


class AccessItemEntitlementResponse(BaseModel):
    """
    AccessItemEntitlementResponse
    """
    access_type: Optional[StrictStr] = Field(
        None,
        alias="accessType",
        description="the access item type. entitlement in this case")
    id: Optional[StrictStr] = Field(None, description="the access item id")
    attribute: Optional[StrictStr] = Field(
        None, description="the entitlement attribute")
    value: Optional[StrictStr] = Field(None,
                                       description="the associated value")
    entitlement_type: Optional[StrictStr] = Field(
        None, alias="entitlementType", description="the type of entitlement")
    source_name: Optional[StrictStr] = Field(
        None, alias="sourceName", description="the name of the source")
    source_id: Optional[StrictStr] = Field(None,
                                           alias="sourceId",
                                           description="the id of the source")
    description: Optional[StrictStr] = Field(
        None, description="the description for the entitlment")
    display_name: Optional[StrictStr] = Field(
        None,
        alias="displayName",
        description="the display name of the identity")
    __properties = [
        "accessType", "id", "attribute", "value", "entitlementType",
        "sourceName", "sourceId", "description", "displayName"
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
    def from_json(cls, json_str: str) -> AccessItemEntitlementResponse:
        """Create an instance of AccessItemEntitlementResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessItemEntitlementResponse:
        """Create an instance of AccessItemEntitlementResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessItemEntitlementResponse.parse_obj(obj)

        _obj = AccessItemEntitlementResponse.parse_obj({
            "access_type":
            obj.get("accessType"),
            "id":
            obj.get("id"),
            "attribute":
            obj.get("attribute"),
            "value":
            obj.get("value"),
            "entitlement_type":
            obj.get("entitlementType"),
            "source_name":
            obj.get("sourceName"),
            "source_id":
            obj.get("sourceId"),
            "description":
            obj.get("description"),
            "display_name":
            obj.get("displayName")
        })
        return _obj
