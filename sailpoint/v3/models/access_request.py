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

from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from sailpoint.v3.models.access_request_item import AccessRequestItem
from sailpoint.v3.models.access_request_type import AccessRequestType


class AccessRequest(BaseModel):
    """
    AccessRequest
    """
    requested_for: conlist(StrictStr) = Field(
        ...,
        alias="requestedFor",
        description=
        "A list of Identity IDs for whom the Access is requested. If it's a Revoke request, there can only be one Identity ID."
    )
    request_type: Optional[AccessRequestType] = Field(None,
                                                      alias="requestType")
    requested_items: conlist(AccessRequestItem) = Field(
        ..., alias="requestedItems")
    client_metadata: Optional[Dict[str, StrictStr]] = Field(
        None,
        alias="clientMetadata",
        description=
        "Arbitrary key-value pairs. They will never be processed by the IdentityNow system but will be returned on associated APIs such as /account-activities."
    )
    __properties = [
        "requestedFor", "requestType", "requestedItems", "clientMetadata"
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
    def from_json(cls, json_str: str) -> AccessRequest:
        """Create an instance of AccessRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in requested_items (list)
        _items = []
        if self.requested_items:
            for _item in self.requested_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requestedItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRequest:
        """Create an instance of AccessRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequest.parse_obj(obj)

        _obj = AccessRequest.parse_obj({
            "requested_for":
            obj.get("requestedFor"),
            "request_type":
            obj.get("requestType"),
            "requested_items": [
                AccessRequestItem.from_dict(_item)
                for _item in obj.get("requestedItems")
            ] if obj.get("requestedItems") is not None else None,
            "client_metadata":
            obj.get("clientMetadata")
        })
        return _obj
