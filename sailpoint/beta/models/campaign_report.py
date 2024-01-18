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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.report_type import ReportType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CampaignReport(BaseModel):
    """
    CampaignReport
    """

  # noqa: E501
    type: Optional[StrictStr] = Field(
        default=None,
        description="SOD policy violation report result DTO type.")
    id: Optional[StrictStr] = Field(
        default=None, description="SOD policy violation report result ID.")
    name: Optional[StrictStr] = Field(
        default=None,
        description=
        "Human-readable name of the SOD policy violation report result.")
    status: Optional[StrictStr] = Field(
        default=None, description="Status of a SOD policy violation report.")
    report_type: ReportType = Field(alias="reportType")
    last_run_at: Optional[datetime] = Field(
        default=None,
        description="The most recent date and time this report was run",
        alias="lastRunAt")
    __properties: ClassVar[List[str]] = [
        "type", "id", "name", "status", "reportType", "lastRunAt"
    ]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('REPORT_RESULT'):
            raise ValueError("must be one of enum values ('REPORT_RESULT')")
        return value

    @field_validator('status')
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

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CampaignReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "last_run_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "reportType": obj.get("reportType"),
            "lastRunAt": obj.get("lastRunAt")
        })
        return _obj
