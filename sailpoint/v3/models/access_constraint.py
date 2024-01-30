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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccessConstraint(BaseModel):
    """
    AccessConstraint
    """

  # noqa: E501
    type: StrictStr = Field(description="Type of Access")
    ids: Optional[List[StrictStr]] = Field(
        default=None, description="Must be set only if operator is SELECTED.")
    operator: StrictStr = Field(
        description=
        "Used to determine whether the scope of the campaign should be reduced for selected ids or all."
    )
    __properties: ClassVar[List[str]] = ["type", "ids", "operator"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ENTITLEMENT', 'ACCESS_PROFILE', 'ROLE'):
            raise ValueError(
                "must be one of enum values ('ENTITLEMENT', 'ACCESS_PROFILE', 'ROLE')"
            )
        return value

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ALL', 'SELECTED'):
            raise ValueError("must be one of enum values ('ALL', 'SELECTED')")
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
        """Create an instance of AccessConstraint from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccessConstraint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "ids": obj.get("ids"),
            "operator": obj.get("operator")
        })
        return _obj
