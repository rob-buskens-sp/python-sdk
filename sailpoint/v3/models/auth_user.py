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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class AuthUser(BaseModel):
    """
    AuthUser
    """
    tenant: Optional[StrictStr] = Field(None, description="Tenant name.")
    id: Optional[StrictStr] = Field(None, description="Identity ID.")
    uid: Optional[StrictStr] = Field(None, description="Identity unique identitifier.")
    profile: Optional[StrictStr] = Field(None, description="ID of the auth profile associated with this auth user.")
    identification_number: Optional[StrictStr] = Field(None, alias="identificationNumber", description="Auth user employee number.")
    email: Optional[StrictStr] = Field(None, description="Auth user's email.")
    phone: Optional[StrictStr] = Field(None, description="Auth user's phone number.")
    work_phone: Optional[StrictStr] = Field(None, alias="workPhone", description="Auth user's work phone number.")
    personal_email: Optional[StrictStr] = Field(None, alias="personalEmail", description="Auth user's personal email.")
    firstname: Optional[StrictStr] = Field(None, description="Auth user's first name.")
    lastname: Optional[StrictStr] = Field(None, description="Auth user's last name.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="Auth user's name in displayed format.")
    alias: Optional[StrictStr] = Field(None, description="Auth user's alias.")
    last_password_change_date: Optional[StrictStr] = Field(None, alias="lastPasswordChangeDate", description="the date of last password change")
    last_login_timestamp: Optional[StrictInt] = Field(None, alias="lastLoginTimestamp", description="Timestamp of the last login (long type value).")
    current_login_timestamp: Optional[StrictInt] = Field(None, alias="currentLoginTimestamp", description="Timestamp of the current login (long type value).")
    capabilities: Optional[conlist(StrictStr)] = Field(None, description="Array of capabilities for this auth user.")
    __properties = ["tenant", "id", "uid", "profile", "identificationNumber", "email", "phone", "workPhone", "personalEmail", "firstname", "lastname", "displayName", "alias", "lastPasswordChangeDate", "lastLoginTimestamp", "currentLoginTimestamp", "capabilities"]

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
    def from_json(cls, json_str: str) -> AuthUser:
        """Create an instance of AuthUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthUser:
        """Create an instance of AuthUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthUser.parse_obj(obj)

        _obj = AuthUser.parse_obj({
            "tenant": obj.get("tenant"),
            "id": obj.get("id"),
            "uid": obj.get("uid"),
            "profile": obj.get("profile"),
            "identification_number": obj.get("identificationNumber"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "work_phone": obj.get("workPhone"),
            "personal_email": obj.get("personalEmail"),
            "firstname": obj.get("firstname"),
            "lastname": obj.get("lastname"),
            "display_name": obj.get("displayName"),
            "alias": obj.get("alias"),
            "last_password_change_date": obj.get("lastPasswordChangeDate"),
            "last_login_timestamp": obj.get("lastLoginTimestamp"),
            "current_login_timestamp": obj.get("currentLoginTimestamp"),
            "capabilities": obj.get("capabilities")
        })
        return _obj


