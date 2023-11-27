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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from sailpoint.beta.models.owner_reference_segments import OwnerReferenceSegments
from sailpoint.beta.models.visibility_criteria import VisibilityCriteria


class Segment(BaseModel):
    """
    Segment
    """
    id: Optional[StrictStr] = Field(None, description="The segment's ID.")
    name: Optional[StrictStr] = Field(
        None, description="The segment's business name.")
    created: Optional[datetime] = Field(
        None, description="The time when the segment is created.")
    modified: Optional[datetime] = Field(
        None, description="The time when the segment is modified.")
    description: Optional[StrictStr] = Field(
        None, description="The segment's optional description.")
    owner: Optional[OwnerReferenceSegments] = None
    visibility_criteria: Optional[VisibilityCriteria] = Field(
        None, alias="visibilityCriteria")
    active: Optional[StrictBool] = Field(
        False,
        description=
        "This boolean indicates whether the segment is currently active. Inactive segments have no effect."
    )
    __properties = [
        "id", "name", "created", "modified", "description", "owner",
        "visibilityCriteria", "active"
    ]

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
    def from_json(cls, json_str: str) -> Segment:
        """Create an instance of Segment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of visibility_criteria
        if self.visibility_criteria:
            _dict['visibilityCriteria'] = self.visibility_criteria.to_dict()
        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Segment:
        """Create an instance of Segment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Segment.parse_obj(obj)

        _obj = Segment.parse_obj({
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
            "owner":
            OwnerReferenceSegments.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "visibility_criteria":
            VisibilityCriteria.from_dict(obj.get("visibilityCriteria"))
            if obj.get("visibilityCriteria") is not None else None,
            "active":
            obj.get("active") if obj.get("active") is not None else False
        })
        return _obj
