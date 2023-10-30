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

class NonEmployeeBulkUploadJob(BaseModel):
    """
    NonEmployeeBulkUploadJob
    """
    id: Optional[StrictStr] = Field(None, description="The bulk upload job's ID. (UUID)")
    source_id: Optional[StrictStr] = Field(None, alias="sourceId", description="The ID of the source to bulk-upload non-employees to. (UUID)")
    created: Optional[datetime] = Field(None, description="The date-time the job was submitted.")
    modified: Optional[datetime] = Field(None, description="The date-time that the job was last updated.")
    status: Optional[StrictStr] = Field(None, description="Returns the following values indicating the progress or result of the bulk upload job. \"PENDING\" means the job is queued and waiting to be processed. \"IN_PROGRESS\" means the job is currently being processed. \"COMPLETED\" means the job has been completed without any errors. \"ERROR\" means the job failed to process with errors. ")
    __properties = ["id", "sourceId", "created", "modified", "status"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'ERROR'):
            raise ValueError("must be one of enum values ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'ERROR')")
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
    def from_json(cls, json_str: str) -> NonEmployeeBulkUploadJob:
        """Create an instance of NonEmployeeBulkUploadJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonEmployeeBulkUploadJob:
        """Create an instance of NonEmployeeBulkUploadJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonEmployeeBulkUploadJob.parse_obj(obj)

        _obj = NonEmployeeBulkUploadJob.parse_obj({
            "id": obj.get("id"),
            "source_id": obj.get("sourceId"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "status": obj.get("status")
        })
        return _obj


