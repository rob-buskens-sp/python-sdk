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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from sailpoint.v3.models.document_type import DocumentType
from sailpoint.v3.models.owner import Owner
from sailpoint.v3.models.reference import Reference


class RoleDocument(BaseModel):
    """
    Role  # noqa: E501
    """
    id: StrictStr = Field(
        ..., description="The unique ID of the referenced object.")
    name: StrictStr = Field(
        ..., description="The human readable name of the referenced object.")
    type: DocumentType = Field(..., alias="_type")
    description: Optional[StrictStr] = Field(
        None, description="The description of the access item")
    created: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    modified: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    synced: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    enabled: Optional[StrictBool] = None
    requestable: Optional[StrictBool] = Field(
        None, description="Indicates if the access can be requested")
    request_comments_required: Optional[StrictBool] = Field(
        None,
        alias="requestCommentsRequired",
        description="Indicates if comments are required when requesting access"
    )
    owner: Optional[Owner] = None
    access_profiles: Optional[conlist(Reference)] = Field(
        None, alias="accessProfiles")
    access_profile_count: Optional[StrictInt] = Field(
        None, alias="accessProfileCount")
    tags: Optional[conlist(StrictStr)] = None
    __properties = [
        "id", "name", "_type", "description", "created", "modified", "synced",
        "enabled", "requestable", "requestCommentsRequired", "owner",
        "accessProfiles", "accessProfileCount", "tags"
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
    def from_json(cls, json_str: str) -> RoleDocument:
        """Create an instance of RoleDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in access_profiles (list)
        _items = []
        if self.access_profiles:
            for _item in self.access_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessProfiles'] = _items
        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if modified (nullable) is None
        # and __fields_set__ contains the field
        if self.modified is None and "modified" in self.__fields_set__:
            _dict['modified'] = None

        # set to None if synced (nullable) is None
        # and __fields_set__ contains the field
        if self.synced is None and "synced" in self.__fields_set__:
            _dict['synced'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleDocument:
        """Create an instance of RoleDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleDocument.parse_obj(obj)

        _obj = RoleDocument.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "type":
            obj.get("_type"),
            "description":
            obj.get("description"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "synced":
            obj.get("synced"),
            "enabled":
            obj.get("enabled"),
            "requestable":
            obj.get("requestable"),
            "request_comments_required":
            obj.get("requestCommentsRequired"),
            "owner":
            Owner.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "access_profiles": [
                Reference.from_dict(_item)
                for _item in obj.get("accessProfiles")
            ] if obj.get("accessProfiles") is not None else None,
            "access_profile_count":
            obj.get("accessProfileCount"),
            "tags":
            obj.get("tags")
        })
        return _obj
