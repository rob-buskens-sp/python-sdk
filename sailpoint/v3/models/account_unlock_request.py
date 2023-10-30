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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class AccountUnlockRequest(BaseModel):
    """
    Request used for account unlock  # noqa: E501
    """
    external_verification_id: Optional[StrictStr] = Field(None, alias="externalVerificationId", description="If set, an external process validates that the user wants to proceed with this request.")
    unlock_idn_account: Optional[StrictBool] = Field(None, alias="unlockIDNAccount", description="If set, the IDN account is unlocked after the workflow completes.")
    force_provisioning: Optional[StrictBool] = Field(None, alias="forceProvisioning", description="If set, provisioning updates the account attribute at the source.   This option is used when the account is not synced to ensure the attribute is updated.")
    __properties = ["externalVerificationId", "unlockIDNAccount", "forceProvisioning"]

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
    def from_json(cls, json_str: str) -> AccountUnlockRequest:
        """Create an instance of AccountUnlockRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountUnlockRequest:
        """Create an instance of AccountUnlockRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountUnlockRequest.parse_obj(obj)

        _obj = AccountUnlockRequest.parse_obj({
            "external_verification_id": obj.get("externalVerificationId"),
            "unlock_idn_account": obj.get("unlockIDNAccount"),
            "force_provisioning": obj.get("forceProvisioning")
        })
        return _obj


