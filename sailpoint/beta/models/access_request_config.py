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

from typing import Optional
from pydantic import BaseModel, Field, StrictBool
from sailpoint.beta.models.approval_reminder_and_escalation_config import ApprovalReminderAndEscalationConfig
from sailpoint.beta.models.entitlement_request_config1 import EntitlementRequestConfig1
from sailpoint.beta.models.request_on_behalf_of_config import RequestOnBehalfOfConfig


class AccessRequestConfig(BaseModel):
    """
    AccessRequestConfig
    """
    approvals_must_be_external: Optional[StrictBool] = Field(
        None,
        alias="approvalsMustBeExternal",
        description=
        "If true, then approvals must be processed by external system.")
    auto_approval_enabled: Optional[StrictBool] = Field(
        None,
        alias="autoApprovalEnabled",
        description=
        "If true and requester and reviewer are the same, then automatically approve the approval."
    )
    request_on_behalf_of_config: Optional[RequestOnBehalfOfConfig] = Field(
        None, alias="requestOnBehalfOfConfig")
    approval_reminder_and_escalation_config: Optional[
        ApprovalReminderAndEscalationConfig] = Field(
            None, alias="approvalReminderAndEscalationConfig")
    entitlement_request_config: Optional[EntitlementRequestConfig1] = Field(
        None, alias="entitlementRequestConfig")
    __properties = [
        "approvalsMustBeExternal", "autoApprovalEnabled",
        "requestOnBehalfOfConfig", "approvalReminderAndEscalationConfig",
        "entitlementRequestConfig"
    ]

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
    def from_json(cls, json_str: str) -> AccessRequestConfig:
        """Create an instance of AccessRequestConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of request_on_behalf_of_config
        if self.request_on_behalf_of_config:
            _dict[
                'requestOnBehalfOfConfig'] = self.request_on_behalf_of_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of approval_reminder_and_escalation_config
        if self.approval_reminder_and_escalation_config:
            _dict[
                'approvalReminderAndEscalationConfig'] = self.approval_reminder_and_escalation_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of entitlement_request_config
        if self.entitlement_request_config:
            _dict[
                'entitlementRequestConfig'] = self.entitlement_request_config.to_dict(
                )
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccessRequestConfig:
        """Create an instance of AccessRequestConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccessRequestConfig.parse_obj(obj)

        _obj = AccessRequestConfig.parse_obj({
            "approvals_must_be_external":
            obj.get("approvalsMustBeExternal"),
            "auto_approval_enabled":
            obj.get("autoApprovalEnabled"),
            "request_on_behalf_of_config":
            RequestOnBehalfOfConfig.from_dict(
                obj.get("requestOnBehalfOfConfig"))
            if obj.get("requestOnBehalfOfConfig") is not None else None,
            "approval_reminder_and_escalation_config":
            ApprovalReminderAndEscalationConfig.from_dict(
                obj.get("approvalReminderAndEscalationConfig"))
            if obj.get("approvalReminderAndEscalationConfig") is not None else
            None,
            "entitlement_request_config":
            EntitlementRequestConfig1.from_dict(
                obj.get("entitlementRequestConfig"))
            if obj.get("entitlementRequestConfig") is not None else None
        })
        return _obj
