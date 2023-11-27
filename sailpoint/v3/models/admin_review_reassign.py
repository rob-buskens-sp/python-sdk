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
from sailpoint.v3.models.admin_review_reassign_reassign_to import AdminReviewReassignReassignTo


class AdminReviewReassign(BaseModel):
    """
    AdminReviewReassign
    """
    certification_ids: Optional[conlist(
        StrictStr, max_items=250, min_items=1)] = Field(
            None,
            alias="certificationIds",
            description="List of certification IDs to reassign")
    reassign_to: Optional[AdminReviewReassignReassignTo] = Field(
        None, alias="reassignTo")
    reason: Optional[StrictStr] = Field(
        None,
        description="Comment to explain why the certification was reassigned")
    __properties = ["certificationIds", "reassignTo", "reason"]

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
    def from_json(cls, json_str: str) -> AdminReviewReassign:
        """Create an instance of AdminReviewReassign from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reassign_to
        if self.reassign_to:
            _dict['reassignTo'] = self.reassign_to.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdminReviewReassign:
        """Create an instance of AdminReviewReassign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdminReviewReassign.parse_obj(obj)

        _obj = AdminReviewReassign.parse_obj({
            "certification_ids":
            obj.get("certificationIds"),
            "reassign_to":
            AdminReviewReassignReassignTo.from_dict(obj.get("reassignTo"))
            if obj.get("reassignTo") is not None else None,
            "reason":
            obj.get("reason")
        })
        return _obj
