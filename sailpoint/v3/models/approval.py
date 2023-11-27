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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from sailpoint.v3.models.account_source import AccountSource
from sailpoint.v3.models.approval_comment import ApprovalComment


class Approval(BaseModel):
    """
    Approval
    """
    comments: Optional[conlist(ApprovalComment)] = None
    created: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    modified: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    owner: Optional[AccountSource] = None
    result: Optional[StrictStr] = Field(
        None, description="The result of the approval")
    type: Optional[StrictStr] = None
    __properties = [
        "comments", "created", "modified", "owner", "result", "type"
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
    def from_json(cls, json_str: str) -> Approval:
        """Create an instance of Approval from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if modified (nullable) is None
        # and __fields_set__ contains the field
        if self.modified is None and "modified" in self.__fields_set__:
            _dict['modified'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Approval:
        """Create an instance of Approval from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Approval.parse_obj(obj)

        _obj = Approval.parse_obj({
            "comments": [
                ApprovalComment.from_dict(_item)
                for _item in obj.get("comments")
            ] if obj.get("comments") is not None else None,
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "owner":
            AccountSource.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "result":
            obj.get("result"),
            "type":
            obj.get("type")
        })
        return _obj
