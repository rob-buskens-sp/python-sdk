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
from v3.models.account_source import AccountSource
from v3.models.attribute_request import AttributeRequest

class OriginalRequest(BaseModel):
    """
    OriginalRequest
    """
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="the account id")
    attribute_requests: Optional[conlist(AttributeRequest)] = Field(None, alias="attributeRequests")
    op: Optional[StrictStr] = Field(None, description="the operation that was used")
    source: Optional[AccountSource] = None
    __properties = ["accountId", "attributeRequests", "op", "source"]

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
    def from_json(cls, json_str: str) -> OriginalRequest:
        """Create an instance of OriginalRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_requests (list)
        _items = []
        if self.attribute_requests:
            for _item in self.attribute_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OriginalRequest:
        """Create an instance of OriginalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OriginalRequest.parse_obj(obj)

        _obj = OriginalRequest.parse_obj({
            "account_id": obj.get("accountId"),
            "attribute_requests": [AttributeRequest.from_dict(_item) for _item in obj.get("attributeRequests")] if obj.get("attributeRequests") is not None else None,
            "op": obj.get("op"),
            "source": AccountSource.from_dict(obj.get("source")) if obj.get("source") is not None else None
        })
        return _obj


