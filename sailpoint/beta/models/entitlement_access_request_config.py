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
from pydantic import BaseModel, Field, StrictBool, conlist
from sailpoint.beta.models.entitlement_approval_scheme import EntitlementApprovalScheme


class EntitlementAccessRequestConfig(BaseModel):
    """
    EntitlementAccessRequestConfig
    """
    approval_schemes: Optional[conlist(EntitlementApprovalScheme)] = Field(
        None,
        alias="approvalSchemes",
        description=
        "Ordered list of approval steps for the access request. Empty when no approval is required."
    )
    request_comment_required: Optional[StrictBool] = Field(
        False,
        alias="requestCommentRequired",
        description=
        "If the requester must provide a comment during access request.")
    denial_comment_required: Optional[StrictBool] = Field(
        False,
        alias="denialCommentRequired",
        description=
        "If the reviewer must provide a comment when denying the access request."
    )
    __properties = [
        "approvalSchemes", "requestCommentRequired", "denialCommentRequired"
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
    def from_json(cls, json_str: str) -> EntitlementAccessRequestConfig:
        """Create an instance of EntitlementAccessRequestConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in approval_schemes (list)
        _items = []
        if self.approval_schemes:
            for _item in self.approval_schemes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvalSchemes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntitlementAccessRequestConfig:
        """Create an instance of EntitlementAccessRequestConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntitlementAccessRequestConfig.parse_obj(obj)

        _obj = EntitlementAccessRequestConfig.parse_obj({
            "approval_schemes": [
                EntitlementApprovalScheme.from_dict(_item)
                for _item in obj.get("approvalSchemes")
            ] if obj.get("approvalSchemes") is not None else None,
            "request_comment_required":
            obj.get("requestCommentRequired")
            if obj.get("requestCommentRequired") is not None else False,
            "denial_comment_required":
            obj.get("denialCommentRequired")
            if obj.get("denialCommentRequired") is not None else False
        })
        return _obj
