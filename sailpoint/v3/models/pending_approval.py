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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.v3.models.access_item_requested_for import AccessItemRequestedFor
from sailpoint.v3.models.access_item_requester import AccessItemRequester
from sailpoint.v3.models.access_request_type import AccessRequestType
from sailpoint.v3.models.approval_forward_history import ApprovalForwardHistory
from sailpoint.v3.models.comment_dto import CommentDto
from sailpoint.v3.models.pending_approval_action import PendingApprovalAction
from sailpoint.v3.models.pending_approval_owner import PendingApprovalOwner
from sailpoint.v3.models.requestable_object_reference import RequestableObjectReference
from sailpoint.v3.models.sod_violation_context_check_completed import SodViolationContextCheckCompleted
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class PendingApproval(BaseModel):
    """
    PendingApproval
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="The approval id.")
    name: Optional[StrictStr] = Field(default=None,
                                      description="The name of the approval.")
    created: Optional[datetime] = Field(
        default=None, description="When the approval was created.")
    modified: Optional[datetime] = Field(
        default=None, description="When the approval was modified last time.")
    request_created: Optional[datetime] = Field(
        default=None,
        description="When the access-request was created.",
        alias="requestCreated")
    request_type: Optional[AccessRequestType] = Field(default=None,
                                                      alias="requestType")
    requester: Optional[AccessItemRequester] = None
    requested_for: Optional[AccessItemRequestedFor] = Field(
        default=None, alias="requestedFor")
    owner: Optional[PendingApprovalOwner] = None
    requested_object: Optional[RequestableObjectReference] = Field(
        default=None, alias="requestedObject")
    requester_comment: Optional[CommentDto] = Field(default=None,
                                                    alias="requesterComment")
    previous_reviewers_comments: Optional[List[CommentDto]] = Field(
        default=None,
        description="The history of the previous reviewers comments.",
        alias="previousReviewersComments")
    forward_history: Optional[List[ApprovalForwardHistory]] = Field(
        default=None,
        description="The history of approval forward action.",
        alias="forwardHistory")
    comment_required_when_rejected: Optional[StrictBool] = Field(
        default=None,
        description=
        "When true the rejector has to provide comments when rejecting",
        alias="commentRequiredWhenRejected")
    action_in_process: Optional[PendingApprovalAction] = Field(
        default=None, alias="actionInProcess")
    remove_date: Optional[datetime] = Field(
        default=None,
        description=
        "The date the role or access profile is no longer assigned to the specified identity.",
        alias="removeDate")
    remove_date_update_requested: Optional[StrictBool] = Field(
        default=None,
        description=
        "If true, then the request is to change the remove date or sunset date.",
        alias="removeDateUpdateRequested")
    current_remove_date: Optional[datetime] = Field(
        default=None,
        description=
        "The remove date or sunset date that was assigned at the time of the request.",
        alias="currentRemoveDate")
    sod_violation_context: Optional[SodViolationContextCheckCompleted] = Field(
        default=None, alias="sodViolationContext")
    __properties: ClassVar[List[str]] = [
        "id", "name", "created", "modified", "requestCreated", "requestType",
        "requester", "requestedFor", "owner", "requestedObject",
        "requesterComment", "previousReviewersComments", "forwardHistory",
        "commentRequiredWhenRejected", "actionInProcess", "removeDate",
        "removeDateUpdateRequested", "currentRemoveDate", "sodViolationContext"
    ]

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
        """Create an instance of PendingApproval from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_for
        if self.requested_for:
            _dict['requestedFor'] = self.requested_for.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_object
        if self.requested_object:
            _dict['requestedObject'] = self.requested_object.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requester_comment
        if self.requester_comment:
            _dict['requesterComment'] = self.requester_comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in previous_reviewers_comments (list)
        _items = []
        if self.previous_reviewers_comments:
            for _item in self.previous_reviewers_comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['previousReviewersComments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in forward_history (list)
        _items = []
        if self.forward_history:
            for _item in self.forward_history:
                if _item:
                    _items.append(_item.to_dict())
            _dict['forwardHistory'] = _items
        # override the default output from pydantic by calling `to_dict()` of sod_violation_context
        if self.sod_violation_context:
            _dict['sodViolationContext'] = self.sod_violation_context.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of PendingApproval from a dict"""
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
            "requestCreated":
            obj.get("requestCreated"),
            "requestType":
            obj.get("requestType"),
            "requester":
            AccessItemRequester.from_dict(obj.get("requester"))
            if obj.get("requester") is not None else None,
            "requestedFor":
            AccessItemRequestedFor.from_dict(obj.get("requestedFor"))
            if obj.get("requestedFor") is not None else None,
            "owner":
            PendingApprovalOwner.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "requestedObject":
            RequestableObjectReference.from_dict(obj.get("requestedObject"))
            if obj.get("requestedObject") is not None else None,
            "requesterComment":
            CommentDto.from_dict(obj.get("requesterComment"))
            if obj.get("requesterComment") is not None else None,
            "previousReviewersComments": [
                CommentDto.from_dict(_item)
                for _item in obj.get("previousReviewersComments")
            ] if obj.get("previousReviewersComments") is not None else None,
            "forwardHistory": [
                ApprovalForwardHistory.from_dict(_item)
                for _item in obj.get("forwardHistory")
            ] if obj.get("forwardHistory") is not None else None,
            "commentRequiredWhenRejected":
            obj.get("commentRequiredWhenRejected"),
            "actionInProcess":
            obj.get("actionInProcess"),
            "removeDate":
            obj.get("removeDate"),
            "removeDateUpdateRequested":
            obj.get("removeDateUpdateRequested"),
            "currentRemoveDate":
            obj.get("currentRemoveDate"),
            "sodViolationContext":
            SodViolationContextCheckCompleted.from_dict(
                obj.get("sodViolationContext"))
            if obj.get("sodViolationContext") is not None else None
        })
        return _obj
