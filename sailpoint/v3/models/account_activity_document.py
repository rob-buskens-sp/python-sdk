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
from sailpoint.v3.models.account_request import AccountRequest
from sailpoint.v3.models.account_source import AccountSource
from sailpoint.v3.models.approval import Approval
from sailpoint.v3.models.document_type import DocumentType
from sailpoint.v3.models.expansion_item import ExpansionItem
from sailpoint.v3.models.original_request import OriginalRequest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountActivityDocument(BaseModel):
    """
    AccountActivity
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    type: DocumentType = Field(alias="_type")
    action: Optional[StrictStr] = Field(default=None, description="Type of action performed in the activity.")
    created: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the time when the object was created.")
    modified: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the time when the object was last modified.")
    stage: Optional[StrictStr] = Field(default=None, description="Activity's current stage.")
    origin: Optional[StrictStr] = Field(default=None, description="Activity's origin.")
    status: Optional[StrictStr] = Field(default=None, description="Activity's current status.")
    requester: Optional[AccountSource] = None
    recipient: Optional[AccountSource] = None
    tracking_number: Optional[StrictStr] = Field(default=None, description="Account activity's tracking number.", alias="trackingNumber")
    errors: Optional[List[StrictStr]] = Field(default=None, description="Errors provided by the source while completing account actions.")
    warnings: Optional[List[StrictStr]] = Field(default=None, description="Warnings provided by the source while completing account actions.")
    approvals: Optional[List[Approval]] = Field(default=None, description="Approvals performed on an item during activity.")
    original_requests: Optional[List[OriginalRequest]] = Field(default=None, description="Original actions that triggered all individual source actions related to the account action.", alias="originalRequests")
    expansion_items: Optional[List[ExpansionItem]] = Field(default=None, description="Controls that translated the attribute requests into actual provisioning actions on the source.", alias="expansionItems")
    account_requests: Optional[List[AccountRequest]] = Field(default=None, description="Account data for each individual source action triggered by the original requests.", alias="accountRequests")
    sources: Optional[StrictStr] = Field(default=None, description="Sources involved in the account activity.")
    __properties: ClassVar[List[str]] = ["id", "name", "_type", "action", "created", "modified", "stage", "origin", "status", "requester", "recipient", "trackingNumber", "errors", "warnings", "approvals", "originalRequests", "expansionItems", "accountRequests", "sources"]

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
        """Create an instance of AccountActivityDocument from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in approvals (list)
        _items = []
        if self.approvals:
            for _item in self.approvals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['approvals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in original_requests (list)
        _items = []
        if self.original_requests:
            for _item in self.original_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['originalRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in expansion_items (list)
        _items = []
        if self.expansion_items:
            for _item in self.expansion_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expansionItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_requests (list)
        _items = []
        if self.account_requests:
            for _item in self.account_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountRequests'] = _items
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if modified (nullable) is None
        # and model_fields_set contains the field
        if self.modified is None and "modified" in self.model_fields_set:
            _dict['modified'] = None

        # set to None if origin (nullable) is None
        # and model_fields_set contains the field
        if self.origin is None and "origin" in self.model_fields_set:
            _dict['origin'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountActivityDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "_type": obj.get("_type"),
            "action": obj.get("action"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "stage": obj.get("stage"),
            "origin": obj.get("origin"),
            "status": obj.get("status"),
            "requester": AccountSource.from_dict(obj.get("requester")) if obj.get("requester") is not None else None,
            "recipient": AccountSource.from_dict(obj.get("recipient")) if obj.get("recipient") is not None else None,
            "trackingNumber": obj.get("trackingNumber"),
            "errors": obj.get("errors"),
            "warnings": obj.get("warnings"),
            "approvals": [Approval.from_dict(_item) for _item in obj.get("approvals")] if obj.get("approvals") is not None else None,
            "originalRequests": [OriginalRequest.from_dict(_item) for _item in obj.get("originalRequests")] if obj.get("originalRequests") is not None else None,
            "expansionItems": [ExpansionItem.from_dict(_item) for _item in obj.get("expansionItems")] if obj.get("expansionItems") is not None else None,
            "accountRequests": [AccountRequest.from_dict(_item) for _item in obj.get("accountRequests")] if obj.get("accountRequests") is not None else None,
            "sources": obj.get("sources")
        })
        return _obj


