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

from datetime import date, datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.approval_status import ApprovalStatus
from sailpoint.v3.models.non_employee_identity_reference_with_id import NonEmployeeIdentityReferenceWithId
from sailpoint.v3.models.non_employee_source_lite_with_schema_attributes import NonEmployeeSourceLiteWithSchemaAttributes
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NonEmployeeRequestWithoutApprovalItem(BaseModel):
    """
    NonEmployeeRequestWithoutApprovalItem
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Non-Employee request id.")
    requester: Optional[NonEmployeeIdentityReferenceWithId] = None
    account_name: Optional[StrictStr] = Field(default=None, description="Requested identity account name.", alias="accountName")
    first_name: Optional[StrictStr] = Field(default=None, description="Non-Employee's first name.", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="Non-Employee's last name.", alias="lastName")
    email: Optional[StrictStr] = Field(default=None, description="Non-Employee's email.")
    phone: Optional[StrictStr] = Field(default=None, description="Non-Employee's phone.")
    manager: Optional[StrictStr] = Field(default=None, description="The account ID of a valid identity to serve as this non-employee's manager.")
    non_employee_source: Optional[NonEmployeeSourceLiteWithSchemaAttributes] = Field(default=None, alias="nonEmployeeSource")
    data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Attribute blob/bag for a non-employee.")
    approval_status: Optional[ApprovalStatus] = Field(default=None, alias="approvalStatus")
    comment: Optional[StrictStr] = Field(default=None, description="comment of requester")
    completion_date: Optional[datetime] = Field(default=None, description="When the request was completely approved.", alias="completionDate")
    start_date: Optional[date] = Field(default=None, description="Non-Employee employment start date.", alias="startDate")
    end_date: Optional[date] = Field(default=None, description="Non-Employee employment end date.", alias="endDate")
    modified: Optional[datetime] = Field(default=None, description="When the request was last modified.")
    created: Optional[datetime] = Field(default=None, description="When the request was created.")
    __properties: ClassVar[List[str]] = ["id", "requester", "accountName", "firstName", "lastName", "email", "phone", "manager", "nonEmployeeSource", "data", "approvalStatus", "comment", "completionDate", "startDate", "endDate", "modified", "created"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NonEmployeeRequestWithoutApprovalItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of non_employee_source
        if self.non_employee_source:
            _dict['nonEmployeeSource'] = self.non_employee_source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NonEmployeeRequestWithoutApprovalItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "requester": NonEmployeeIdentityReferenceWithId.from_dict(obj.get("requester")) if obj.get("requester") is not None else None,
            "accountName": obj.get("accountName"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "manager": obj.get("manager"),
            "nonEmployeeSource": NonEmployeeSourceLiteWithSchemaAttributes.from_dict(obj.get("nonEmployeeSource")) if obj.get("nonEmployeeSource") is not None else None,
            "data": obj.get("data"),
            "approvalStatus": obj.get("approvalStatus"),
            "comment": obj.get("comment"),
            "completionDate": obj.get("completionDate"),
            "startDate": obj.get("startDate"),
            "endDate": obj.get("endDate"),
            "modified": obj.get("modified"),
            "created": obj.get("created")
        })
        return _obj


