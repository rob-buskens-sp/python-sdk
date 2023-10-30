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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from v3.models.document_type import DocumentType

class Aggregation(BaseModel):
    """
    Aggregation  # noqa: E501
    """
    id: StrictStr = Field(...)
    name: StrictStr = Field(...)
    type: DocumentType = Field(..., alias="_type")
    status: Optional[StrictStr] = None
    duration: Optional[StrictInt] = None
    avg_duration: Optional[StrictInt] = Field(None, alias="avgDuration")
    changed_accounts: Optional[StrictInt] = Field(None, alias="changedAccounts")
    next_scheduled: Optional[datetime] = Field(None, alias="nextScheduled", description="A date-time in ISO-8601 format")
    start_time: Optional[datetime] = Field(None, alias="startTime", description="A date-time in ISO-8601 format")
    source_owner: Optional[StrictStr] = Field(None, alias="sourceOwner", description="John Doe")
    __properties = ["id", "name", "_type", "status", "duration", "avgDuration", "changedAccounts", "nextScheduled", "startTime", "sourceOwner"]

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
    def from_json(cls, json_str: str) -> Aggregation:
        """Create an instance of Aggregation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if next_scheduled (nullable) is None
        # and __fields_set__ contains the field
        if self.next_scheduled is None and "next_scheduled" in self.__fields_set__:
            _dict['nextScheduled'] = None

        # set to None if start_time (nullable) is None
        # and __fields_set__ contains the field
        if self.start_time is None and "start_time" in self.__fields_set__:
            _dict['startTime'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Aggregation:
        """Create an instance of Aggregation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Aggregation.parse_obj(obj)

        _obj = Aggregation.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("_type"),
            "status": obj.get("status"),
            "duration": obj.get("duration"),
            "avg_duration": obj.get("avgDuration"),
            "changed_accounts": obj.get("changedAccounts"),
            "next_scheduled": obj.get("nextScheduled"),
            "start_time": obj.get("startTime"),
            "source_owner": obj.get("sourceOwner")
        })
        return _obj


