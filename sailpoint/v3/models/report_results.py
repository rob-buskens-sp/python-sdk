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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator


class ReportResults(BaseModel):
    """
    Details about report result or current state.  # noqa: E501
    """
    report_type: Optional[StrictStr] = Field(
        None,
        alias="reportType",
        description=
        "Use this property to define what report should be processed in the RDE service."
    )
    task_def_name: Optional[StrictStr] = Field(
        None,
        alias="taskDefName",
        description=
        "Name of the task definition which is started to process requesting report. Usually the same as report name"
    )
    id: Optional[StrictStr] = Field(
        None, description="Unique task definition identifier.")
    created: Optional[datetime] = Field(
        None, description="Report processing start date")
    status: Optional[StrictStr] = Field(
        None, description="Report current state or result status.")
    duration: Optional[StrictInt] = Field(
        None, description="Report processing time in ms.")
    rows: Optional[StrictInt] = Field(None, description="Report size in rows.")
    available_formats: Optional[conlist(StrictStr)] = Field(
        None,
        alias="availableFormats",
        description=
        "Output report file formats. This are formats for calling get endpoint as a query parameter 'fileFormat'.  In case report won't have this argument there will be ['CSV', 'PDF'] as default."
    )
    __properties = [
        "reportType", "taskDefName", "id", "created", "status", "duration",
        "rows", "availableFormats"
    ]

    @validator('report_type')
    def report_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACCOUNTS', 'IDENTITIES_DETAILS', 'IDENTITIES',
                         'IDENTITY_PROFILE_IDENTITY_ERROR',
                         'ORPHAN_IDENTITIES', 'SEARCH_EXPORT',
                         'UNCORRELATED_ACCOUNTS'):
            raise ValueError(
                "must be one of enum values ('ACCOUNTS', 'IDENTITIES_DETAILS', 'IDENTITIES', 'IDENTITY_PROFILE_IDENTITY_ERROR', 'ORPHAN_IDENTITIES', 'SEARCH_EXPORT', 'UNCORRELATED_ACCOUNTS')"
            )
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'FAILURE', 'WARNING', 'TERMINATED'):
            raise ValueError(
                "must be one of enum values ('SUCCESS', 'FAILURE', 'WARNING', 'TERMINATED')"
            )
        return value

    @validator('available_formats')
    def available_formats_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('CSV', 'PDF'):
                raise ValueError(
                    "each list item must be one of ('CSV', 'PDF')")
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
    def from_json(cls, json_str: str) -> ReportResults:
        """Create an instance of ReportResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReportResults:
        """Create an instance of ReportResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReportResults.parse_obj(obj)

        _obj = ReportResults.parse_obj({
            "report_type":
            obj.get("reportType"),
            "task_def_name":
            obj.get("taskDefName"),
            "id":
            obj.get("id"),
            "created":
            obj.get("created"),
            "status":
            obj.get("status"),
            "duration":
            obj.get("duration"),
            "rows":
            obj.get("rows"),
            "available_formats":
            obj.get("availableFormats")
        })
        return _obj
