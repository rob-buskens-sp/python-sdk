# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.task_return_details import TaskReturnDetails
from sailpoint.beta.models.task_status_message import TaskStatusMessage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TaskStatus(BaseModel):
    """
    Details and current status of a specific task
    """ # noqa: E501
    id: StrictStr = Field(description="System-generated unique ID of the task this TaskStatus represents")
    type: StrictStr = Field(description="Type of task this TaskStatus represents")
    unique_name: StrictStr = Field(description="Name of the task this TaskStatus represents", alias="uniqueName")
    description: StrictStr = Field(description="Description of the task this TaskStatus represents")
    parent_name: StrictStr = Field(description="Name of the parent of the task this TaskStatus represents", alias="parentName")
    launcher: StrictStr = Field(description="Service to execute the task this TaskStatus represents")
    created: datetime = Field(description="Creation date of the task this TaskStatus represents")
    modified: datetime = Field(description="Last modification date of the task this TaskStatus represents")
    launched: datetime = Field(description="Launch date of the task this TaskStatus represents")
    completed: datetime = Field(description="Completion date of the task this TaskStatus represents")
    completion_status: StrictStr = Field(description="Completion status of the task this TaskStatus represents", alias="completionStatus")
    messages: List[TaskStatusMessage] = Field(description="Messages associated with the task this TaskStatus represents")
    returns: List[TaskReturnDetails] = Field(description="Return values from the task this TaskStatus represents")
    attributes: Dict[str, Any] = Field(description="Attributes of the task this TaskStatus represents")
    progress: StrictStr = Field(description="Current progress of the task this TaskStatus represents")
    percent_complete: StrictInt = Field(description="Current percentage completion of the task this TaskStatus represents", alias="percentComplete")
    __properties: ClassVar[List[str]] = ["id", "type", "uniqueName", "description", "parentName", "launcher", "created", "modified", "launched", "completed", "completionStatus", "messages", "returns", "attributes", "progress", "percentComplete"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('QUARTZ', 'QPOC', 'QUEUED_TASK'):
            raise ValueError("must be one of enum values ('QUARTZ', 'QPOC', 'QUEUED_TASK')")
        return value

    @field_validator('completion_status')
    def completion_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Success', 'Warning', 'Error', 'Terminated', 'TempError'):
            raise ValueError("must be one of enum values ('Success', 'Warning', 'Error', 'Terminated', 'TempError')")
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
        """Create an instance of TaskStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in returns (list)
        _items = []
        if self.returns:
            for _item in self.returns:
                if _item:
                    _items.append(_item.to_dict())
            _dict['returns'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TaskStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "uniqueName": obj.get("uniqueName"),
            "description": obj.get("description"),
            "parentName": obj.get("parentName"),
            "launcher": obj.get("launcher"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "launched": obj.get("launched"),
            "completed": obj.get("completed"),
            "completionStatus": obj.get("completionStatus"),
            "messages": [TaskStatusMessage.from_dict(_item) for _item in obj.get("messages")] if obj.get("messages") is not None else None,
            "returns": [TaskReturnDetails.from_dict(_item) for _item in obj.get("returns")] if obj.get("returns") is not None else None,
            "attributes": obj.get("attributes"),
            "progress": obj.get("progress"),
            "percentComplete": obj.get("percentComplete")
        })
        return _obj


