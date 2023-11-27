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
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator
from sailpoint.beta.models.access_item_requested_for import AccessItemRequestedFor
from sailpoint.beta.models.access_item_requester import AccessItemRequester
from sailpoint.beta.models.access_request_phases import AccessRequestPhases
from sailpoint.beta.models.access_request_type import AccessRequestType
from sailpoint.beta.models.approval_status_dto import ApprovalStatusDto
from sailpoint.beta.models.cancelled_request_details import CancelledRequestDetails
from sailpoint.beta.models.comment_dto import CommentDto
from sailpoint.beta.models.error_message_dto import ErrorMessageDto
from sailpoint.beta.models.manual_work_item_details import ManualWorkItemDetails
from sailpoint.beta.models.pre_approval_trigger_details import PreApprovalTriggerDetails
from sailpoint.beta.models.provisioning_details import ProvisioningDetails
from sailpoint.beta.models.requested_item_status_request_state import RequestedItemStatusRequestState
from sailpoint.beta.models.sod_violation_context_check_completed import SodViolationContextCheckCompleted


class RequestedItemStatus(BaseModel):
    """
    RequestedItemStatus
    """
    name: Optional[StrictStr] = Field(
        None,
        description="Human-readable display name of the item being requested.")
    type: Optional[StrictStr] = Field(None,
                                      description="Type of requested object.")
    cancelled_request_details: Optional[CancelledRequestDetails] = Field(
        None, alias="cancelledRequestDetails")
    error_messages: Optional[conlist(conlist(ErrorMessageDto))] = Field(
        None,
        alias="errorMessages",
        description=
        "List of list of localized error messages, if any, encountered during the approval/provisioning process."
    )
    state: Optional[RequestedItemStatusRequestState] = None
    approval_details: Optional[conlist(ApprovalStatusDto)] = Field(
        None,
        alias="approvalDetails",
        description="Approval details for each item.")
    manual_work_item_details: Optional[conlist(ManualWorkItemDetails)] = Field(
        None,
        alias="manualWorkItemDetails",
        description="Manual work items created for provisioning the item.")
    account_activity_item_id: Optional[StrictStr] = Field(
        None,
        alias="accountActivityItemId",
        description="Id of associated account activity item.")
    request_type: Optional[AccessRequestType] = Field(None,
                                                      alias="requestType")
    modified: Optional[datetime] = Field(
        None, description="When the request was last modified.")
    created: Optional[datetime] = Field(
        None, description="When the request was created.")
    requester: Optional[AccessItemRequester] = None
    requested_for: Optional[AccessItemRequestedFor] = Field(
        None, alias="requestedFor")
    requester_comment: Optional[CommentDto] = Field(None,
                                                    alias="requesterComment")
    sod_violation_context: Optional[SodViolationContextCheckCompleted] = Field(
        None, alias="sodViolationContext")
    provisioning_details: Optional[ProvisioningDetails] = Field(
        None, alias="provisioningDetails")
    pre_approval_trigger_details: Optional[PreApprovalTriggerDetails] = Field(
        None, alias="preApprovalTriggerDetails")
    access_request_phases: Optional[conlist(AccessRequestPhases)] = Field(
        None,
        alias="accessRequestPhases",
        description=
        "A list of Phases that the Access Request has gone through in order, to help determine the status of the request."
    )
    description: Optional[StrictStr] = Field(
        None, description="Description associated to the requested object.")
    remove_date: Optional[datetime] = Field(
        None,
        alias="removeDate",
        description="When the role access is scheduled for removal.")
    cancelable: Optional[StrictBool] = Field(
        None, description="True if the request can be canceled.")
    access_request_id: Optional[StrictStr] = Field(
        None,
        alias="accessRequestId",
        description="This is the account activity id.")
    client_metadata: Optional[Dict[str, StrictStr]] = Field(
        None,
        alias="clientMetadata",
        description=
        "Arbitrary key-value pairs, if any were included in the corresponding access request"
    )
    __properties = [
        "name", "type", "cancelledRequestDetails", "errorMessages", "state",
        "approvalDetails", "manualWorkItemDetails", "accountActivityItemId",
        "requestType", "modified", "created", "requester", "requestedFor",
        "requesterComment", "sodViolationContext", "provisioningDetails",
        "preApprovalTriggerDetails", "accessRequestPhases", "description",
        "removeDate", "cancelable", "accessRequestId", "clientMetadata"
    ]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACCESS_PROFILE', 'ROLE', 'ENTITLEMENT'):
            raise ValueError(
                "must be one of enum values ('ACCESS_PROFILE', 'ROLE', 'ENTITLEMENT')"
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
    def from_json(cls, json_str: str) -> RequestedItemStatus:
        """Create an instance of RequestedItemStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cancelled_request_details
        if self.cancelled_request_details:
            _dict[
                'cancelledRequestDetails'] = self.cancelled_request_details.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in error_messages (list of list)
        _items = []
        if self.error_messages:
            for _item in self.error_messages:
                if _item:
                    _items.append([
                        _inner_item.to_dict() for _inner_item in _item
                        if _inner_item is not None
                    ])
            _dict['errorMessages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in approval_details (list)
        _items = []
        if self.approval_details:
            for _item in self.approval_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvalDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in manual_work_item_details (list)
        _items = []
        if self.manual_work_item_details:
            for _item in self.manual_work_item_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['manualWorkItemDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_for
        if self.requested_for:
            _dict['requestedFor'] = self.requested_for.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requester_comment
        if self.requester_comment:
            _dict['requesterComment'] = self.requester_comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sod_violation_context
        if self.sod_violation_context:
            _dict['sodViolationContext'] = self.sod_violation_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of provisioning_details
        if self.provisioning_details:
            _dict['provisioningDetails'] = self.provisioning_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pre_approval_trigger_details
        if self.pre_approval_trigger_details:
            _dict[
                'preApprovalTriggerDetails'] = self.pre_approval_trigger_details.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of each item in access_request_phases (list)
        _items = []
        if self.access_request_phases:
            for _item in self.access_request_phases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accessRequestPhases'] = _items
        # set to None if error_messages (nullable) is None
        # and __fields_set__ contains the field
        if self.error_messages is None and "error_messages" in self.__fields_set__:
            _dict['errorMessages'] = None

        # set to None if manual_work_item_details (nullable) is None
        # and __fields_set__ contains the field
        if self.manual_work_item_details is None and "manual_work_item_details" in self.__fields_set__:
            _dict['manualWorkItemDetails'] = None

        # set to None if remove_date (nullable) is None
        # and __fields_set__ contains the field
        if self.remove_date is None and "remove_date" in self.__fields_set__:
            _dict['removeDate'] = None

        # set to None if client_metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.client_metadata is None and "client_metadata" in self.__fields_set__:
            _dict['clientMetadata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestedItemStatus:
        """Create an instance of RequestedItemStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestedItemStatus.parse_obj(obj)

        _obj = RequestedItemStatus.parse_obj({
            "name":
            obj.get("name"),
            "type":
            obj.get("type"),
            "cancelled_request_details":
            CancelledRequestDetails.from_dict(
                obj.get("cancelledRequestDetails"))
            if obj.get("cancelledRequestDetails") is not None else None,
            "error_messages":
            [[ErrorMessageDto.from_dict(_inner_item) for _inner_item in _item]
             for _item in obj.get("errorMessages")]
            if obj.get("errorMessages") is not None else None,
            "state":
            obj.get("state"),
            "approval_details": [
                ApprovalStatusDto.from_dict(_item)
                for _item in obj.get("approvalDetails")
            ] if obj.get("approvalDetails") is not None else None,
            "manual_work_item_details": [
                ManualWorkItemDetails.from_dict(_item)
                for _item in obj.get("manualWorkItemDetails")
            ] if obj.get("manualWorkItemDetails") is not None else None,
            "account_activity_item_id":
            obj.get("accountActivityItemId"),
            "request_type":
            obj.get("requestType"),
            "modified":
            obj.get("modified"),
            "created":
            obj.get("created"),
            "requester":
            AccessItemRequester.from_dict(obj.get("requester"))
            if obj.get("requester") is not None else None,
            "requested_for":
            AccessItemRequestedFor.from_dict(obj.get("requestedFor"))
            if obj.get("requestedFor") is not None else None,
            "requester_comment":
            CommentDto.from_dict(obj.get("requesterComment"))
            if obj.get("requesterComment") is not None else None,
            "sod_violation_context":
            SodViolationContextCheckCompleted.from_dict(
                obj.get("sodViolationContext"))
            if obj.get("sodViolationContext") is not None else None,
            "provisioning_details":
            ProvisioningDetails.from_dict(obj.get("provisioningDetails"))
            if obj.get("provisioningDetails") is not None else None,
            "pre_approval_trigger_details":
            PreApprovalTriggerDetails.from_dict(
                obj.get("preApprovalTriggerDetails"))
            if obj.get("preApprovalTriggerDetails") is not None else None,
            "access_request_phases": [
                AccessRequestPhases.from_dict(_item)
                for _item in obj.get("accessRequestPhases")
            ] if obj.get("accessRequestPhases") is not None else None,
            "description":
            obj.get("description"),
            "remove_date":
            obj.get("removeDate"),
            "cancelable":
            obj.get("cancelable"),
            "access_request_id":
            obj.get("accessRequestId"),
            "client_metadata":
            obj.get("clientMetadata")
        })
        return _obj
