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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from v3.models.account_source import AccountSource

class BaseAccount(BaseModel):
    """
    BaseAccount
    """
    id: Optional[StrictStr] = Field(None, description="The unique ID of the referenced object.")
    name: Optional[StrictStr] = Field(None, description="The human readable name of the referenced object.")
    account_id: Optional[StrictStr] = Field(None, alias="accountId", description="The ID of the account")
    source: Optional[AccountSource] = None
    disabled: Optional[StrictBool] = Field(None, description="Indicates if the account is disabled")
    locked: Optional[StrictBool] = Field(None, description="Indicates if the account is locked")
    privileged: Optional[StrictBool] = None
    manually_correlated: Optional[StrictBool] = Field(None, alias="manuallyCorrelated", description="Indicates if the account has been manually correlated to an identity")
    password_last_set: Optional[datetime] = Field(None, alias="passwordLastSet", description="A date-time in ISO-8601 format")
    entitlement_attributes: Optional[Dict[str, Any]] = Field(None, alias="entitlementAttributes", description="a map or dictionary of key/value pairs")
    created: Optional[datetime] = Field(None, description="A date-time in ISO-8601 format")
    __properties = ["id", "name", "accountId", "source", "disabled", "locked", "privileged", "manuallyCorrelated", "passwordLastSet", "entitlementAttributes", "created"]

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
    def from_json(cls, json_str: str) -> BaseAccount:
        """Create an instance of BaseAccount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # set to None if password_last_set (nullable) is None
        # and __fields_set__ contains the field
        if self.password_last_set is None and "password_last_set" in self.__fields_set__:
            _dict['passwordLastSet'] = None

        # set to None if entitlement_attributes (nullable) is None
        # and __fields_set__ contains the field
        if self.entitlement_attributes is None and "entitlement_attributes" in self.__fields_set__:
            _dict['entitlementAttributes'] = None

        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaseAccount:
        """Create an instance of BaseAccount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseAccount.parse_obj(obj)

        _obj = BaseAccount.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "account_id": obj.get("accountId"),
            "source": AccountSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "disabled": obj.get("disabled"),
            "locked": obj.get("locked"),
            "privileged": obj.get("privileged"),
            "manually_correlated": obj.get("manuallyCorrelated"),
            "password_last_set": obj.get("passwordLastSet"),
            "entitlement_attributes": obj.get("entitlementAttributes"),
            "created": obj.get("created")
        })
        return _obj


