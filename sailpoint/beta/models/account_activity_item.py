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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.account_activity_item_operation import AccountActivityItemOperation
from sailpoint.beta.models.account_request_info import AccountRequestInfo
from sailpoint.beta.models.comment import Comment
from sailpoint.beta.models.identity_summary import IdentitySummary
from sailpoint.beta.models.provisioning_state import ProvisioningState
from sailpoint.beta.models.work_item_state import WorkItemState
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccountActivityItem(BaseModel):
    """
    AccountActivityItem
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Item id")
    name: Optional[StrictStr] = Field(
        default=None, description="Human-readable display name of item")
    requested: Optional[datetime] = Field(
        default=None, description="Date and time item was requested")
    approval_status: Optional[WorkItemState] = Field(default=None,
                                                     alias="approvalStatus")
    provisioning_status: Optional[ProvisioningState] = Field(
        default=None, alias="provisioningStatus")
    requester_comment: Optional[Comment] = Field(default=None,
                                                 alias="requesterComment")
    reviewer_identity_summary: Optional[IdentitySummary] = Field(
        default=None, alias="reviewerIdentitySummary")
    reviewer_comment: Optional[Comment] = Field(default=None,
                                                alias="reviewerComment")
    operation: Optional[AccountActivityItemOperation] = None
    attribute: Optional[StrictStr] = Field(
        default=None,
        description="Attribute to which account activity applies")
    value: Optional[StrictStr] = Field(default=None,
                                       description="Value of attribute")
    native_identity: Optional[StrictStr] = Field(
        default=None,
        description=
        "Native identity in the target system to which the account activity applies",
        alias="nativeIdentity")
    source_id: Optional[StrictStr] = Field(
        default=None,
        description="Id of Source to which account activity applies",
        alias="sourceId")
    account_request_info: Optional[AccountRequestInfo] = Field(
        default=None, alias="accountRequestInfo")
    client_metadata: Optional[Dict[str, StrictStr]] = Field(
        default=None,
        description=
        "Arbitrary key-value pairs, if any were included in the corresponding access request item",
        alias="clientMetadata")
    remove_date: Optional[datetime] = Field(
        default=None,
        description=
        "The date the role or access profile is no longer assigned to the specified identity.",
        alias="removeDate")
    __properties: ClassVar[List[str]] = [
        "id", "name", "requested", "approvalStatus", "provisioningStatus",
        "requesterComment", "reviewerIdentitySummary", "reviewerComment",
        "operation", "attribute", "value", "nativeIdentity", "sourceId",
        "accountRequestInfo", "clientMetadata", "removeDate"
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
        """Create an instance of AccountActivityItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requester_comment
        if self.requester_comment:
            _dict['requesterComment'] = self.requester_comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reviewer_identity_summary
        if self.reviewer_identity_summary:
            _dict[
                'reviewerIdentitySummary'] = self.reviewer_identity_summary.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of reviewer_comment
        if self.reviewer_comment:
            _dict['reviewerComment'] = self.reviewer_comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account_request_info
        if self.account_request_info:
            _dict['accountRequestInfo'] = self.account_request_info.to_dict()
        # set to None if requester_comment (nullable) is None
        # and model_fields_set contains the field
        if self.requester_comment is None and "requester_comment" in self.model_fields_set:
            _dict['requesterComment'] = None

        # set to None if reviewer_identity_summary (nullable) is None
        # and model_fields_set contains the field
        if self.reviewer_identity_summary is None and "reviewer_identity_summary" in self.model_fields_set:
            _dict['reviewerIdentitySummary'] = None

        # set to None if reviewer_comment (nullable) is None
        # and model_fields_set contains the field
        if self.reviewer_comment is None and "reviewer_comment" in self.model_fields_set:
            _dict['reviewerComment'] = None

        # set to None if attribute (nullable) is None
        # and model_fields_set contains the field
        if self.attribute is None and "attribute" in self.model_fields_set:
            _dict['attribute'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if native_identity (nullable) is None
        # and model_fields_set contains the field
        if self.native_identity is None and "native_identity" in self.model_fields_set:
            _dict['nativeIdentity'] = None

        # set to None if account_request_info (nullable) is None
        # and model_fields_set contains the field
        if self.account_request_info is None and "account_request_info" in self.model_fields_set:
            _dict['accountRequestInfo'] = None

        # set to None if client_metadata (nullable) is None
        # and model_fields_set contains the field
        if self.client_metadata is None and "client_metadata" in self.model_fields_set:
            _dict['clientMetadata'] = None

        # set to None if remove_date (nullable) is None
        # and model_fields_set contains the field
        if self.remove_date is None and "remove_date" in self.model_fields_set:
            _dict['removeDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountActivityItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "requested":
            obj.get("requested"),
            "approvalStatus":
            obj.get("approvalStatus"),
            "provisioningStatus":
            obj.get("provisioningStatus"),
            "requesterComment":
            Comment.from_dict(obj.get("requesterComment"))
            if obj.get("requesterComment") is not None else None,
            "reviewerIdentitySummary":
            IdentitySummary.from_dict(obj.get("reviewerIdentitySummary"))
            if obj.get("reviewerIdentitySummary") is not None else None,
            "reviewerComment":
            Comment.from_dict(obj.get("reviewerComment"))
            if obj.get("reviewerComment") is not None else None,
            "operation":
            obj.get("operation"),
            "attribute":
            obj.get("attribute"),
            "value":
            obj.get("value"),
            "nativeIdentity":
            obj.get("nativeIdentity"),
            "sourceId":
            obj.get("sourceId"),
            "accountRequestInfo":
            AccountRequestInfo.from_dict(obj.get("accountRequestInfo"))
            if obj.get("accountRequestInfo") is not None else None,
            "clientMetadata":
            obj.get("clientMetadata"),
            "removeDate":
            obj.get("removeDate")
        })
        return _obj
