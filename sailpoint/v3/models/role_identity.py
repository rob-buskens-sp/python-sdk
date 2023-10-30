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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from v3.models.role_assignment_source_type import RoleAssignmentSourceType

class RoleIdentity(BaseModel):
    """
    A subset of the fields of an Identity which is a member of a Role.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="The ID of the Identity")
    alias_name: Optional[StrictStr] = Field(None, alias="aliasName", description="The alias / username of the Identity")
    name: Optional[StrictStr] = Field(None, description="The human-readable display name of the Identity")
    email: Optional[StrictStr] = Field(None, description="Email address of the Identity")
    role_assignment_source: Optional[RoleAssignmentSourceType] = Field(None, alias="roleAssignmentSource")
    __properties = ["id", "aliasName", "name", "email", "roleAssignmentSource"]

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
    def from_json(cls, json_str: str) -> RoleIdentity:
        """Create an instance of RoleIdentity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleIdentity:
        """Create an instance of RoleIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleIdentity.parse_obj(obj)

        _obj = RoleIdentity.parse_obj({
            "id": obj.get("id"),
            "alias_name": obj.get("aliasName"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "role_assignment_source": obj.get("roleAssignmentSource")
        })
        return _obj


