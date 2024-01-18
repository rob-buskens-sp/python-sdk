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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.account_activity_item import AccountActivityItem
from sailpoint.v3.models.completion_status import CompletionStatus
from sailpoint.v3.models.execution_status import ExecutionStatus
from sailpoint.v3.models.identity_summary import IdentitySummary
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccountActivity(BaseModel):
    """
    AccountActivity
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="Id of the account activity")
    name: Optional[StrictStr] = Field(default=None,
                                      description="The name of the activity")
    created: Optional[datetime] = Field(
        default=None, description="When the activity was first created")
    modified: Optional[datetime] = Field(
        default=None, description="When the activity was last modified")
    completed: Optional[datetime] = Field(
        default=None, description="When the activity was completed")
    completion_status: Optional[CompletionStatus] = Field(
        default=None, alias="completionStatus")
    type: Optional[StrictStr] = Field(
        default=None,
        description=
        "The type of action the activity performed.  Please see the following list of types.  This list may grow over time.  - CloudAutomated - IdentityAttributeUpdate - appRequest - LifecycleStateChange - AccountStateUpdate - AccountAttributeUpdate - CloudPasswordRequest - Attribute Synchronization Refresh - Certification - Identity Refresh - Lifecycle Change Refresh   [Learn more here](https://documentation.sailpoint.com/saas/help/search/searchable-fields.html#searching-account-activity-data). "
    )
    requester_identity_summary: Optional[IdentitySummary] = Field(
        default=None, alias="requesterIdentitySummary")
    target_identity_summary: Optional[IdentitySummary] = Field(
        default=None, alias="targetIdentitySummary")
    errors: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of error messages, if any, that were encountered.")
    warnings: Optional[List[StrictStr]] = Field(
        default=None,
        description="A list of warning messages, if any, that were encountered."
    )
    items: Optional[List[AccountActivityItem]] = Field(
        default=None,
        description=
        "Individual actions performed as part of this account activity")
    execution_status: Optional[ExecutionStatus] = Field(
        default=None, alias="executionStatus")
    client_metadata: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description=
        "Arbitrary key-value pairs, if any were included in the corresponding access request",
        alias="clientMetadata")
    __properties: ClassVar[List[str]] = [
        "id", "name", "created", "modified", "completed", "completionStatus",
        "type", "requesterIdentitySummary", "targetIdentitySummary", "errors",
        "warnings", "items", "executionStatus", "clientMetadata"
    ]

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
        """Create an instance of AccountActivity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requester_identity_summary
        if self.requester_identity_summary:
            _dict[
                'requesterIdentitySummary'] = self.requester_identity_summary.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of target_identity_summary
        if self.target_identity_summary:
            _dict[
                'targetIdentitySummary'] = self.target_identity_summary.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # set to None if modified (nullable) is None
        # and model_fields_set contains the field
        if self.modified is None and "modified" in self.model_fields_set:
            _dict['modified'] = None

        # set to None if completed (nullable) is None
        # and model_fields_set contains the field
        if self.completed is None and "completed" in self.model_fields_set:
            _dict['completed'] = None

        # set to None if completion_status (nullable) is None
        # and model_fields_set contains the field
        if self.completion_status is None and "completion_status" in self.model_fields_set:
            _dict['completionStatus'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if requester_identity_summary (nullable) is None
        # and model_fields_set contains the field
        if self.requester_identity_summary is None and "requester_identity_summary" in self.model_fields_set:
            _dict['requesterIdentitySummary'] = None

        # set to None if target_identity_summary (nullable) is None
        # and model_fields_set contains the field
        if self.target_identity_summary is None and "target_identity_summary" in self.model_fields_set:
            _dict['targetIdentitySummary'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        # set to None if client_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.client_metadata is None and "client_metadata" in self.model_fields_set:
            _dict['clientMetadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountActivity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "completed":
            obj.get("completed"),
            "completionStatus":
            obj.get("completionStatus"),
            "type":
            obj.get("type"),
            "requesterIdentitySummary":
            IdentitySummary.from_dict(obj.get("requesterIdentitySummary"))
            if obj.get("requesterIdentitySummary") is not None else None,
            "targetIdentitySummary":
            IdentitySummary.from_dict(obj.get("targetIdentitySummary"))
            if obj.get("targetIdentitySummary") is not None else None,
            "errors":
            obj.get("errors"),
            "warnings":
            obj.get("warnings"),
            "items": [
                AccountActivityItem.from_dict(_item)
                for _item in obj.get("items")
            ] if obj.get("items") is not None else None,
            "executionStatus":
            obj.get("executionStatus"),
            "clientMetadata":
            obj.get("clientMetadata")
        })
        return _obj
