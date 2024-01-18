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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.identity_reference_with_id import IdentityReferenceWithId
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class NonEmployeeSourceWithNECount(BaseModel):
    """
    NonEmployeeSourceWithNECount
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="Non-Employee source id.")
    source_id: Optional[StrictStr] = Field(
        default=None,
        description="Source Id associated with this non-employee source.",
        alias="sourceId")
    name: Optional[StrictStr] = Field(
        default=None,
        description="Source name associated with this non-employee source.")
    description: Optional[StrictStr] = Field(
        default=None,
        description=
        "Source description associated with this non-employee source.")
    approvers: Optional[List[IdentityReferenceWithId]] = Field(
        default=None, description="List of approvers")
    account_managers: Optional[List[IdentityReferenceWithId]] = Field(
        default=None,
        description="List of account managers",
        alias="accountManagers")
    modified: Optional[datetime] = Field(
        default=None, description="When the request was last modified.")
    created: Optional[datetime] = Field(
        default=None, description="When the request was created.")
    non_employee_count: Optional[StrictInt] = Field(
        default=None,
        description=
        "Number of non-employee records associated with this source.",
        alias="nonEmployeeCount")
    __properties: ClassVar[List[str]] = [
        "id", "sourceId", "name", "description", "approvers",
        "accountManagers", "modified", "created", "nonEmployeeCount"
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NonEmployeeSourceWithNECount from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in approvers (list)
        _items = []
        if self.approvers:
            for _item in self.approvers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_managers (list)
        _items = []
        if self.account_managers:
            for _item in self.account_managers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountManagers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NonEmployeeSourceWithNECount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "sourceId":
            obj.get("sourceId"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "approvers": [
                IdentityReferenceWithId.from_dict(_item)
                for _item in obj.get("approvers")
            ] if obj.get("approvers") is not None else None,
            "accountManagers": [
                IdentityReferenceWithId.from_dict(_item)
                for _item in obj.get("accountManagers")
            ] if obj.get("accountManagers") is not None else None,
            "modified":
            obj.get("modified"),
            "created":
            obj.get("created"),
            "nonEmployeeCount":
            obj.get("nonEmployeeCount")
        })
        return _obj
