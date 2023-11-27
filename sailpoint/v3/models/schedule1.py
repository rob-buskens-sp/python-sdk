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
from pydantic import BaseModel, Field, StrictStr
from sailpoint.v3.models.schedule1_days import Schedule1Days
from sailpoint.v3.models.schedule1_hours import Schedule1Hours
from sailpoint.v3.models.schedule_type import ScheduleType


class Schedule1(BaseModel):
    """
    The schedule information.  # noqa: E501
    """
    type: ScheduleType = Field(...)
    days: Optional[Schedule1Days] = None
    hours: Schedule1Hours = Field(...)
    expiration: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    time_zone_id: Optional[StrictStr] = Field(
        None,
        alias="timeZoneId",
        description=
        "The GMT formatted timezone the schedule will run in (ex. GMT-06:00).  If no timezone is specified, the org's default timezone is used."
    )
    __properties = ["type", "days", "hours", "expiration", "timeZoneId"]

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
    def from_json(cls, json_str: str) -> Schedule1:
        """Create an instance of Schedule1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of days
        if self.days:
            _dict['days'] = self.days.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hours
        if self.hours:
            _dict['hours'] = self.hours.to_dict()
        # set to None if expiration (nullable) is None
        # and __fields_set__ contains the field
        if self.expiration is None and "expiration" in self.__fields_set__:
            _dict['expiration'] = None

        # set to None if time_zone_id (nullable) is None
        # and __fields_set__ contains the field
        if self.time_zone_id is None and "time_zone_id" in self.__fields_set__:
            _dict['timeZoneId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Schedule1:
        """Create an instance of Schedule1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Schedule1.parse_obj(obj)

        _obj = Schedule1.parse_obj({
            "type":
            obj.get("type"),
            "days":
            Schedule1Days.from_dict(obj.get("days"))
            if obj.get("days") is not None else None,
            "hours":
            Schedule1Hours.from_dict(obj.get("hours"))
            if obj.get("hours") is not None else None,
            "expiration":
            obj.get("expiration"),
            "time_zone_id":
            obj.get("timeZoneId")
        })
        return _obj
