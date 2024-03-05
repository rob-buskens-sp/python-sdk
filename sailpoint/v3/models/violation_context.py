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
from pydantic import BaseModel
from pydantic import Field
from sailpoint.v3.models.exception_access_criteria import ExceptionAccessCriteria
from sailpoint.v3.models.violation_context_policy import ViolationContextPolicy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ViolationContext(BaseModel):
    """
    ViolationContext
    """ # noqa: E501
    policy: Optional[ViolationContextPolicy] = None
    conflicting_access_criteria: Optional[ExceptionAccessCriteria] = Field(default=None, alias="conflictingAccessCriteria")
    __properties: ClassVar[List[str]] = ["policy", "conflictingAccessCriteria"]

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
        """Create an instance of ViolationContext from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of policy
        if self.policy:
            _dict['policy'] = self.policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of conflicting_access_criteria
        if self.conflicting_access_criteria:
            _dict['conflictingAccessCriteria'] = self.conflicting_access_criteria.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ViolationContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "policy": ViolationContextPolicy.from_dict(obj.get("policy")) if obj.get("policy") is not None else None,
            "conflictingAccessCriteria": ExceptionAccessCriteria.from_dict(obj.get("conflictingAccessCriteria")) if obj.get("conflictingAccessCriteria") is not None else None
        })
        return _obj


