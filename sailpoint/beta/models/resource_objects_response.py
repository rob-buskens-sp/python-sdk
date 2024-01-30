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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.resource_object import ResourceObject
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ResourceObjectsResponse(BaseModel):
    """
    Response model for peek resource objects from source connectors.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="ID of the source")
    name: Optional[StrictStr] = Field(default=None,
                                      description="Name of the source")
    object_count: Optional[StrictInt] = Field(
        default=None,
        description="The number of objects that were fetched by the connector.",
        alias="objectCount")
    elapsed_millis: Optional[StrictInt] = Field(
        default=None,
        description="The number of milliseconds spent on the entire request.",
        alias="elapsedMillis")
    resource_objects: Optional[List[ResourceObject]] = Field(
        default=None,
        description="Fetched objects from the source connector.",
        alias="resourceObjects")
    __properties: ClassVar[List[str]] = [
        "id", "name", "objectCount", "elapsedMillis", "resourceObjects"
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
        """Create an instance of ResourceObjectsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "name",
                "object_count",
                "elapsed_millis",
                "resource_objects",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in resource_objects (list)
        _items = []
        if self.resource_objects:
            for _item in self.resource_objects:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceObjects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ResourceObjectsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "objectCount":
            obj.get("objectCount"),
            "elapsedMillis":
            obj.get("elapsedMillis"),
            "resourceObjects": [
                ResourceObject.from_dict(_item)
                for _item in obj.get("resourceObjects")
            ] if obj.get("resourceObjects") is not None else None
        })
        return _obj
