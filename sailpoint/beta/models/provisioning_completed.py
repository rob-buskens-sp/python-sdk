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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.provisioning_completed_account_requests_inner import ProvisioningCompletedAccountRequestsInner
from sailpoint.beta.models.provisioning_completed_recipient import ProvisioningCompletedRecipient
from sailpoint.beta.models.provisioning_completed_requester import ProvisioningCompletedRequester
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ProvisioningCompleted(BaseModel):
    """
    ProvisioningCompleted
    """

  # noqa: E501
    tracking_number: StrictStr = Field(
        description=
        "The reference number of the provisioning request. Useful for tracking status in the Account Activity search interface.",
        alias="trackingNumber")
    sources: StrictStr = Field(
        description=
        "One or more sources that the provisioning transaction(s) were done against.  Sources are comma separated."
    )
    action: Optional[StrictStr] = Field(
        default=None,
        description="Origin of where the provisioning request came from.")
    errors: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "A list of any accumulated error messages that occurred during provisioning."
    )
    warnings: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "A list of any accumulated warning messages that occurred during provisioning."
    )
    recipient: ProvisioningCompletedRecipient
    requester: Optional[ProvisioningCompletedRequester] = None
    account_requests: List[ProvisioningCompletedAccountRequestsInner] = Field(
        description=
        "A list of provisioning instructions to perform on an account-by-account basis.",
        alias="accountRequests")
    __properties: ClassVar[List[str]] = [
        "trackingNumber", "sources", "action", "errors", "warnings",
        "recipient", "requester", "accountRequests"
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
        """Create an instance of ProvisioningCompleted from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recipient
        if self.recipient:
            _dict['recipient'] = self.recipient.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requester
        if self.requester:
            _dict['requester'] = self.requester.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in account_requests (list)
        _items = []
        if self.account_requests:
            for _item in self.account_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountRequests'] = _items
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        # set to None if requester (nullable) is None
        # and model_fields_set contains the field
        if self.requester is None and "requester" in self.model_fields_set:
            _dict['requester'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProvisioningCompleted from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "trackingNumber":
            obj.get("trackingNumber"),
            "sources":
            obj.get("sources"),
            "action":
            obj.get("action"),
            "errors":
            obj.get("errors"),
            "warnings":
            obj.get("warnings"),
            "recipient":
            ProvisioningCompletedRecipient.from_dict(obj.get("recipient"))
            if obj.get("recipient") is not None else None,
            "requester":
            ProvisioningCompletedRequester.from_dict(obj.get("requester"))
            if obj.get("requester") is not None else None,
            "accountRequests": [
                ProvisioningCompletedAccountRequestsInner.from_dict(_item)
                for _item in obj.get("accountRequests")
            ] if obj.get("accountRequests") is not None else None
        })
        return _obj
