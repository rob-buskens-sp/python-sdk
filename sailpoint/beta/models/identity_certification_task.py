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
from pydantic import BaseModel, Field, StrictStr, conlist, validator


class IdentityCertificationTask(BaseModel):
    """
    IdentityCertificationTask
    """
    id: Optional[StrictStr] = Field(None, description="The task id")
    certification_id: Optional[StrictStr] = Field(
        None, alias="certificationId", description="The certification id")
    type: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    errors: Optional[conlist(StrictStr)] = Field(
        None, description="Any errors executing the task (Optional).")
    __properties = ["id", "certificationId", "type", "status", "errors"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('REASSIGN'):
            raise ValueError("must be one of enum values ('REASSIGN')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('QUEUED', 'IN_PROGRESS', 'SUCCESS', 'ERROR'):
            raise ValueError(
                "must be one of enum values ('QUEUED', 'IN_PROGRESS', 'SUCCESS', 'ERROR')"
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
    def from_json(cls, json_str: str) -> IdentityCertificationTask:
        """Create an instance of IdentityCertificationTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityCertificationTask:
        """Create an instance of IdentityCertificationTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityCertificationTask.parse_obj(obj)

        _obj = IdentityCertificationTask.parse_obj({
            "id":
            obj.get("id"),
            "certification_id":
            obj.get("certificationId"),
            "type":
            obj.get("type"),
            "status":
            obj.get("status"),
            "errors":
            obj.get("errors")
        })
        return _obj
