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
from pydantic import BaseModel, Field


class TestExternalExecuteWorkflow200Response(BaseModel):
    """
    TestExternalExecuteWorkflow200Response
    """
    payload: Optional[Dict[str, Any]] = Field(
        None, description="The input that was received")
    __properties = ["payload"]

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
    def from_json(cls,
                  json_str: str) -> TestExternalExecuteWorkflow200Response:
        """Create an instance of TestExternalExecuteWorkflow200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TestExternalExecuteWorkflow200Response:
        """Create an instance of TestExternalExecuteWorkflow200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TestExternalExecuteWorkflow200Response.parse_obj(obj)

        _obj = TestExternalExecuteWorkflow200Response.parse_obj(
            {"payload": obj.get("payload")})
        return _obj
