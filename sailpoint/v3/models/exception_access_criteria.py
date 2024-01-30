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
from sailpoint.v3.models.exception_criteria import ExceptionCriteria
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ExceptionAccessCriteria(BaseModel):
    """
    ExceptionAccessCriteria
    """

  # noqa: E501
    left_criteria: Optional[ExceptionCriteria] = Field(default=None,
                                                       alias="leftCriteria")
    right_criteria: Optional[ExceptionCriteria] = Field(default=None,
                                                        alias="rightCriteria")
    __properties: ClassVar[List[str]] = ["leftCriteria", "rightCriteria"]

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
        """Create an instance of ExceptionAccessCriteria from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of left_criteria
        if self.left_criteria:
            _dict['leftCriteria'] = self.left_criteria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of right_criteria
        if self.right_criteria:
            _dict['rightCriteria'] = self.right_criteria.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExceptionAccessCriteria from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "leftCriteria":
            ExceptionCriteria.from_dict(obj.get("leftCriteria"))
            if obj.get("leftCriteria") is not None else None,
            "rightCriteria":
            ExceptionCriteria.from_dict(obj.get("rightCriteria"))
            if obj.get("rightCriteria") is not None else None
        })
        return _obj
