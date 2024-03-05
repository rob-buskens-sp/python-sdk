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
from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SpConfigExportJobStatus(BaseModel):
    """
    SpConfigExportJobStatus
    """ # noqa: E501
    job_id: StrictStr = Field(description="Unique id assigned to this job.", alias="jobId")
    status: StrictStr = Field(description="Status of the job.")
    type: StrictStr = Field(description="Type of the job, either export or import.")
    expiration: datetime = Field(description="The time until which the artifacts will be available for download.")
    created: datetime = Field(description="The time the job was started.")
    modified: datetime = Field(description="The time of the last update to the job.")
    description: StrictStr = Field(description="Optional user defined description/name for export job.")
    completed: datetime = Field(description="The time the job was completed.")
    __properties: ClassVar[List[str]] = ["jobId", "status", "type", "expiration", "created", "modified", "description", "completed"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'FAILED'):
            raise ValueError("must be one of enum values ('NOT_STARTED', 'IN_PROGRESS', 'COMPLETE', 'CANCELLED', 'FAILED')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('EXPORT', 'IMPORT'):
            raise ValueError("must be one of enum values ('EXPORT', 'IMPORT')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SpConfigExportJobStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SpConfigExportJobStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "jobId": obj.get("jobId"),
            "status": obj.get("status"),
            "type": obj.get("type"),
            "expiration": obj.get("expiration"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "description": obj.get("description"),
            "completed": obj.get("completed")
        })
        return _obj


