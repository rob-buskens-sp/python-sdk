# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, conlist
from cc.models.list_connectors200_response_items_inner import ListConnectors200ResponseItemsInner

class ListConnectors200Response(BaseModel):
    """
    ListConnectors200Response
    """
    total: Optional[Union[StrictFloat, StrictInt]] = None
    items: Optional[conlist(ListConnectors200ResponseItemsInner)] = None
    __properties = ["total", "items"]

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
    def from_json(cls, json_str: str) -> ListConnectors200Response:
        """Create an instance of ListConnectors200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListConnectors200Response:
        """Create an instance of ListConnectors200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListConnectors200Response.parse_obj(obj)

        _obj = ListConnectors200Response.parse_obj({
            "total": obj.get("total"),
            "items": [ListConnectors200ResponseItemsInner.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None
        })
        return _obj


