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

from datetime import date, datetime
from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from sailpoint.beta.models.approval_status import ApprovalStatus
from sailpoint.beta.models.identity_reference_with_id import IdentityReferenceWithId
from sailpoint.beta.models.non_employee_source_lite_with_schema_attributes import NonEmployeeSourceLiteWithSchemaAttributes


class NonEmployeeRequestWithoutApprovalItem(BaseModel):
    """
    NonEmployeeRequestWithoutApprovalItem
    """
    id: Optional[StrictStr] = Field(None,
                                    description="Non-Employee request id.")
    requester: Optional[IdentityReferenceWithId] = None
    account_name: Optional[StrictStr] = Field(
        None,
        alias="accountName",
        description="Requested identity account name.")
    first_name: Optional[StrictStr] = Field(
        None, alias="firstName", description="Non-Employee's first name.")
    last_name: Optional[StrictStr] = Field(
        None, alias="lastName", description="Non-Employee's last name.")
    email: Optional[StrictStr] = Field(None,
                                       description="Non-Employee's email.")
    phone: Optional[StrictStr] = Field(None,
                                       description="Non-Employee's phone.")
    manager: Optional[StrictStr] = Field(
        None,
        description=
        "The account ID of a valid identity to serve as this non-employee's manager."
    )
    non_employee_source: Optional[
        NonEmployeeSourceLiteWithSchemaAttributes] = Field(
            None, alias="nonEmployeeSource")
    data: Optional[Dict[str, StrictStr]] = Field(
        None, description="Attribute blob/bag for a non-employee.")
    approval_status: Optional[ApprovalStatus] = Field(None,
                                                      alias="approvalStatus")
    comment: Optional[StrictStr] = Field(None,
                                         description="comment of requester")
    completion_date: Optional[datetime] = Field(
        None,
        alias="completionDate",
        description="When the request was completely approved.")
    start_date: Optional[date] = Field(
        None,
        alias="startDate",
        description="Non-Employee employment start date.")
    end_date: Optional[date] = Field(
        None, alias="endDate", description="Non-Employee employment end date.")
    modified: Optional[datetime] = Field(
        None, description="When the request was last modified.")
    created: Optional[datetime] = Field(
        None, description="When the request was created.")
    __properties = [
        "id", "requester", "accountName", "firstName", "lastName", "email",
        "phone", "manager", "nonEmployeeSource", "data", "approvalStatus",
        "comment", "completionDate", "startDate", "endDate", "modified",
        "created"
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
    def from_json(cls, json_str: str) -> NonEmployeeRequestWithoutApprovalItem:
        """Create an instance of NonEmployeeRequestWithoutApprovalItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of non_employee_source
        if self.non_employee_source:
            _dict['nonEmployeeSource'] = self.non_employee_source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeRequestWithoutApprovalItem:
        """Create an instance of NonEmployeeRequestWithoutApprovalItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeRequestWithoutApprovalItem.parse_obj(obj)

        _obj = NonEmployeeRequestWithoutApprovalItem.parse_obj({
            "id":
            obj.get("id"),
            "requester":
            IdentityReferenceWithId.from_dict(obj.get("requester"))
            if obj.get("requester") is not None else None,
            "account_name":
            obj.get("accountName"),
            "first_name":
            obj.get("firstName"),
            "last_name":
            obj.get("lastName"),
            "email":
            obj.get("email"),
            "phone":
            obj.get("phone"),
            "manager":
            obj.get("manager"),
            "non_employee_source":
            NonEmployeeSourceLiteWithSchemaAttributes.from_dict(
                obj.get("nonEmployeeSource"))
            if obj.get("nonEmployeeSource") is not None else None,
            "data":
            obj.get("data"),
            "approval_status":
            obj.get("approvalStatus"),
            "comment":
            obj.get("comment"),
            "completion_date":
            obj.get("completionDate"),
            "start_date":
            obj.get("startDate"),
            "end_date":
            obj.get("endDate"),
            "modified":
            obj.get("modified"),
            "created":
            obj.get("created")
        })
        return _obj
