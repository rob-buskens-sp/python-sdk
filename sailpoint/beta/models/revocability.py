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
from beta.models.access_profile_approval_scheme import AccessProfileApprovalScheme

class Revocability(BaseModel):
    """
    Revocability
    """
    comments_required: Optional[StrictBool] = Field(False, alias="commentsRequired", description="Whether the requester of the containing object must provide comments justifying the request")
    denial_comments_required: Optional[StrictBool] = Field(False, alias="denialCommentsRequired", description="Whether an approver must provide comments when denying the request")
    approval_schemes: Optional[conlist(AccessProfileApprovalScheme)] = Field(None, alias="approvalSchemes", description="List describing the steps in approving the revocation request")
    __properties = ["commentsRequired", "denialCommentsRequired", "approvalSchemes"]

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
    def from_json(cls, json_str: str) -> Revocability:
        """Create an instance of Revocability from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in approval_schemes (list)
        _items = []
        if self.approval_schemes:
            for _item in self.approval_schemes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvalSchemes'] = _items
        # set to None if comments_required (nullable) is None
        # and __fields_set__ contains the field
        if self.comments_required is None and "comments_required" in self.__fields_set__:
            _dict['commentsRequired'] = None

        # set to None if denial_comments_required (nullable) is None
        # and __fields_set__ contains the field
        if self.denial_comments_required is None and "denial_comments_required" in self.__fields_set__:
            _dict['denialCommentsRequired'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Revocability:
        """Create an instance of Revocability from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Revocability.parse_obj(obj)

        _obj = Revocability.parse_obj({
            "comments_required": obj.get("commentsRequired") if obj.get("commentsRequired") is not None else False,
            "denial_comments_required": obj.get("denialCommentsRequired") if obj.get("denialCommentsRequired") is not None else False,
            "approval_schemes": [AccessProfileApprovalScheme.from_dict(_item) for _item in obj.get("approvalSchemes")] if obj.get("approvalSchemes") is not None else None
        })
        return _obj


