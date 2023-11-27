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
from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from sailpoint.v3.models.approval_status import ApprovalStatus
from sailpoint.v3.models.non_employee_identity_reference_with_id import NonEmployeeIdentityReferenceWithId
from sailpoint.v3.models.non_employee_request_lite import NonEmployeeRequestLite


class NonEmployeeApprovalItem(BaseModel):
    """
    NonEmployeeApprovalItem
    """
    id: Optional[StrictStr] = Field(
        None, description="Non-Employee approval item id")
    approver: Optional[NonEmployeeIdentityReferenceWithId] = None
    account_name: Optional[StrictStr] = Field(
        None,
        alias="accountName",
        description="Requested identity account name")
    approval_status: Optional[ApprovalStatus] = Field(None,
                                                      alias="approvalStatus")
    approval_order: Optional[Union[StrictFloat, StrictInt]] = Field(
        None, alias="approvalOrder", description="Approval order")
    comment: Optional[StrictStr] = Field(None,
                                         description="comment of approver")
    modified: Optional[datetime] = Field(
        None, description="When the request was last modified.")
    created: Optional[datetime] = Field(
        None, description="When the request was created.")
    non_employee_request: Optional[NonEmployeeRequestLite] = Field(
        None, alias="nonEmployeeRequest")
    __properties = [
        "id", "approver", "accountName", "approvalStatus", "approvalOrder",
        "comment", "modified", "created", "nonEmployeeRequest"
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
    def from_json(cls, json_str: str) -> NonEmployeeApprovalItem:
        """Create an instance of NonEmployeeApprovalItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of approver
        if self.approver:
            _dict['approver'] = self.approver.to_dict()
        # override the default output from pydantic by calling `to_dict()` of non_employee_request
        if self.non_employee_request:
            _dict['nonEmployeeRequest'] = self.non_employee_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeApprovalItem:
        """Create an instance of NonEmployeeApprovalItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeApprovalItem.parse_obj(obj)

        _obj = NonEmployeeApprovalItem.parse_obj({
            "id":
            obj.get("id"),
            "approver":
            NonEmployeeIdentityReferenceWithId.from_dict(obj.get("approver"))
            if obj.get("approver") is not None else None,
            "account_name":
            obj.get("accountName"),
            "approval_status":
            obj.get("approvalStatus"),
            "approval_order":
            obj.get("approvalOrder"),
            "comment":
            obj.get("comment"),
            "modified":
            obj.get("modified"),
            "created":
            obj.get("created"),
            "non_employee_request":
            NonEmployeeRequestLite.from_dict(obj.get("nonEmployeeRequest"))
            if obj.get("nonEmployeeRequest") is not None else None
        })
        return _obj
