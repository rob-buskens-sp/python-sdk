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
from pydantic import BaseModel, Field
from sailpoint.v3.models.access_criteria import AccessCriteria


class SodPolicyConflictingAccessCriteria(BaseModel):
    """
    SodPolicyConflictingAccessCriteria
    """
    left_criteria: Optional[AccessCriteria] = Field(None, alias="leftCriteria")
    right_criteria: Optional[AccessCriteria] = Field(None,
                                                     alias="rightCriteria")
    __properties = ["leftCriteria", "rightCriteria"]

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
    def from_json(cls, json_str: str) -> SodPolicyConflictingAccessCriteria:
        """Create an instance of SodPolicyConflictingAccessCriteria from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of left_criteria
        if self.left_criteria:
            _dict['leftCriteria'] = self.left_criteria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of right_criteria
        if self.right_criteria:
            _dict['rightCriteria'] = self.right_criteria.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SodPolicyConflictingAccessCriteria:
        """Create an instance of SodPolicyConflictingAccessCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SodPolicyConflictingAccessCriteria.parse_obj(obj)

        _obj = SodPolicyConflictingAccessCriteria.parse_obj({
            "left_criteria":
            AccessCriteria.from_dict(obj.get("leftCriteria"))
            if obj.get("leftCriteria") is not None else None,
            "right_criteria":
            AccessCriteria.from_dict(obj.get("rightCriteria"))
            if obj.get("rightCriteria") is not None else None
        })
        return _obj
