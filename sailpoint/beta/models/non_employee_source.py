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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from sailpoint.beta.models.identity_reference_with_id import IdentityReferenceWithId


class NonEmployeeSource(BaseModel):
    """
    NonEmployeeSource
    """
    id: Optional[StrictStr] = Field(None,
                                    description="Non-Employee source id.")
    source_id: Optional[StrictStr] = Field(
        None,
        alias="sourceId",
        description="Source Id associated with this non-employee source.")
    name: Optional[StrictStr] = Field(
        None,
        description="Source name associated with this non-employee source.")
    description: Optional[StrictStr] = Field(
        None,
        description=
        "Source description associated with this non-employee source.")
    approvers: Optional[conlist(IdentityReferenceWithId)] = Field(
        None, description="List of approvers")
    account_managers: Optional[conlist(IdentityReferenceWithId)] = Field(
        None, alias="accountManagers", description="List of account managers")
    modified: Optional[datetime] = Field(
        None, description="When the request was last modified.")
    created: Optional[datetime] = Field(
        None, description="When the request was created.")
    non_employee_count: Optional[StrictInt] = Field(
        None,
        alias="nonEmployeeCount",
        description=
        "The number of non-employee records on all sources that *requested-for* user manages."
    )
    __properties = [
        "id", "sourceId", "name", "description", "approvers",
        "accountManagers", "modified", "created", "nonEmployeeCount"
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
    def from_json(cls, json_str: str) -> NonEmployeeSource:
        """Create an instance of NonEmployeeSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
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
        # set to None if non_employee_count (nullable) is None
        # and __fields_set__ contains the field
        if self.non_employee_count is None and "non_employee_count" in self.__fields_set__:
            _dict['nonEmployeeCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeSource:
        """Create an instance of NonEmployeeSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeSource.parse_obj(obj)

        _obj = NonEmployeeSource.parse_obj({
            "id":
            obj.get("id"),
            "source_id":
            obj.get("sourceId"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "approvers": [
                IdentityReferenceWithId.from_dict(_item)
                for _item in obj.get("approvers")
            ] if obj.get("approvers") is not None else None,
            "account_managers": [
                IdentityReferenceWithId.from_dict(_item)
                for _item in obj.get("accountManagers")
            ] if obj.get("accountManagers") is not None else None,
            "modified":
            obj.get("modified"),
            "created":
            obj.get("created"),
            "non_employee_count":
            obj.get("nonEmployeeCount")
        })
        return _obj
