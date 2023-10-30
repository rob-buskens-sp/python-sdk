# coding: utf-8

"""
    IdentityNow cc (private) APIs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist
from cc.models.get_identity200_response_auth import GetIdentity200ResponseAuth
from cc.models.get_identity200_response_org import GetIdentity200ResponseOrg

class GetIdentity200Response(BaseModel):
    """
    GetIdentity200Response
    """
    id: Optional[StrictStr] = None
    alias: Optional[StrictStr] = None
    uid: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = Field(None, alias="displayName")
    uuid: Optional[StrictStr] = None
    encryption_key: Optional[Dict[str, Any]] = Field(None, alias="encryptionKey")
    encryption_check: Optional[Dict[str, Any]] = Field(None, alias="encryptionCheck")
    status: Optional[StrictStr] = None
    pending: Optional[StrictBool] = None
    password_reset_since_last_login: Optional[StrictBool] = Field(None, alias="passwordResetSinceLastLogin")
    usage_cert_attested: Optional[Dict[str, Any]] = Field(None, alias="usageCertAttested")
    user_flags: Optional[Dict[str, Any]] = Field(None, alias="userFlags")
    enabled: Optional[StrictBool] = None
    alt_auth_via: Optional[StrictStr] = Field(None, alias="altAuthVia")
    alt_auth_via_integration_data: Optional[Dict[str, Any]] = Field(None, alias="altAuthViaIntegrationData")
    kba_answers: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="kbaAnswers")
    disable_password_reset: Optional[StrictBool] = Field(None, alias="disablePasswordReset")
    pta_source_id: Optional[Dict[str, Any]] = Field(None, alias="ptaSourceId")
    supports_password_push: Optional[StrictBool] = Field(None, alias="supportsPasswordPush")
    attributes: Optional[Dict[str, Any]] = None
    external_id: Optional[StrictStr] = Field(None, alias="externalId")
    role: Optional[conlist(Dict[str, Any])] = None
    phone: Optional[Dict[str, Any]] = None
    email: Optional[StrictStr] = None
    personal_email: Optional[Dict[str, Any]] = Field(None, alias="personalEmail")
    employee_number: Optional[Dict[str, Any]] = Field(None, alias="employeeNumber")
    risk_score: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="riskScore")
    feature_flags: Optional[Dict[str, Any]] = Field(None, alias="featureFlags")
    feature: Optional[conlist(StrictStr)] = None
    org_encryption_key: Optional[StrictStr] = Field(None, alias="orgEncryptionKey")
    org_encryption_key_id: Optional[StrictStr] = Field(None, alias="orgEncryptionKeyId")
    meta: Optional[Dict[str, Any]] = None
    org: Optional[GetIdentity200ResponseOrg] = None
    step_up_auth: Optional[StrictBool] = Field(None, alias="stepUpAuth")
    bx_install_prompted: Optional[StrictBool] = Field(None, alias="bxInstallPrompted")
    federated_login: Optional[StrictBool] = Field(None, alias="federatedLogin")
    auth: Optional[GetIdentity200ResponseAuth] = None
    on_network: Optional[StrictBool] = Field(None, alias="onNetwork")
    on_trusted_geo: Optional[StrictBool] = Field(None, alias="onTrustedGeo")
    login_url: Optional[StrictStr] = Field(None, alias="loginUrl")
    __properties = ["id", "alias", "uid", "name", "displayName", "uuid", "encryptionKey", "encryptionCheck", "status", "pending", "passwordResetSinceLastLogin", "usageCertAttested", "userFlags", "enabled", "altAuthVia", "altAuthViaIntegrationData", "kbaAnswers", "disablePasswordReset", "ptaSourceId", "supportsPasswordPush", "attributes", "externalId", "role", "phone", "email", "personalEmail", "employeeNumber", "riskScore", "featureFlags", "feature", "orgEncryptionKey", "orgEncryptionKeyId", "meta", "org", "stepUpAuth", "bxInstallPrompted", "federatedLogin", "auth", "onNetwork", "onTrustedGeo", "loginUrl"]

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
    def from_json(cls, json_str: str) -> GetIdentity200Response:
        """Create an instance of GetIdentity200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of org
        if self.org:
            _dict['org'] = self.org.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth
        if self.auth:
            _dict['auth'] = self.auth.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetIdentity200Response:
        """Create an instance of GetIdentity200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetIdentity200Response.parse_obj(obj)

        _obj = GetIdentity200Response.parse_obj({
            "id": obj.get("id"),
            "alias": obj.get("alias"),
            "uid": obj.get("uid"),
            "name": obj.get("name"),
            "display_name": obj.get("displayName"),
            "uuid": obj.get("uuid"),
            "encryption_key": obj.get("encryptionKey"),
            "encryption_check": obj.get("encryptionCheck"),
            "status": obj.get("status"),
            "pending": obj.get("pending"),
            "password_reset_since_last_login": obj.get("passwordResetSinceLastLogin"),
            "usage_cert_attested": obj.get("usageCertAttested"),
            "user_flags": obj.get("userFlags"),
            "enabled": obj.get("enabled"),
            "alt_auth_via": obj.get("altAuthVia"),
            "alt_auth_via_integration_data": obj.get("altAuthViaIntegrationData"),
            "kba_answers": obj.get("kbaAnswers"),
            "disable_password_reset": obj.get("disablePasswordReset"),
            "pta_source_id": obj.get("ptaSourceId"),
            "supports_password_push": obj.get("supportsPasswordPush"),
            "attributes": obj.get("attributes"),
            "external_id": obj.get("externalId"),
            "role": obj.get("role"),
            "phone": obj.get("phone"),
            "email": obj.get("email"),
            "personal_email": obj.get("personalEmail"),
            "employee_number": obj.get("employeeNumber"),
            "risk_score": obj.get("riskScore"),
            "feature_flags": obj.get("featureFlags"),
            "feature": obj.get("feature"),
            "org_encryption_key": obj.get("orgEncryptionKey"),
            "org_encryption_key_id": obj.get("orgEncryptionKeyId"),
            "meta": obj.get("meta"),
            "org": GetIdentity200ResponseOrg.from_dict(obj.get("org")) if obj.get("org") is not None else None,
            "step_up_auth": obj.get("stepUpAuth"),
            "bx_install_prompted": obj.get("bxInstallPrompted"),
            "federated_login": obj.get("federatedLogin"),
            "auth": GetIdentity200ResponseAuth.from_dict(obj.get("auth")) if obj.get("auth") is not None else None,
            "on_network": obj.get("onNetwork"),
            "on_trusted_geo": obj.get("onTrustedGeo"),
            "login_url": obj.get("loginUrl")
        })
        return _obj


