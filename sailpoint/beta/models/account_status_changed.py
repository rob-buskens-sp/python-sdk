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
from sailpoint.beta.models.account_status_changed_account import AccountStatusChangedAccount
from sailpoint.beta.models.account_status_changed_status_change import AccountStatusChangedStatusChange
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountStatusChanged(BaseModel):
    """
    AccountStatusChanged
    """ # noqa: E501
    event_type: Optional[StrictStr] = Field(default=None, description="the event type", alias="eventType")
    identity_id: Optional[StrictStr] = Field(default=None, description="the identity id", alias="identityId")
    dt: Optional[StrictStr] = Field(default=None, description="the date of event")
    account: Optional[AccountStatusChangedAccount] = None
    status_change: Optional[AccountStatusChangedStatusChange] = Field(default=None, alias="statusChange")
    __properties: ClassVar[List[str]] = ["eventType", "identityId", "dt", "account", "statusChange"]

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
        """Create an instance of AccountStatusChanged from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status_change
        if self.status_change:
            _dict['statusChange'] = self.status_change.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountStatusChanged from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventType": obj.get("eventType"),
            "identityId": obj.get("identityId"),
            "dt": obj.get("dt"),
            "account": AccountStatusChangedAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "statusChange": AccountStatusChangedStatusChange.from_dict(obj.get("statusChange")) if obj.get("statusChange") is not None else None
        })
        return _obj


