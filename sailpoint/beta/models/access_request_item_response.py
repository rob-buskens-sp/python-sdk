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
from sailpoint.beta.models.approval_info_response import ApprovalInfoResponse


class AccessRequestItemResponse(BaseModel):
    """
    AccessRequestItemResponse
    """
    operation: Optional[StrictStr] = Field(
        None, description="the access request item operation")
    access_item_type: Optional[StrictStr] = Field(
        None, alias="accessItemType", description="the access item type")
    name: Optional[StrictStr] = Field(
        None, description="the name of access request item")
    decision: Optional[StrictStr] = Field(
        None, description="the final decision for the access request")
    description: Optional[StrictStr] = Field(
        None, description="the description of access request item")
    source_id: Optional[StrictStr] = Field(None,
                                           alias="sourceId",
                                           description="the source id")
    source_name: Optional[StrictStr] = Field(None,
                                             alias="sourceName",
                                             description="the source Name")
    approval_infos: Optional[conlist(ApprovalInfoResponse)] = Field(
        None, alias="approvalInfos")
    __properties = [
        "operation", "accessItemType", "name", "decision", "description",
        "sourceId", "sourceName", "approvalInfos"
    ]

    @validator('decision')
    def decision_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('APPROVED', 'REJECTED'):
            raise ValueError(
                "must be one of enum values ('APPROVED', 'REJECTED')")
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
    def from_json(cls, json_str: str) -> AccessRequestItemResponse:
        """Create an instance of AccessRequestItemResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in approval_infos (list)
        _items = []
        if self.approval_infos:
            for _item in self.approval_infos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvalInfos'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRequestItemResponse:
        """Create an instance of AccessRequestItemResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequestItemResponse.parse_obj(obj)

        _obj = AccessRequestItemResponse.parse_obj({
            "operation":
            obj.get("operation"),
            "access_item_type":
            obj.get("accessItemType"),
            "name":
            obj.get("name"),
            "decision":
            obj.get("decision"),
            "description":
            obj.get("description"),
            "source_id":
            obj.get("sourceId"),
            "source_name":
            obj.get("sourceName"),
            "approval_infos": [
                ApprovalInfoResponse.from_dict(_item)
                for _item in obj.get("approvalInfos")
            ] if obj.get("approvalInfos") is not None else None
        })
        return _obj
