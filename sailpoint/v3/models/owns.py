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
from pydantic import BaseModel, StrictBool
from pydantic import Field
from sailpoint.v3.models.reference1 import Reference1
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Owns(BaseModel):
    """
    Owns
    """ # noqa: E501
    sources: Optional[List[Reference1]] = None
    entitlements: Optional[List[Reference1]] = None
    access_profiles: Optional[List[Reference1]] = Field(default=None, alias="accessProfiles")
    roles: Optional[List[Reference1]] = None
    apps: Optional[List[Reference1]] = None
    governance_groups: Optional[List[Reference1]] = Field(default=None, alias="governanceGroups")
    fallback_approver: Optional[StrictBool] = Field(default=None, alias="fallbackApprover")
    __properties: ClassVar[List[str]] = ["sources", "entitlements", "accessProfiles", "roles", "apps", "governanceGroups", "fallbackApprover"]

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
        """Create an instance of Owns from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in entitlements (list)
        _items = []
        if self.entitlements:
            for _item in self.entitlements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entitlements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in access_profiles (list)
        _items = []
        if self.access_profiles:
            for _item in self.access_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in roles (list)
        _items = []
        if self.roles:
            for _item in self.roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in apps (list)
        _items = []
        if self.apps:
            for _item in self.apps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['apps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in governance_groups (list)
        _items = []
        if self.governance_groups:
            for _item in self.governance_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['governanceGroups'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Owns from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sources": [Reference1.from_dict(_item) for _item in obj.get("sources")] if obj.get("sources") is not None else None,
            "entitlements": [Reference1.from_dict(_item) for _item in obj.get("entitlements")] if obj.get("entitlements") is not None else None,
            "accessProfiles": [Reference1.from_dict(_item) for _item in obj.get("accessProfiles")] if obj.get("accessProfiles") is not None else None,
            "roles": [Reference1.from_dict(_item) for _item in obj.get("roles")] if obj.get("roles") is not None else None,
            "apps": [Reference1.from_dict(_item) for _item in obj.get("apps")] if obj.get("apps") is not None else None,
            "governanceGroups": [Reference1.from_dict(_item) for _item in obj.get("governanceGroups")] if obj.get("governanceGroups") is not None else None,
            "fallbackApprover": obj.get("fallbackApprover")
        })
        return _obj


