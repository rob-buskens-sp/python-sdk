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
from pydantic import BaseModel, Field, StrictStr, validator
from v3.models.violation_owner_assignment_config_owner_ref import ViolationOwnerAssignmentConfigOwnerRef

class ViolationOwnerAssignmentConfig(BaseModel):
    """
    ViolationOwnerAssignmentConfig
    """
    assignment_rule: Optional[StrictStr] = Field(None, alias="assignmentRule", description="Details about the violations owner. MANAGER - identity's manager STATIC - Governance Group or Identity")
    owner_ref: Optional[ViolationOwnerAssignmentConfigOwnerRef] = Field(None, alias="ownerRef")
    __properties = ["assignmentRule", "ownerRef"]

    @validator('assignment_rule')
    def assignment_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MANAGER', 'STATIC', 'null'):
            raise ValueError("must be one of enum values ('MANAGER', 'STATIC', 'null')")
        return value

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
    def from_json(cls, json_str: str) -> ViolationOwnerAssignmentConfig:
        """Create an instance of ViolationOwnerAssignmentConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner_ref
        if self.owner_ref:
            _dict['ownerRef'] = self.owner_ref.to_dict()
        # set to None if assignment_rule (nullable) is None
        # and __fields_set__ contains the field
        if self.assignment_rule is None and "assignment_rule" in self.__fields_set__:
            _dict['assignmentRule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ViolationOwnerAssignmentConfig:
        """Create an instance of ViolationOwnerAssignmentConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ViolationOwnerAssignmentConfig.parse_obj(obj)

        _obj = ViolationOwnerAssignmentConfig.parse_obj({
            "assignment_rule": obj.get("assignmentRule"),
            "owner_ref": ViolationOwnerAssignmentConfigOwnerRef.from_dict(obj.get("ownerRef")) if obj.get("ownerRef") is not None else None
        })
        return _obj


