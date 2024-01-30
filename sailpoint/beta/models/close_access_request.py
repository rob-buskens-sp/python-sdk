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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CloseAccessRequest(BaseModel):
    """
    Request body payload for close access requests endpoint.
    """ # noqa: E501
    access_request_ids: List[StrictStr] = Field(
        description=
        "Access Request IDs for the requests to be closed. Accepts 1-500 Identity Request IDs per request.",
        alias="accessRequestIds")
    message: Optional[StrictStr] = Field(
        default='The IdentityNow Administrator manually closed this request.',
        description=
        "Reason for closing the access request. Displayed under Warnings in IdentityNow."
    )
    execution_status: Optional[StrictStr] = Field(
        default='Terminated',
        description=
        "The request's provisioning status. Displayed as Stage in IdentityNow.",
        alias="executionStatus")
    completion_status: Optional[StrictStr] = Field(
        default='Failure',
        description=
        "The request's overall status. Displayed as Status in IdentityNow.",
        alias="completionStatus")
    __properties: ClassVar[List[str]] = [
        "accessRequestIds", "message", "executionStatus", "completionStatus"
    ]

    @field_validator('execution_status')
    def execution_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Terminated', 'Completed'):
            raise ValueError(
                "must be one of enum values ('Terminated', 'Completed')")
        return value

    @field_validator('completion_status')
    def completion_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Success', 'Incomplete', 'Failure'):
            raise ValueError(
                "must be one of enum values ('Success', 'Incomplete', 'Failure')"
            )
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
        """Create an instance of CloseAccessRequest from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CloseAccessRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessRequestIds":
            obj.get("accessRequestIds"),
            "message":
            obj.get("message") if obj.get("message") is not None else
            'The IdentityNow Administrator manually closed this request.',
            "executionStatus":
            obj.get("executionStatus")
            if obj.get("executionStatus") is not None else 'Terminated',
            "completionStatus":
            obj.get("completionStatus")
            if obj.get("completionStatus") is not None else 'Failure'
        })
        return _obj
