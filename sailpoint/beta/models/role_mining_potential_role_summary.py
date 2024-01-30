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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.role_mining_potential_role_provision_state import RoleMiningPotentialRoleProvisionState
from sailpoint.beta.models.role_mining_potential_role_ref import RoleMiningPotentialRoleRef
from sailpoint.beta.models.role_mining_role_type import RoleMiningRoleType
from sailpoint.beta.models.role_mining_session_parameters_dto import RoleMiningSessionParametersDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RoleMiningPotentialRoleSummary(BaseModel):
    """
    RoleMiningPotentialRoleSummary
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="Id of the potential role")
    name: Optional[StrictStr] = Field(default=None,
                                      description="Name of the potential role")
    potential_role_ref: Optional[RoleMiningPotentialRoleRef] = Field(
        default=None, alias="potentialRoleRef")
    identity_count: Optional[StrictInt] = Field(
        default=None,
        description="The number of identities in a potential role.",
        alias="identityCount")
    entitlement_count: Optional[StrictInt] = Field(
        default=None,
        description="The number of entitlements in a potential role.",
        alias="entitlementCount")
    identity_group_status: Optional[StrictStr] = Field(
        default=None,
        description=
        "The status for this identity group which can be \"REQUESTED\" or \"OBTAINED\"",
        alias="identityGroupStatus")
    provision_state: Optional[RoleMiningPotentialRoleProvisionState] = Field(
        default=None, alias="provisionState")
    role_id: Optional[StrictStr] = Field(
        default=None,
        description=
        "ID of the provisioned role in IIQ or IDN.  Null if this potential role has not been provisioned.",
        alias="roleId")
    density: Optional[StrictInt] = Field(
        default=None,
        description=
        "The density metric (0-100) of this potential role. Higher density values indicate higher similarity amongst the identities."
    )
    freshness: Optional[StrictInt] = Field(
        default=None,
        description=
        "The freshness metric (0-100) of this potential role. Higher freshness values indicate this potential role is more distinctive compared to existing roles."
    )
    quality: Optional[StrictInt] = Field(
        default=None,
        description=
        "The quality metric (0-100) of this potential role. Higher quality values indicate this potential role has high density and freshness."
    )
    type: Optional[RoleMiningRoleType] = None
    session: Optional[RoleMiningSessionParametersDto] = None
    __properties: ClassVar[List[str]] = [
        "id", "name", "potentialRoleRef", "identityCount", "entitlementCount",
        "identityGroupStatus", "provisionState", "roleId", "density",
        "freshness", "quality", "type", "session"
    ]

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
        """Create an instance of RoleMiningPotentialRoleSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of potential_role_ref
        if self.potential_role_ref:
            _dict['potentialRoleRef'] = self.potential_role_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        # set to None if role_id (nullable) is None
        # and model_fields_set contains the field
        if self.role_id is None and "role_id" in self.model_fields_set:
            _dict['roleId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoleMiningPotentialRoleSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "potentialRoleRef":
            RoleMiningPotentialRoleRef.from_dict(obj.get("potentialRoleRef"))
            if obj.get("potentialRoleRef") is not None else None,
            "identityCount":
            obj.get("identityCount"),
            "entitlementCount":
            obj.get("entitlementCount"),
            "identityGroupStatus":
            obj.get("identityGroupStatus"),
            "provisionState":
            obj.get("provisionState"),
            "roleId":
            obj.get("roleId"),
            "density":
            obj.get("density"),
            "freshness":
            obj.get("freshness"),
            "quality":
            obj.get("quality"),
            "type":
            obj.get("type"),
            "session":
            RoleMiningSessionParametersDto.from_dict(obj.get("session"))
            if obj.get("session") is not None else None
        })
        return _obj
