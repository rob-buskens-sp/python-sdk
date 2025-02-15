# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.entity_created_by_dto import EntityCreatedByDTO
from sailpoint.beta.models.role_mining_identity_distribution import RoleMiningIdentityDistribution
from sailpoint.beta.models.role_mining_potential_role_provision_state import RoleMiningPotentialRoleProvisionState
from sailpoint.beta.models.role_mining_role_type import RoleMiningRoleType
from sailpoint.beta.models.role_mining_session_parameters_dto import RoleMiningSessionParametersDto
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RoleMiningPotentialRole(BaseModel):
    """
    RoleMiningPotentialRole
    """ # noqa: E501
    created_by: Optional[EntityCreatedByDTO] = Field(default=None, alias="createdBy")
    density: Optional[StrictInt] = Field(default=None, description="The density of a potential role.")
    description: Optional[StrictStr] = Field(default=None, description="The description of a potential role.")
    entitlement_count: Optional[StrictInt] = Field(default=None, description="The number of entitlements in a potential role.", alias="entitlementCount")
    excluded_entitlements: Optional[List[StrictStr]] = Field(default=None, description="The list of entitlement ids to be excluded.", alias="excludedEntitlements")
    freshness: Optional[StrictInt] = Field(default=None, description="The freshness of a potential role.")
    identity_count: Optional[StrictInt] = Field(default=None, description="The number of identities in a potential role.", alias="identityCount")
    identity_distribution: Optional[List[RoleMiningIdentityDistribution]] = Field(default=None, description="Identity attribute distribution.", alias="identityDistribution")
    identity_ids: Optional[List[StrictStr]] = Field(default=None, description="The list of ids in a potential role.", alias="identityIds")
    name: Optional[StrictStr] = Field(default=None, description="Name of the potential role.")
    provision_state: Optional[RoleMiningPotentialRoleProvisionState] = Field(default=None, alias="provisionState")
    quality: Optional[StrictInt] = Field(default=None, description="The quality of a potential role.")
    role_id: Optional[StrictStr] = Field(default=None, description="The roleId of a potential role.", alias="roleId")
    saved: Optional[StrictBool] = Field(default=None, description="The potential role's saved status.")
    session: Optional[RoleMiningSessionParametersDto] = None
    type: Optional[RoleMiningRoleType] = None
    __properties: ClassVar[List[str]] = ["createdBy", "density", "description", "entitlementCount", "excludedEntitlements", "freshness", "identityCount", "identityDistribution", "identityIds", "name", "provisionState", "quality", "roleId", "saved", "session", "type"]

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
        """Create an instance of RoleMiningPotentialRole from a JSON string"""
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
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identity_distribution (list)
        _items = []
        if self.identity_distribution:
            for _item in self.identity_distribution:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identityDistribution'] = _items
        # override the default output from pydantic by calling `to_dict()` of session
        if self.session:
            _dict['session'] = self.session.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoleMiningPotentialRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdBy": EntityCreatedByDTO.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "density": obj.get("density"),
            "description": obj.get("description"),
            "entitlementCount": obj.get("entitlementCount"),
            "excludedEntitlements": obj.get("excludedEntitlements"),
            "freshness": obj.get("freshness"),
            "identityCount": obj.get("identityCount"),
            "identityDistribution": [RoleMiningIdentityDistribution.from_dict(_item) for _item in obj.get("identityDistribution")] if obj.get("identityDistribution") is not None else None,
            "identityIds": obj.get("identityIds"),
            "name": obj.get("name"),
            "provisionState": obj.get("provisionState"),
            "quality": obj.get("quality"),
            "roleId": obj.get("roleId"),
            "saved": obj.get("saved"),
            "session": RoleMiningSessionParametersDto.from_dict(obj.get("session")) if obj.get("session") is not None else None,
            "type": obj.get("type")
        })
        return _obj


