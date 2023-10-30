# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class ListApplications200ResponseInnerAppProfilesInner(BaseModel):
    """
    ListApplications200ResponseInnerAppProfilesInner
    """
    id: Optional[Union[StrictFloat, StrictInt]] = None
    filename: Optional[StrictStr] = None
    created_by: Optional[StrictStr] = Field(None, alias="createdBy")
    date_created: Optional[StrictStr] = Field(None, alias="dateCreated")
    xsd_version: Optional[StrictStr] = Field(None, alias="xsdVersion")
    __properties = ["id", "filename", "createdBy", "dateCreated", "xsdVersion"]

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
    def from_json(cls, json_str: str) -> ListApplications200ResponseInnerAppProfilesInner:
        """Create an instance of ListApplications200ResponseInnerAppProfilesInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListApplications200ResponseInnerAppProfilesInner:
        """Create an instance of ListApplications200ResponseInnerAppProfilesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListApplications200ResponseInnerAppProfilesInner.parse_obj(obj)

        _obj = ListApplications200ResponseInnerAppProfilesInner.parse_obj({
            "id": obj.get("id"),
            "filename": obj.get("filename"),
            "created_by": obj.get("createdBy"),
            "date_created": obj.get("dateCreated"),
            "xsd_version": obj.get("xsdVersion")
        })
        return _obj


