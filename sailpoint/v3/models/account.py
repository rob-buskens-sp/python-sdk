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

class Account(BaseModel):
    """
    Account
    """
    id: Optional[StrictStr] = Field(None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(..., description="Name of the Object")
    created: Optional[datetime] = Field(None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(None, description="Last modification date of the Object")
    source_id: StrictStr = Field(..., alias="sourceId", description="The unique ID of the source this account belongs to")
    source_name: StrictStr = Field(..., alias="sourceName", description="The display name of the source this account belongs to")
    identity_id: Optional[StrictStr] = Field(None, alias="identityId", description="The unique ID of the identity this account is correlated to")
    attributes: Dict[str, Any] = Field(..., description="The account attributes that are aggregated")
    authoritative: StrictBool = Field(..., description="Indicates if this account is from an authoritative source")
    description: Optional[StrictStr] = Field(None, description="A description of the account")
    disabled: StrictBool = Field(..., description="Indicates if the account is currently disabled")
    locked: StrictBool = Field(..., description="Indicates if the account is currently locked")
    native_identity: StrictStr = Field(..., alias="nativeIdentity", description="The unique ID of the account generated by the source system")
    system_account: StrictBool = Field(..., alias="systemAccount", description="If true, this is a user account within IdentityNow.  If false, this is an account from a source system.")
    uncorrelated: StrictBool = Field(..., description="Indicates if this account is not correlated to an identity")
    uuid: Optional[StrictStr] = Field(None, description="The unique ID of the account as determined by the account schema")
    manually_correlated: StrictBool = Field(..., alias="manuallyCorrelated", description="Indicates if the account has been manually correlated to an identity")
    has_entitlements: StrictBool = Field(..., alias="hasEntitlements", description="Indicates if the account has entitlements")
    __properties = ["id", "name", "created", "modified", "sourceId", "sourceName", "identityId", "attributes", "authoritative", "description", "disabled", "locked", "nativeIdentity", "systemAccount", "uncorrelated", "uuid", "manuallyCorrelated", "hasEntitlements"]

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
    def from_json(cls, json_str: str) -> Account:
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created",
                            "modified",
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if uuid (nullable) is None
        # and __fields_set__ contains the field
        if self.uuid is None and "uuid" in self.__fields_set__:
            _dict['uuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Account:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Account.parse_obj(obj)

        _obj = Account.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "source_id": obj.get("sourceId"),
            "source_name": obj.get("sourceName"),
            "identity_id": obj.get("identityId"),
            "attributes": obj.get("attributes"),
            "authoritative": obj.get("authoritative"),
            "description": obj.get("description"),
            "disabled": obj.get("disabled"),
            "locked": obj.get("locked"),
            "native_identity": obj.get("nativeIdentity"),
            "system_account": obj.get("systemAccount"),
            "uncorrelated": obj.get("uncorrelated"),
            "uuid": obj.get("uuid"),
            "manually_correlated": obj.get("manuallyCorrelated"),
            "has_entitlements": obj.get("hasEntitlements")
        })
        return _obj


