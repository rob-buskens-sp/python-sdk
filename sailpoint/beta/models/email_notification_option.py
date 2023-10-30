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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class EmailNotificationOption(BaseModel):
    """
    EmailNotificationOption
    """
    notify_managers: Optional[StrictBool] = Field(None, alias="notifyManagers", description="If true, then the manager is notified of the lifecycle state change.")
    notify_all_admins: Optional[StrictBool] = Field(None, alias="notifyAllAdmins", description="If true, then all the admins are notified of the lifecycle state change.")
    notify_specific_users: Optional[StrictBool] = Field(None, alias="notifySpecificUsers", description="If true, then the users specified in \"emailAddressList\" below are notified of lifecycle state change.")
    email_address_list: Optional[conlist(StrictStr)] = Field(None, alias="emailAddressList", description="List of user email addresses. If \"notifySpecificUsers\" option is true, then these users are notified of lifecycle state change.")
    __properties = ["notifyManagers", "notifyAllAdmins", "notifySpecificUsers", "emailAddressList"]

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
    def from_json(cls, json_str: str) -> EmailNotificationOption:
        """Create an instance of EmailNotificationOption from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EmailNotificationOption:
        """Create an instance of EmailNotificationOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EmailNotificationOption.parse_obj(obj)

        _obj = EmailNotificationOption.parse_obj({
            "notify_managers": obj.get("notifyManagers"),
            "notify_all_admins": obj.get("notifyAllAdmins"),
            "notify_specific_users": obj.get("notifySpecificUsers"),
            "email_address_list": obj.get("emailAddressList")
        })
        return _obj


