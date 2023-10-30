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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr

class IdentityHistoryResponse(BaseModel):
    """
    IdentityHistoryResponse
    """
    id: Optional[StrictStr] = Field(None, description="the identity ID")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="the display name of the identity")
    snapshot: Optional[StrictStr] = Field(None, description="the date when the identity record was created")
    deleted_date: Optional[StrictStr] = Field(None, alias="deletedDate", description="the date when the identity was deleted")
    access_item_count: Optional[Dict[str, StrictStr]] = Field(None, alias="accessItemCount", description="A map containing the count of each access item")
    attributes: Optional[Dict[str, StrictStr]] = Field(None, description="A map containing the identity attributes")
    __properties = ["id", "displayName", "snapshot", "deletedDate", "accessItemCount", "attributes"]

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
    def from_json(cls, json_str: str) -> IdentityHistoryResponse:
        """Create an instance of IdentityHistoryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityHistoryResponse:
        """Create an instance of IdentityHistoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityHistoryResponse.parse_obj(obj)

        _obj = IdentityHistoryResponse.parse_obj({
            "id": obj.get("id"),
            "display_name": obj.get("displayName"),
            "snapshot": obj.get("snapshot"),
            "deleted_date": obj.get("deletedDate"),
            "access_item_count": obj.get("accessItemCount"),
            "attributes": obj.get("attributes")
        })
        return _obj


