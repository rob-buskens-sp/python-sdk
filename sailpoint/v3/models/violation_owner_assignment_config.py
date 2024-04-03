# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from sailpoint.v3.models.violation_owner_assignment_config_owner_ref import ViolationOwnerAssignmentConfigOwnerRef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ViolationOwnerAssignmentConfig(BaseModel):
    """
    ViolationOwnerAssignmentConfig
    """ # noqa: E501
    assignment_rule: Optional[StrictStr] = Field(default=None, description="Details about the violations owner. MANAGER - identity's manager STATIC - Governance Group or Identity", alias="assignmentRule")
    owner_ref: Optional[ViolationOwnerAssignmentConfigOwnerRef] = Field(default=None, alias="ownerRef")
    __properties: ClassVar[List[str]] = ["assignmentRule", "ownerRef"]

    @field_validator('assignment_rule')
    def assignment_rule_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('MANAGER', 'STATIC', 'null'):
            raise ValueError("must be one of enum values ('MANAGER', 'STATIC', 'null')")
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
        """Create an instance of ViolationOwnerAssignmentConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner_ref
        if self.owner_ref:
            _dict['ownerRef'] = self.owner_ref.to_dict()
        # set to None if assignment_rule (nullable) is None
        # and model_fields_set contains the field
        if self.assignment_rule is None and "assignment_rule" in self.model_fields_set:
            _dict['assignmentRule'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ViolationOwnerAssignmentConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assignmentRule": obj.get("assignmentRule"),
            "ownerRef": ViolationOwnerAssignmentConfigOwnerRef.from_dict(obj.get("ownerRef")) if obj.get("ownerRef") is not None else None
        })
        return _obj


