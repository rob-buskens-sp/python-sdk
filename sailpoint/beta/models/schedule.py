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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from sailpoint.beta.models.schedule_days import ScheduleDays
from sailpoint.beta.models.schedule_hours import ScheduleHours
from sailpoint.beta.models.schedule_months import ScheduleMonths


class Schedule(BaseModel):
    """
    Schedule
    """
    type: StrictStr = Field(
        ...,
        description=
        "Determines the overall schedule cadence. In general, all time period fields smaller than the chosen type can be configured. For example, a DAILY schedule can have 'hours' set, but not 'days'; a WEEKLY schedule can have both 'hours' and 'days' set."
    )
    months: Optional[ScheduleMonths] = None
    days: Optional[ScheduleDays] = None
    hours: ScheduleHours = Field(...)
    expiration: Optional[datetime] = Field(
        None,
        description=
        "Specifies the time after which this schedule will no longer occur.")
    time_zone_id: Optional[StrictStr] = Field(
        None,
        alias="timeZoneId",
        description=
        "The time zone to use when running the schedule. For instance, if the schedule is scheduled to run at 1AM, and this field is set to \"CST\", the schedule will run at 1AM CST."
    )
    __properties = [
        "type", "months", "days", "hours", "expiration", "timeZoneId"
    ]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('WEEKLY', 'MONTHLY', 'ANNUALLY', 'CALENDAR'):
            raise ValueError(
                "must be one of enum values ('WEEKLY', 'MONTHLY', 'ANNUALLY', 'CALENDAR')"
            )
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
    def from_json(cls, json_str: str) -> Schedule:
        """Create an instance of Schedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of months
        if self.months:
            _dict['months'] = self.months.to_dict()
        # override the default output from pydantic by calling `to_dict()` of days
        if self.days:
            _dict['days'] = self.days.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hours
        if self.hours:
            _dict['hours'] = self.hours.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Schedule:
        """Create an instance of Schedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Schedule.parse_obj(obj)

        _obj = Schedule.parse_obj({
            "type":
            obj.get("type"),
            "months":
            ScheduleMonths.from_dict(obj.get("months"))
            if obj.get("months") is not None else None,
            "days":
            ScheduleDays.from_dict(obj.get("days"))
            if obj.get("days") is not None else None,
            "hours":
            ScheduleHours.from_dict(obj.get("hours"))
            if obj.get("hours") is not None else None,
            "expiration":
            obj.get("expiration"),
            "time_zone_id":
            obj.get("timeZoneId")
        })
        return _obj
