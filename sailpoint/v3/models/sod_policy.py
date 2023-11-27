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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from sailpoint.v3.models.owner_dto import OwnerDto
from sailpoint.v3.models.sod_policy_conflicting_access_criteria import SodPolicyConflictingAccessCriteria
from sailpoint.v3.models.violation_owner_assignment_config import ViolationOwnerAssignmentConfig


class SodPolicy(BaseModel):
    """
    SodPolicy
    """
    id: Optional[StrictStr] = Field(None, description="Policy id")
    name: Optional[StrictStr] = Field(None, description="Policy Business Name")
    created: Optional[datetime] = Field(
        None, description="The time when this SOD policy is created.")
    modified: Optional[datetime] = Field(
        None, description="The time when this SOD policy is modified.")
    description: Optional[StrictStr] = Field(
        None, description="Optional description of the SOD policy")
    owner_ref: Optional[OwnerDto] = Field(None, alias="ownerRef")
    external_policy_reference: Optional[StrictStr] = Field(
        None,
        alias="externalPolicyReference",
        description="Optional External Policy Reference")
    policy_query: Optional[StrictStr] = Field(
        None,
        alias="policyQuery",
        description="Search query of the SOD policy")
    compensating_controls: Optional[StrictStr] = Field(
        None,
        alias="compensatingControls",
        description="Optional compensating controls(Mitigating Controls)")
    correction_advice: Optional[StrictStr] = Field(
        None,
        alias="correctionAdvice",
        description="Optional correction advice")
    state: Optional[StrictStr] = Field(
        None, description="whether the policy is enforced or not")
    tags: Optional[conlist(StrictStr)] = Field(
        None, description="tags for this policy object")
    creator_id: Optional[StrictStr] = Field(None,
                                            alias="creatorId",
                                            description="Policy's creator ID")
    modifier_id: Optional[StrictStr] = Field(
        None, alias="modifierId", description="Policy's modifier ID")
    violation_owner_assignment_config: Optional[
        ViolationOwnerAssignmentConfig] = Field(
            None, alias="violationOwnerAssignmentConfig")
    scheduled: Optional[StrictBool] = Field(
        False,
        description="defines whether a policy has been scheduled or not")
    type: Optional[StrictStr] = Field(
        'GENERAL',
        description=
        "whether a policy is query based or conflicting access based")
    conflicting_access_criteria: Optional[
        SodPolicyConflictingAccessCriteria] = Field(
            None, alias="conflictingAccessCriteria")
    __properties = [
        "id", "name", "created", "modified", "description", "ownerRef",
        "externalPolicyReference", "policyQuery", "compensatingControls",
        "correctionAdvice", "state", "tags", "creatorId", "modifierId",
        "violationOwnerAssignmentConfig", "scheduled", "type",
        "conflictingAccessCriteria"
    ]

    @validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ENFORCED', 'NOT_ENFORCED'):
            raise ValueError(
                "must be one of enum values ('ENFORCED', 'NOT_ENFORCED')")
        return value

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('GENERAL', 'CONFLICTING_ACCESS_BASED'):
            raise ValueError(
                "must be one of enum values ('GENERAL', 'CONFLICTING_ACCESS_BASED')"
            )
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
    def from_json(cls, json_str: str) -> SodPolicy:
        """Create an instance of SodPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "id",
                              "created",
                              "modified",
                              "creator_id",
                              "modifier_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner_ref
        if self.owner_ref:
            _dict['ownerRef'] = self.owner_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of violation_owner_assignment_config
        if self.violation_owner_assignment_config:
            _dict[
                'violationOwnerAssignmentConfig'] = self.violation_owner_assignment_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of conflicting_access_criteria
        if self.conflicting_access_criteria:
            _dict[
                'conflictingAccessCriteria'] = self.conflicting_access_criteria.to_dict(
                )
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if external_policy_reference (nullable) is None
        # and __fields_set__ contains the field
        if self.external_policy_reference is None and "external_policy_reference" in self.__fields_set__:
            _dict['externalPolicyReference'] = None

        # set to None if compensating_controls (nullable) is None
        # and __fields_set__ contains the field
        if self.compensating_controls is None and "compensating_controls" in self.__fields_set__:
            _dict['compensatingControls'] = None

        # set to None if correction_advice (nullable) is None
        # and __fields_set__ contains the field
        if self.correction_advice is None and "correction_advice" in self.__fields_set__:
            _dict['correctionAdvice'] = None

        # set to None if modifier_id (nullable) is None
        # and __fields_set__ contains the field
        if self.modifier_id is None and "modifier_id" in self.__fields_set__:
            _dict['modifierId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SodPolicy:
        """Create an instance of SodPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SodPolicy.parse_obj(obj)

        _obj = SodPolicy.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "description":
            obj.get("description"),
            "owner_ref":
            OwnerDto.from_dict(obj.get("ownerRef"))
            if obj.get("ownerRef") is not None else None,
            "external_policy_reference":
            obj.get("externalPolicyReference"),
            "policy_query":
            obj.get("policyQuery"),
            "compensating_controls":
            obj.get("compensatingControls"),
            "correction_advice":
            obj.get("correctionAdvice"),
            "state":
            obj.get("state"),
            "tags":
            obj.get("tags"),
            "creator_id":
            obj.get("creatorId"),
            "modifier_id":
            obj.get("modifierId"),
            "violation_owner_assignment_config":
            ViolationOwnerAssignmentConfig.from_dict(
                obj.get("violationOwnerAssignmentConfig"))
            if obj.get("violationOwnerAssignmentConfig") is not None else None,
            "scheduled":
            obj.get("scheduled")
            if obj.get("scheduled") is not None else False,
            "type":
            obj.get("type") if obj.get("type") is not None else 'GENERAL',
            "conflicting_access_criteria":
            SodPolicyConflictingAccessCriteria.from_dict(
                obj.get("conflictingAccessCriteria"))
            if obj.get("conflictingAccessCriteria") is not None else None
        })
        return _obj
