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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class BasicAuthConfig(BaseModel):
    """
    Config required if BASIC_AUTH is used.  # noqa: E501
    """
    user_name: Optional[StrictStr] = Field(None, alias="userName", description="The username to authenticate.")
    password: Optional[StrictStr] = Field(None, description="The password to authenticate. On response, this field is set to null as to not return secrets.")
    __properties = ["userName", "password"]

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
    def from_json(cls, json_str: str) -> BasicAuthConfig:
        """Create an instance of BasicAuthConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if password (nullable) is None
        # and __fields_set__ contains the field
        if self.password is None and "password" in self.__fields_set__:
            _dict['password'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BasicAuthConfig:
        """Create an instance of BasicAuthConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BasicAuthConfig.parse_obj(obj)

        _obj = BasicAuthConfig.parse_obj({
            "user_name": obj.get("userName"),
            "password": obj.get("password")
        })
        return _obj


