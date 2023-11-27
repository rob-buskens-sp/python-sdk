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

from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from sailpoint.v3.models.role_criteria_level1 import RoleCriteriaLevel1
from sailpoint.v3.models.role_membership_identity import RoleMembershipIdentity
from sailpoint.v3.models.role_membership_selector_type import RoleMembershipSelectorType


class RoleMembershipSelector(BaseModel):
    """
    When present, specifies that the Role is to be granted to Identities which either satisfy specific criteria or which are members of a given list of Identities.  # noqa: E501
    """
    type: Optional[RoleMembershipSelectorType] = None
    criteria: Optional[RoleCriteriaLevel1] = None
    identities: Optional[conlist(RoleMembershipIdentity)] = Field(
        None,
        description=
        "Defines role membership as being exclusive to the specified Identities, when type is IDENTITY_LIST."
    )
    __properties = ["type", "criteria", "identities"]

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
    def from_json(cls, json_str: str) -> RoleMembershipSelector:
        """Create an instance of RoleMembershipSelector from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of criteria
        if self.criteria:
            _dict['criteria'] = self.criteria.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in identities (list)
        _items = []
        if self.identities:
            for _item in self.identities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['identities'] = _items
        # set to None if criteria (nullable) is None
        # and __fields_set__ contains the field
        if self.criteria is None and "criteria" in self.__fields_set__:
            _dict['criteria'] = None

        # set to None if identities (nullable) is None
        # and __fields_set__ contains the field
        if self.identities is None and "identities" in self.__fields_set__:
            _dict['identities'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleMembershipSelector:
        """Create an instance of RoleMembershipSelector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleMembershipSelector.parse_obj(obj)

        _obj = RoleMembershipSelector.parse_obj({
            "type":
            obj.get("type"),
            "criteria":
            RoleCriteriaLevel1.from_dict(obj.get("criteria"))
            if obj.get("criteria") is not None else None,
            "identities": [
                RoleMembershipIdentity.from_dict(_item)
                for _item in obj.get("identities")
            ] if obj.get("identities") is not None else None
        })
        return _obj
