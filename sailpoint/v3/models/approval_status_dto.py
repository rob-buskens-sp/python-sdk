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
from sailpoint.v3.models.access_item_reviewed_by import AccessItemReviewedBy
from sailpoint.v3.models.approval_scheme import ApprovalScheme
from sailpoint.v3.models.approval_status_dto_original_owner import ApprovalStatusDtoOriginalOwner
from sailpoint.v3.models.error_message_dto import ErrorMessageDto
from sailpoint.v3.models.manual_work_item_state import ManualWorkItemState
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ApprovalStatusDto(BaseModel):
    """
    ApprovalStatusDto
    """

  # noqa: E501
    forwarded: Optional[StrictBool] = Field(
        default=None,
        description=
        "True if the request for this item was forwarded from one owner to another."
    )
    original_owner: Optional[ApprovalStatusDtoOriginalOwner] = Field(
        default=None, alias="originalOwner")
    current_owner: Optional[AccessItemReviewedBy] = Field(default=None,
                                                          alias="currentOwner")
    modified: Optional[datetime] = Field(
        default=None, description="Time at which item was modified.")
    status: Optional[ManualWorkItemState] = None
    scheme: Optional[ApprovalScheme] = None
    error_messages: Optional[List[ErrorMessageDto]] = Field(
        default=None,
        description=
        "If the request failed, includes any error messages that were generated.",
        alias="errorMessages")
    comment: Optional[StrictStr] = Field(
        default=None, description="Comment, if any, provided by the approver.")
    remove_date: Optional[datetime] = Field(
        default=None,
        description=
        "The date the role or access profile is no longer assigned to the specified identity.",
        alias="removeDate")
    __properties: ClassVar[List[str]] = [
        "forwarded", "originalOwner", "currentOwner", "modified", "status",
        "scheme", "errorMessages", "comment", "removeDate"
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
        """Create an instance of ApprovalStatusDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of original_owner
        if self.original_owner:
            _dict['originalOwner'] = self.original_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_owner
        if self.current_owner:
            _dict['currentOwner'] = self.current_owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in error_messages (list)
        _items = []
        if self.error_messages:
            for _item in self.error_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorMessages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApprovalStatusDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forwarded":
            obj.get("forwarded"),
            "originalOwner":
            ApprovalStatusDtoOriginalOwner.from_dict(obj.get("originalOwner"))
            if obj.get("originalOwner") is not None else None,
            "currentOwner":
            AccessItemReviewedBy.from_dict(obj.get("currentOwner"))
            if obj.get("currentOwner") is not None else None,
            "modified":
            obj.get("modified"),
            "status":
            obj.get("status"),
            "scheme":
            obj.get("scheme"),
            "errorMessages": [
                ErrorMessageDto.from_dict(_item)
                for _item in obj.get("errorMessages")
            ] if obj.get("errorMessages") is not None else None,
            "comment":
            obj.get("comment"),
            "removeDate":
            obj.get("removeDate")
        })
        return _obj
