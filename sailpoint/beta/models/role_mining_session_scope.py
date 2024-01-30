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
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class RoleMiningSessionScope(BaseModel):
    """
    RoleMiningSessionScope
    """

  # noqa: E501
    identity_ids: Optional[List[StrictStr]] = Field(
        default=None,
        description="The list of identities for this role mining session.",
        alias="identityIds")
    criteria: Optional[StrictStr] = Field(
        default=None,
        description=
        "The \"search\" criteria that produces the list of identities for this role mining session."
    )
    attribute_filter_criteria: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="The filter criteria for this role mining session.",
        alias="attributeFilterCriteria")
    __properties: ClassVar[List[str]] = [
        "identityIds", "criteria", "attributeFilterCriteria"
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
        """Create an instance of RoleMiningSessionScope from a JSON string"""
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
        # set to None if criteria (nullable) is None
        # and model_fields_set contains the field
        if self.criteria is None and "criteria" in self.model_fields_set:
            _dict['criteria'] = None

        # set to None if attribute_filter_criteria (nullable) is None
        # and model_fields_set contains the field
        if self.attribute_filter_criteria is None and "attribute_filter_criteria" in self.model_fields_set:
            _dict['attributeFilterCriteria'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RoleMiningSessionScope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identityIds":
            obj.get("identityIds"),
            "criteria":
            obj.get("criteria"),
            "attributeFilterCriteria":
            obj.get("attributeFilterCriteria")
        })
        return _obj
