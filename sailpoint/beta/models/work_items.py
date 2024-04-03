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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.approval_item_details import ApprovalItemDetails
from sailpoint.beta.models.remediation_item_details import RemediationItemDetails
from sailpoint.beta.models.work_item_state import WorkItemState
from sailpoint.beta.models.work_item_type import WorkItemType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkItems(BaseModel):
    """
    WorkItems
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the work item")
    requester_id: Optional[StrictStr] = Field(default=None, description="ID of the requester", alias="requesterId")
    requester_display_name: Optional[StrictStr] = Field(default=None, description="The displayname of the requester", alias="requesterDisplayName")
    owner_id: Optional[StrictStr] = Field(default=None, description="The ID of the owner", alias="ownerId")
    owner_name: Optional[StrictStr] = Field(default=None, description="The name of the owner", alias="ownerName")
    created: Optional[datetime] = None
    modified: Optional[datetime] = None
    description: Optional[StrictStr] = Field(default=None, description="The description of the work item")
    state: Optional[WorkItemState] = None
    type: Optional[WorkItemType] = None
    remediation_items: Optional[RemediationItemDetails] = Field(default=None, alias="remediationItems")
    approval_items: Optional[ApprovalItemDetails] = Field(default=None, alias="approvalItems")
    name: Optional[StrictStr] = Field(default=None, description="The work item name")
    completed: Optional[datetime] = None
    num_items: Optional[StrictInt] = Field(default=None, description="The number of items in the work item", alias="numItems")
    errors: Optional[List[StrictStr]] = None
    __properties: ClassVar[List[str]] = ["id", "requesterId", "requesterDisplayName", "ownerId", "ownerName", "created", "modified", "description", "state", "type", "remediationItems", "approvalItems", "name", "completed", "numItems", "errors"]

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
        """Create an instance of WorkItems from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of remediation_items
        if self.remediation_items:
            _dict['remediationItems'] = self.remediation_items.to_dict()
        # override the default output from pydantic by calling `to_dict()` of approval_items
        if self.approval_items:
            _dict['approvalItems'] = self.approval_items.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkItems from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "requesterId": obj.get("requesterId"),
            "requesterDisplayName": obj.get("requesterDisplayName"),
            "ownerId": obj.get("ownerId"),
            "ownerName": obj.get("ownerName"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "description": obj.get("description"),
            "state": obj.get("state"),
            "type": obj.get("type"),
            "remediationItems": RemediationItemDetails.from_dict(obj.get("remediationItems")) if obj.get("remediationItems") is not None else None,
            "approvalItems": ApprovalItemDetails.from_dict(obj.get("approvalItems")) if obj.get("approvalItems") is not None else None,
            "name": obj.get("name"),
            "completed": obj.get("completed"),
            "numItems": obj.get("numItems"),
            "errors": obj.get("errors")
        })
        return _obj


