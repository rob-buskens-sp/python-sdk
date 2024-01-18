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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Account(BaseModel):
    """
    Account
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(
        default=None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(description="Name of the Object")
    created: Optional[datetime] = Field(
        default=None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(
        default=None, description="Last modification date of the Object")
    source_id: StrictStr = Field(
        description="The unique ID of the source this account belongs to",
        alias="sourceId")
    source_name: StrictStr = Field(
        description="The display name of the source this account belongs to",
        alias="sourceName")
    identity_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "The unique ID of the identity this account is correlated to",
        alias="identityId")
    attributes: Dict[str, Any] = Field(
        description="The account attributes that are aggregated")
    authoritative: StrictBool = Field(
        description="Indicates if this account is from an authoritative source"
    )
    description: Optional[StrictStr] = Field(
        default=None, description="A description of the account")
    disabled: StrictBool = Field(
        description="Indicates if the account is currently disabled")
    locked: StrictBool = Field(
        description="Indicates if the account is currently locked")
    native_identity: StrictStr = Field(
        description=
        "The unique ID of the account generated by the source system",
        alias="nativeIdentity")
    system_account: StrictBool = Field(
        description=
        "If true, this is a user account within IdentityNow.  If false, this is an account from a source system.",
        alias="systemAccount")
    uncorrelated: StrictBool = Field(
        description="Indicates if this account is not correlated to an identity"
    )
    uuid: Optional[StrictStr] = Field(
        default=None,
        description=
        "The unique ID of the account as determined by the account schema")
    manually_correlated: StrictBool = Field(
        description=
        "Indicates if the account has been manually correlated to an identity",
        alias="manuallyCorrelated")
    has_entitlements: StrictBool = Field(
        description="Indicates if the account has entitlements",
        alias="hasEntitlements")
    __properties: ClassVar[List[str]] = [
        "id", "name", "created", "modified", "sourceId", "sourceName",
        "identityId", "attributes", "authoritative", "description", "disabled",
        "locked", "nativeIdentity", "systemAccount", "uncorrelated", "uuid",
        "manuallyCorrelated", "hasEntitlements"
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
        """Create an instance of Account from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created",
                "modified",
            },
            exclude_none=True,
        )
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if uuid (nullable) is None
        # and model_fields_set contains the field
        if self.uuid is None and "uuid" in self.model_fields_set:
            _dict['uuid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "sourceId":
            obj.get("sourceId"),
            "sourceName":
            obj.get("sourceName"),
            "identityId":
            obj.get("identityId"),
            "attributes":
            obj.get("attributes"),
            "authoritative":
            obj.get("authoritative"),
            "description":
            obj.get("description"),
            "disabled":
            obj.get("disabled"),
            "locked":
            obj.get("locked"),
            "nativeIdentity":
            obj.get("nativeIdentity"),
            "systemAccount":
            obj.get("systemAccount"),
            "uncorrelated":
            obj.get("uncorrelated"),
            "uuid":
            obj.get("uuid"),
            "manuallyCorrelated":
            obj.get("manuallyCorrelated"),
            "hasEntitlements":
            obj.get("hasEntitlements")
        })
        return _obj
