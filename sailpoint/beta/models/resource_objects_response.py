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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from beta.models.resource_object import ResourceObject

class ResourceObjectsResponse(BaseModel):
    """
    Response model for peek resource objects from source connectors.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="ID of the source")
    name: Optional[StrictStr] = Field(None, description="Name of the source")
    object_count: Optional[StrictInt] = Field(None, alias="objectCount", description="The number of objects that were fetched by the connector.")
    elapsed_millis: Optional[StrictInt] = Field(None, alias="elapsedMillis", description="The number of milliseconds spent on the entire request.")
    resource_objects: Optional[conlist(ResourceObject)] = Field(None, alias="resourceObjects", description="Fetched objects from the source connector.")
    __properties = ["id", "name", "objectCount", "elapsedMillis", "resourceObjects"]

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
    def from_json(cls, json_str: str) -> ResourceObjectsResponse:
        """Create an instance of ResourceObjectsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "name",
                            "object_count",
                            "elapsed_millis",
                            "resource_objects",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in resource_objects (list)
        _items = []
        if self.resource_objects:
            for _item in self.resource_objects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceObjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceObjectsResponse:
        """Create an instance of ResourceObjectsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceObjectsResponse.parse_obj(obj)

        _obj = ResourceObjectsResponse.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "object_count": obj.get("objectCount"),
            "elapsed_millis": obj.get("elapsedMillis"),
            "resource_objects": [ResourceObject.from_dict(_item) for _item in obj.get("resourceObjects")] if obj.get("resourceObjects") is not None else None
        })
        return _obj


