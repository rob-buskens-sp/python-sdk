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

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator


class StatusResponse(BaseModel):
    """
    Response model for connection check, configuration test and ping of source connectors.  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="ID of the source")
    name: Optional[StrictStr] = Field(None, description="Name of the source")
    status: Optional[StrictStr] = Field(
        None, description="The status of the health check.")
    elapsed_millis: Optional[StrictInt] = Field(
        None,
        alias="elapsedMillis",
        description="The number of milliseconds spent on the entire request.")
    details: Optional[Dict[str, Any]] = Field(
        None,
        description=
        "The document contains the results of the health check. The schema of this document depends on the type of source used. "
    )
    __properties = ["id", "name", "status", "elapsedMillis", "details"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'FAILURE'):
            raise ValueError(
                "must be one of enum values ('SUCCESS', 'FAILURE')")
        return value

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
    def from_json(cls, json_str: str) -> StatusResponse:
        """Create an instance of StatusResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "id",
                              "name",
                              "status",
                              "elapsed_millis",
                              "details",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatusResponse:
        """Create an instance of StatusResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatusResponse.parse_obj(obj)

        _obj = StatusResponse.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "status":
            obj.get("status"),
            "elapsed_millis":
            obj.get("elapsedMillis"),
            "details":
            obj.get("details")
        })
        return _obj
