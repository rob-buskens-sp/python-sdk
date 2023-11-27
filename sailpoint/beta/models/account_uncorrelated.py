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

from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from sailpoint.beta.models.account_uncorrelated_account import AccountUncorrelatedAccount
from sailpoint.beta.models.account_uncorrelated_identity import AccountUncorrelatedIdentity
from sailpoint.beta.models.account_uncorrelated_source import AccountUncorrelatedSource


class AccountUncorrelated(BaseModel):
    """
    AccountUncorrelated
    """
    identity: AccountUncorrelatedIdentity = Field(...)
    source: AccountUncorrelatedSource = Field(...)
    account: AccountUncorrelatedAccount = Field(...)
    entitlement_count: Optional[StrictInt] = Field(
        None,
        alias="entitlementCount",
        description="The number of entitlements associated with this account.")
    __properties = ["identity", "source", "account", "entitlementCount"]

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
    def from_json(cls, json_str: str) -> AccountUncorrelated:
        """Create an instance of AccountUncorrelated from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountUncorrelated:
        """Create an instance of AccountUncorrelated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountUncorrelated.parse_obj(obj)

        _obj = AccountUncorrelated.parse_obj({
            "identity":
            AccountUncorrelatedIdentity.from_dict(obj.get("identity"))
            if obj.get("identity") is not None else None,
            "source":
            AccountUncorrelatedSource.from_dict(obj.get("source"))
            if obj.get("source") is not None else None,
            "account":
            AccountUncorrelatedAccount.from_dict(obj.get("account"))
            if obj.get("account") is not None else None,
            "entitlement_count":
            obj.get("entitlementCount")
        })
        return _obj
