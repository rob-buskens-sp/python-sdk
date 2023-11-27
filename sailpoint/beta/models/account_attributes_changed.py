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

from typing import List
from pydantic import BaseModel, Field, conlist
from sailpoint.beta.models.account_attributes_changed_account import AccountAttributesChangedAccount
from sailpoint.beta.models.account_attributes_changed_changes_inner import AccountAttributesChangedChangesInner
from sailpoint.beta.models.account_attributes_changed_identity import AccountAttributesChangedIdentity
from sailpoint.beta.models.account_attributes_changed_source import AccountAttributesChangedSource


class AccountAttributesChanged(BaseModel):
    """
    AccountAttributesChanged
    """
    identity: AccountAttributesChangedIdentity = Field(...)
    source: AccountAttributesChangedSource = Field(...)
    account: AccountAttributesChangedAccount = Field(...)
    changes: conlist(AccountAttributesChangedChangesInner) = Field(
        ..., description="A list of attributes that changed.")
    __properties = ["identity", "source", "account", "changes"]

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
    def from_json(cls, json_str: str) -> AccountAttributesChanged:
        """Create an instance of AccountAttributesChanged from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountAttributesChanged:
        """Create an instance of AccountAttributesChanged from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountAttributesChanged.parse_obj(obj)

        _obj = AccountAttributesChanged.parse_obj({
            "identity":
            AccountAttributesChangedIdentity.from_dict(obj.get("identity"))
            if obj.get("identity") is not None else None,
            "source":
            AccountAttributesChangedSource.from_dict(obj.get("source"))
            if obj.get("source") is not None else None,
            "account":
            AccountAttributesChangedAccount.from_dict(obj.get("account"))
            if obj.get("account") is not None else None,
            "changes": [
                AccountAttributesChangedChangesInner.from_dict(_item)
                for _item in obj.get("changes")
            ] if obj.get("changes") is not None else None
        })
        return _obj
