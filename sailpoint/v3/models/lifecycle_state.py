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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from sailpoint.v3.models.account_action import AccountAction
from sailpoint.v3.models.email_notification_option import EmailNotificationOption


class LifecycleState(BaseModel):
    """
    LifecycleState
    """
    id: Optional[StrictStr] = Field(
        None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(..., description="Name of the Object")
    created: Optional[datetime] = Field(
        None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(
        None, description="Last modification date of the Object")
    enabled: Optional[StrictBool] = Field(
        None,
        description="Whether the lifecycle state is enabled or disabled.")
    technical_name: StrictStr = Field(
        ...,
        alias="technicalName",
        description=
        "The technical name for lifecycle state. This is for internal use.")
    description: Optional[StrictStr] = Field(
        None, description="Lifecycle state description.")
    identity_count: Optional[StrictInt] = Field(
        None,
        alias="identityCount",
        description="Number of identities that have the lifecycle state.")
    email_notification_option: Optional[EmailNotificationOption] = Field(
        None, alias="emailNotificationOption")
    account_actions: Optional[conlist(AccountAction)] = Field(
        None, alias="accountActions")
    access_profile_ids: Optional[conlist(
        StrictStr, unique_items=True
    )] = Field(
        None,
        alias="accessProfileIds",
        description=
        "List of unique access-profile IDs that are associated with the lifecycle state."
    )
    __properties = [
        "id", "name", "created", "modified", "enabled", "technicalName",
        "description", "identityCount", "emailNotificationOption",
        "accountActions", "accessProfileIds"
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
    def from_json(cls, json_str: str) -> LifecycleState:
        """Create an instance of LifecycleState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "id",
                              "created",
                              "modified",
                              "identity_count",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of email_notification_option
        if self.email_notification_option:
            _dict[
                'emailNotificationOption'] = self.email_notification_option.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in account_actions (list)
        _items = []
        if self.account_actions:
            for _item in self.account_actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountActions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LifecycleState:
        """Create an instance of LifecycleState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LifecycleState.parse_obj(obj)

        _obj = LifecycleState.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "enabled":
            obj.get("enabled"),
            "technical_name":
            obj.get("technicalName"),
            "description":
            obj.get("description"),
            "identity_count":
            obj.get("identityCount"),
            "email_notification_option":
            EmailNotificationOption.from_dict(
                obj.get("emailNotificationOption"))
            if obj.get("emailNotificationOption") is not None else None,
            "account_actions": [
                AccountAction.from_dict(_item)
                for _item in obj.get("accountActions")
            ] if obj.get("accountActions") is not None else None,
            "access_profile_ids":
            obj.get("accessProfileIds")
        })
        return _obj
