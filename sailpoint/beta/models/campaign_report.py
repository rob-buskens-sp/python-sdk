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
from sailpoint.beta.models.report_type import ReportType


class CampaignReport(BaseModel):
    """
    CampaignReport
    """
    type: Optional[StrictStr] = Field(
        None, description="SOD policy violation report result DTO type.")
    id: Optional[StrictStr] = Field(
        None, description="SOD policy violation report result ID.")
    name: Optional[StrictStr] = Field(
        None,
        description=
        "Human-readable name of the SOD policy violation report result.")
    status: Optional[StrictStr] = Field(
        None, description="Status of a SOD policy violation report.")
    report_type: ReportType = Field(..., alias="reportType")
    last_run_at: Optional[datetime] = Field(
        None,
        alias="lastRunAt",
        description="The most recent date and time this report was run")
    __properties = ["type", "id", "name", "status", "reportType", "lastRunAt"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('REPORT_RESULT'):
            raise ValueError("must be one of enum values ('REPORT_RESULT')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'WARNING', 'ERROR', 'TERMINATED',
                         'TEMP_ERROR', 'PENDING'):
            raise ValueError(
                "must be one of enum values ('SUCCESS', 'WARNING', 'ERROR', 'TERMINATED', 'TEMP_ERROR', 'PENDING')"
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
    def from_json(cls, json_str: str) -> CampaignReport:
        """Create an instance of CampaignReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "last_run_at",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignReport:
        """Create an instance of CampaignReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignReport.parse_obj(obj)

        _obj = CampaignReport.parse_obj({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "report_type": obj.get("reportType"),
            "last_run_at": obj.get("lastRunAt")
        })
        return _obj
