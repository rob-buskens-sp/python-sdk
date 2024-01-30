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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.v3.models.access_type import AccessType
from sailpoint.v3.models.client_type import ClientType
from sailpoint.v3.models.grant_type import GrantType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class GetOAuthClientResponse(BaseModel):
    """
    GetOAuthClientResponse
    """

  # noqa: E501
    id: StrictStr = Field(description="ID of the OAuth client")
    business_name: Optional[StrictStr] = Field(
        description="The name of the business the API Client should belong to",
        alias="businessName")
    homepage_url: Optional[StrictStr] = Field(
        description=
        "The homepage URL associated with the owner of the API Client",
        alias="homepageUrl")
    name: StrictStr = Field(
        description="A human-readable name for the API Client")
    description: Optional[StrictStr] = Field(
        description="A description of the API Client")
    access_token_validity_seconds: StrictInt = Field(
        description=
        "The number of seconds an access token generated for this API Client is valid for",
        alias="accessTokenValiditySeconds")
    refresh_token_validity_seconds: StrictInt = Field(
        description=
        "The number of seconds a refresh token generated for this API Client is valid for",
        alias="refreshTokenValiditySeconds")
    redirect_uris: Optional[List[StrictStr]] = Field(
        description=
        "A list of the approved redirect URIs used with the authorization_code flow",
        alias="redirectUris")
    grant_types: List[GrantType] = Field(
        description=
        "A list of OAuth 2.0 grant types this API Client can be used with",
        alias="grantTypes")
    access_type: AccessType = Field(alias="accessType")
    type: ClientType
    internal: StrictBool = Field(
        description=
        "An indicator of whether the API Client can be used for requests internal to IDN"
    )
    enabled: StrictBool = Field(
        description="An indicator of whether the API Client is enabled for use"
    )
    strong_auth_supported: StrictBool = Field(
        description=
        "An indicator of whether the API Client supports strong authentication",
        alias="strongAuthSupported")
    claims_supported: StrictBool = Field(
        description=
        "An indicator of whether the API Client supports the serialization of SAML claims when used with the authorization_code flow",
        alias="claimsSupported")
    created: datetime = Field(
        description=
        "The date and time, down to the millisecond, when the API Client was created"
    )
    modified: datetime = Field(
        description=
        "The date and time, down to the millisecond, when the API Client was last updated"
    )
    last_used: Optional[datetime] = Field(
        default=None,
        description=
        "The date and time, down to the millisecond, when this API Client was last used to generate an access token. This timestamp does not get updated on every API Client usage, but only once a day. This property can be useful for identifying which API Clients are no longer actively used and can be removed.",
        alias="lastUsed")
    scope: Optional[List[StrictStr]] = Field(
        description="Scopes of the API Client.")
    __properties: ClassVar[List[str]] = [
        "id", "businessName", "homepageUrl", "name", "description",
        "accessTokenValiditySeconds", "refreshTokenValiditySeconds",
        "redirectUris", "grantTypes", "accessType", "type", "internal",
        "enabled", "strongAuthSupported", "claimsSupported", "created",
        "modified", "lastUsed", "scope"
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
        """Create an instance of GetOAuthClientResponse from a JSON string"""
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
        # set to None if business_name (nullable) is None
        # and model_fields_set contains the field
        if self.business_name is None and "business_name" in self.model_fields_set:
            _dict['businessName'] = None

        # set to None if homepage_url (nullable) is None
        # and model_fields_set contains the field
        if self.homepage_url is None and "homepage_url" in self.model_fields_set:
            _dict['homepageUrl'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if redirect_uris (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_uris is None and "redirect_uris" in self.model_fields_set:
            _dict['redirectUris'] = None

        # set to None if last_used (nullable) is None
        # and model_fields_set contains the field
        if self.last_used is None and "last_used" in self.model_fields_set:
            _dict['lastUsed'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetOAuthClientResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "businessName":
            obj.get("businessName"),
            "homepageUrl":
            obj.get("homepageUrl"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "accessTokenValiditySeconds":
            obj.get("accessTokenValiditySeconds"),
            "refreshTokenValiditySeconds":
            obj.get("refreshTokenValiditySeconds"),
            "redirectUris":
            obj.get("redirectUris"),
            "grantTypes":
            obj.get("grantTypes"),
            "accessType":
            obj.get("accessType"),
            "type":
            obj.get("type"),
            "internal":
            obj.get("internal"),
            "enabled":
            obj.get("enabled"),
            "strongAuthSupported":
            obj.get("strongAuthSupported"),
            "claimsSupported":
            obj.get("claimsSupported"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "lastUsed":
            obj.get("lastUsed"),
            "scope":
            obj.get("scope")
        })
        return _obj
