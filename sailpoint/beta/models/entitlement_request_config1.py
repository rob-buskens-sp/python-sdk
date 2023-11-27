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
from pydantic import BaseModel, Field, StrictBool, StrictStr


class EntitlementRequestConfig1(BaseModel):
    """
    EntitlementRequestConfig1
    """
    allow_entitlement_request: Optional[StrictBool] = Field(
        None,
        alias="allowEntitlementRequest",
        description="Flag for allowing entitlement request.")
    request_comments_required: Optional[StrictBool] = Field(
        False,
        alias="requestCommentsRequired",
        description=
        "Flag for requiring comments while submitting an entitlement request.")
    denied_comments_required: Optional[StrictBool] = Field(
        False,
        alias="deniedCommentsRequired",
        description=
        "Flag for requiring comments while rejecting an entitlement request.")
    grant_request_approval_schemes: Optional[StrictStr] = Field(
        'sourceOwner',
        alias="grantRequestApprovalSchemes",
        description=
        "Approval schemes for granting entitlement request. This can be empty if no approval is needed. Multiple schemes must be comma-separated. The valid schemes are \"entitlementOwner\", \"sourceOwner\", \"manager\" and \"workgroup:{id}\". Multiple workgroups (governance groups) can be used. "
    )
    __properties = [
        "allowEntitlementRequest", "requestCommentsRequired",
        "deniedCommentsRequired", "grantRequestApprovalSchemes"
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
    def from_json(cls, json_str: str) -> EntitlementRequestConfig1:
        """Create an instance of EntitlementRequestConfig1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EntitlementRequestConfig1:
        """Create an instance of EntitlementRequestConfig1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EntitlementRequestConfig1.parse_obj(obj)

        _obj = EntitlementRequestConfig1.parse_obj({
            "allow_entitlement_request":
            obj.get("allowEntitlementRequest"),
            "request_comments_required":
            obj.get("requestCommentsRequired")
            if obj.get("requestCommentsRequired") is not None else False,
            "denied_comments_required":
            obj.get("deniedCommentsRequired")
            if obj.get("deniedCommentsRequired") is not None else False,
            "grant_request_approval_schemes":
            obj.get("grantRequestApprovalSchemes")
            if obj.get("grantRequestApprovalSchemes") is not None else
            'sourceOwner'
        })
        return _obj
