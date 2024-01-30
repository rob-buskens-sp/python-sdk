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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.access_type import AccessType
from sailpoint.beta.models.client_type import ClientType
from sailpoint.beta.models.grant_type import GrantType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CreateOAuthClientRequest(BaseModel):
    """
    CreateOAuthClientRequest
    """

  # noqa: E501
    business_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the business the API Client should belong to",
        alias="businessName")
    homepage_url: Optional[StrictStr] = Field(
        default=None,
        description=
        "The homepage URL associated with the owner of the API Client",
        alias="homepageUrl")
    name: Optional[StrictStr] = Field(
        description="A human-readable name for the API Client")
    description: Optional[StrictStr] = Field(
        description="A description of the API Client")
    access_token_validity_seconds: StrictInt = Field(
        description=
        "The number of seconds an access token generated for this API Client is valid for",
        alias="accessTokenValiditySeconds")
    refresh_token_validity_seconds: Optional[StrictInt] = Field(
        default=None,
        description=
        "The number of seconds a refresh token generated for this API Client is valid for",
        alias="refreshTokenValiditySeconds")
    redirect_uris: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "A list of the approved redirect URIs. Provide one or more URIs when assigning the AUTHORIZATION_CODE grant type to a new OAuth Client.",
        alias="redirectUris")
    grant_types: Optional[List[GrantType]] = Field(
        description=
        "A list of OAuth 2.0 grant types this API Client can be used with",
        alias="grantTypes")
    access_type: AccessType = Field(alias="accessType")
    type: Optional[ClientType] = None
    internal: Optional[StrictBool] = Field(
        default=None,
        description=
        "An indicator of whether the API Client can be used for requests internal within the product."
    )
    enabled: StrictBool = Field(
        description="An indicator of whether the API Client is enabled for use"
    )
    strong_auth_supported: Optional[StrictBool] = Field(
        default=None,
        description=
        "An indicator of whether the API Client supports strong authentication",
        alias="strongAuthSupported")
    claims_supported: Optional[StrictBool] = Field(
        default=None,
        description=
        "An indicator of whether the API Client supports the serialization of SAML claims when used with the authorization_code flow",
        alias="claimsSupported")
    scope: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "Scopes of the API Client. If no scope is specified, the client will be created with the default scope \"sp:scopes:all\". This means the API Client will have all the rights of the owner who created it."
    )
    __properties: ClassVar[List[str]] = [
        "businessName", "homepageUrl", "name", "description",
        "accessTokenValiditySeconds", "refreshTokenValiditySeconds",
        "redirectUris", "grantTypes", "accessType", "type", "internal",
        "enabled", "strongAuthSupported", "claimsSupported", "scope"
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
        """Create an instance of CreateOAuthClientRequest from a JSON string"""
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

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if redirect_uris (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_uris is None and "redirect_uris" in self.model_fields_set:
            _dict['redirectUris'] = None

        # set to None if grant_types (nullable) is None
        # and model_fields_set contains the field
        if self.grant_types is None and "grant_types" in self.model_fields_set:
            _dict['grantTypes'] = None

        # set to None if scope (nullable) is None
        # and model_fields_set contains the field
        if self.scope is None and "scope" in self.model_fields_set:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CreateOAuthClientRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
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
            "scope":
            obj.get("scope")
        })
        return _obj
