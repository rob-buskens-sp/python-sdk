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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowExecution(BaseModel):
    """
    WorkflowExecution
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The workflow execution ID")
    workflow_id: Optional[StrictStr] = Field(default=None, description="The workflow ID", alias="workflowId")
    request_id: Optional[StrictStr] = Field(default=None, description="This backend ID tracks a workflow request in the system. You can provide this ID in a customer support ticket for debugging purposes.", alias="requestId")
    start_time: Optional[datetime] = Field(default=None, description="The date/time the workflow started", alias="startTime")
    close_time: Optional[datetime] = Field(default=None, description="The date/time the workflow ended", alias="closeTime")
    status: Optional[StrictStr] = Field(default=None, description="The workflow execution status")
    __properties: ClassVar[List[str]] = ["id", "workflowId", "requestId", "startTime", "closeTime", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Completed', 'Failed', 'Canceled', 'Running'):
            raise ValueError("must be one of enum values ('Completed', 'Failed', 'Canceled', 'Running')")
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
        """Create an instance of WorkflowExecution from a JSON string"""
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
        """Create an instance of WorkflowExecution from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "workflowId": obj.get("workflowId"),
            "requestId": obj.get("requestId"),
            "startTime": obj.get("startTime"),
            "closeTime": obj.get("closeTime"),
            "status": obj.get("status")
        })
        return _obj


