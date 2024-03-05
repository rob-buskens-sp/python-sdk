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


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel
from pydantic import Field
from sailpoint.beta.models.account_attributes_changed_account import AccountAttributesChangedAccount
from sailpoint.beta.models.account_attributes_changed_changes_inner import AccountAttributesChangedChangesInner
from sailpoint.beta.models.account_attributes_changed_identity import AccountAttributesChangedIdentity
from sailpoint.beta.models.account_attributes_changed_source import AccountAttributesChangedSource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccountAttributesChanged(BaseModel):
    """
    AccountAttributesChanged
    """ # noqa: E501
    identity: AccountAttributesChangedIdentity
    source: AccountAttributesChangedSource
    account: AccountAttributesChangedAccount
    changes: List[AccountAttributesChangedChangesInner] = Field(description="A list of attributes that changed.")
    __properties: ClassVar[List[str]] = ["identity", "source", "account", "changes"]

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
        """Create an instance of AccountAttributesChanged from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in changes (list)
        _items = []
        if self.changes:
            for _item in self.changes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['changes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountAttributesChanged from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identity": AccountAttributesChangedIdentity.from_dict(obj.get("identity")) if obj.get("identity") is not None else None,
            "source": AccountAttributesChangedSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "account": AccountAttributesChangedAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "changes": [AccountAttributesChangedChangesInner.from_dict(_item) for _item in obj.get("changes")] if obj.get("changes") is not None else None
        })
        return _obj


