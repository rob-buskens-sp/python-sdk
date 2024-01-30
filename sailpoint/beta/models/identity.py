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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.identity_dto_manager_ref import IdentityDtoManagerRef
from sailpoint.beta.models.lifecycle_state_dto import LifecycleStateDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Identity(BaseModel):
    """
    Identity
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(
        default=None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(description="Name of the Object")
    created: Optional[datetime] = Field(
        default=None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(
        default=None, description="Last modification date of the Object")
    alias: Optional[StrictStr] = Field(
        default=None,
        description="Alternate unique identifier for the identity")
    email_address: Optional[StrictStr] = Field(
        default=None,
        description="The email address of the identity",
        alias="emailAddress")
    processing_state: Optional[StrictStr] = Field(
        default=None,
        description="The processing state of the identity",
        alias="processingState")
    identity_status: Optional[StrictStr] = Field(
        default=None,
        description="The identity's status in the system",
        alias="identityStatus")
    manager_ref: Optional[IdentityDtoManagerRef] = Field(default=None,
                                                         alias="managerRef")
    is_manager: Optional[StrictBool] = Field(
        default=False,
        description="Whether this identity is a manager of another identity",
        alias="isManager")
    last_refresh: Optional[datetime] = Field(
        default=None,
        description="The last time the identity was refreshed by the system",
        alias="lastRefresh")
    attributes: Optional[Dict[str, Any]] = Field(
        default=None,
        description="A map with the identity attributes for the identity")
    lifecycle_state: Optional[LifecycleStateDto] = Field(
        default=None, alias="lifecycleState")
    __properties: ClassVar[List[str]] = [
        "id", "name", "created", "modified", "alias", "emailAddress",
        "processingState", "identityStatus", "managerRef", "isManager",
        "lastRefresh", "attributes", "lifecycleState"
    ]

    @field_validator('processing_state')
    def processing_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ERROR', 'OK'):
            raise ValueError("must be one of enum values ('ERROR', 'OK')")
        return value

    @field_validator('identity_status')
    def identity_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('UNREGISTERED', 'REGISTERED', 'PENDING', 'WARNING',
                         'DISABLED', 'ACTIVE', 'DEACTIVATED', 'TERMINATED',
                         'ERROR', 'LOCKED'):
            raise ValueError(
                "must be one of enum values ('UNREGISTERED', 'REGISTERED', 'PENDING', 'WARNING', 'DISABLED', 'ACTIVE', 'DEACTIVATED', 'TERMINATED', 'ERROR', 'LOCKED')"
            )
        return value

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
        """Create an instance of Identity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of manager_ref
        if self.manager_ref:
            _dict['managerRef'] = self.manager_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lifecycle_state
        if self.lifecycle_state:
            _dict['lifecycleState'] = self.lifecycle_state.to_dict()
        # set to None if processing_state (nullable) is None
        # and model_fields_set contains the field
        if self.processing_state is None and "processing_state" in self.model_fields_set:
            _dict['processingState'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Identity from a dict"""
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
            "alias":
            obj.get("alias"),
            "emailAddress":
            obj.get("emailAddress"),
            "processingState":
            obj.get("processingState"),
            "identityStatus":
            obj.get("identityStatus"),
            "managerRef":
            IdentityDtoManagerRef.from_dict(obj.get("managerRef"))
            if obj.get("managerRef") is not None else None,
            "isManager":
            obj.get("isManager")
            if obj.get("isManager") is not None else False,
            "lastRefresh":
            obj.get("lastRefresh"),
            "attributes":
            obj.get("attributes"),
            "lifecycleState":
            LifecycleStateDto.from_dict(obj.get("lifecycleState"))
            if obj.get("lifecycleState") is not None else None
        })
        return _obj
