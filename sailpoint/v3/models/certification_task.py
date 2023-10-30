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
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from v3.models.error_message_dto import ErrorMessageDto
from v3.models.reassignment_trail_dto import ReassignmentTrailDTO

class CertificationTask(BaseModel):
    """
    CertificationTask
    """
    id: Optional[StrictStr] = Field(None, description="The ID of the certification task.")
    type: Optional[StrictStr] = Field(None, description="The type of the certification task. More values may be added in the future.")
    target_type: Optional[StrictStr] = Field(None, alias="targetType", description="The type of item that is being operated on by this task whose ID is stored in the targetId field.")
    target_id: Optional[StrictStr] = Field(None, alias="targetId", description="The ID of the item being operated on by this task.")
    status: Optional[StrictStr] = Field(None, description="The status of the task.")
    errors: Optional[conlist(ErrorMessageDto)] = None
    reassignment_trail_dtos: Optional[conlist(ReassignmentTrailDTO)] = Field(None, alias="reassignmentTrailDTOs", description="Reassignment trails that lead to self certification identity")
    created: Optional[datetime] = Field(None, description="The date and time on which this task was created.")
    __properties = ["id", "type", "targetType", "targetId", "status", "errors", "reassignmentTrailDTOs", "created"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('REASSIGN', 'ADMIN_REASSIGN', 'COMPLETE_CERTIFICATION', 'FINISH_CERTIFICATION', 'COMPLETE_CAMPAIGN', 'ACTIVATE_CAMPAIGN', 'CAMPAIGN_CREATE', 'CAMPAIGN_DELETE'):
            raise ValueError("must be one of enum values ('REASSIGN', 'ADMIN_REASSIGN', 'COMPLETE_CERTIFICATION', 'FINISH_CERTIFICATION', 'COMPLETE_CAMPAIGN', 'ACTIVATE_CAMPAIGN', 'CAMPAIGN_CREATE', 'CAMPAIGN_DELETE')")
        return value

    @validator('target_type')
    def target_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CERTIFICATION', 'CAMPAIGN'):
            raise ValueError("must be one of enum values ('CERTIFICATION', 'CAMPAIGN')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('QUEUED', 'IN_PROGRESS', 'SUCCESS', 'ERROR'):
            raise ValueError("must be one of enum values ('QUEUED', 'IN_PROGRESS', 'SUCCESS', 'ERROR')")
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
    def from_json(cls, json_str: str) -> CertificationTask:
        """Create an instance of CertificationTask from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reassignment_trail_dtos (list)
        _items = []
        if self.reassignment_trail_dtos:
            for _item in self.reassignment_trail_dtos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['reassignmentTrailDTOs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CertificationTask:
        """Create an instance of CertificationTask from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CertificationTask.parse_obj(obj)

        _obj = CertificationTask.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "target_type": obj.get("targetType"),
            "target_id": obj.get("targetId"),
            "status": obj.get("status"),
            "errors": [ErrorMessageDto.from_dict(_item) for _item in obj.get("errors")] if obj.get("errors") is not None else None,
            "reassignment_trail_dtos": [ReassignmentTrailDTO.from_dict(_item) for _item in obj.get("reassignmentTrailDTOs")] if obj.get("reassignmentTrailDTOs") is not None else None,
            "created": obj.get("created")
        })
        return _obj


