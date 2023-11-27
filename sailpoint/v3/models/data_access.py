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
from sailpoint.v3.models.data_access_categories_inner import DataAccessCategoriesInner
from sailpoint.v3.models.data_access_impact_score import DataAccessImpactScore
from sailpoint.v3.models.data_access_policies_inner import DataAccessPoliciesInner


class DataAccess(BaseModel):
    """
    DAS data for the entitlement  # noqa: E501
    """
    policies: Optional[conlist(DataAccessPoliciesInner)] = Field(
        None,
        description=
        "List of classification policies that apply to resources the entitlement \\ groups has access to"
    )
    categories: Optional[conlist(DataAccessCategoriesInner)] = Field(
        None,
        description=
        "List of classification categories that apply to resources the entitlement \\ groups has access to"
    )
    impact_score: Optional[DataAccessImpactScore] = Field(None,
                                                          alias="impactScore")
    __properties = ["policies", "categories", "impactScore"]

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
    def from_json(cls, json_str: str) -> DataAccess:
        """Create an instance of DataAccess from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in categories (list)
        _items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    _items.append(_item.to_dict())
            _dict['categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of impact_score
        if self.impact_score:
            _dict['impactScore'] = self.impact_score.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataAccess:
        """Create an instance of DataAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DataAccess.parse_obj(obj)

        _obj = DataAccess.parse_obj({
            "policies": [
                DataAccessPoliciesInner.from_dict(_item)
                for _item in obj.get("policies")
            ] if obj.get("policies") is not None else None,
            "categories": [
                DataAccessCategoriesInner.from_dict(_item)
                for _item in obj.get("categories")
            ] if obj.get("categories") is not None else None,
            "impact_score":
            DataAccessImpactScore.from_dict(obj.get("impactScore"))
            if obj.get("impactScore") is not None else None
        })
        return _obj
