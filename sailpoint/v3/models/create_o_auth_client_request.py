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

from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from sailpoint.v3.models.access_type import AccessType
from sailpoint.v3.models.client_type import ClientType
from sailpoint.v3.models.grant_type import GrantType


class CreateOAuthClientRequest(BaseModel):
    """
    CreateOAuthClientRequest
    """
    business_name: Optional[StrictStr] = Field(
        None,
        alias="businessName",
        description="The name of the business the API Client should belong to")
    homepage_url: Optional[StrictStr] = Field(
        None,
        alias="homepageUrl",
        description=
        "The homepage URL associated with the owner of the API Client")
    name: Optional[StrictStr] = Field(
        ..., description="A human-readable name for the API Client")
    description: Optional[StrictStr] = Field(
        ..., description="A description of the API Client")
    access_token_validity_seconds: StrictInt = Field(
        ...,
        alias="accessTokenValiditySeconds",
        description=
        "The number of seconds an access token generated for this API Client is valid for"
    )
    refresh_token_validity_seconds: Optional[StrictInt] = Field(
        None,
        alias="refreshTokenValiditySeconds",
        description=
        "The number of seconds a refresh token generated for this API Client is valid for"
    )
    redirect_uris: Optional[conlist(StrictStr)] = Field(
        None,
        alias="redirectUris",
        description=
        "A list of the approved redirect URIs. Provide one or more URIs when assigning the AUTHORIZATION_CODE grant type to a new OAuth Client."
    )
    grant_types: Optional[conlist(GrantType)] = Field(
        ...,
        alias="grantTypes",
        description=
        "A list of OAuth 2.0 grant types this API Client can be used with")
    access_type: AccessType = Field(..., alias="accessType")
    type: Optional[ClientType] = None
    internal: Optional[StrictBool] = Field(
        None,
        description=
        "An indicator of whether the API Client can be used for requests internal within the product."
    )
    enabled: StrictBool = Field(
        ...,
        description="An indicator of whether the API Client is enabled for use"
    )
    strong_auth_supported: Optional[StrictBool] = Field(
        None,
        alias="strongAuthSupported",
        description=
        "An indicator of whether the API Client supports strong authentication"
    )
    claims_supported: Optional[StrictBool] = Field(
        None,
        alias="claimsSupported",
        description=
        "An indicator of whether the API Client supports the serialization of SAML claims when used with the authorization_code flow"
    )
    scope: Optional[conlist(StrictStr)] = Field(
        None,
        description=
        "Scopes of the API Client. If no scope is specified, the client will be created with the default scope \"sp:scopes:all\". This means the API Client will have all the rights of the owner who created it."
    )
    __properties = [
        "businessName", "homepageUrl", "name", "description",
        "accessTokenValiditySeconds", "refreshTokenValiditySeconds",
        "redirectUris", "grantTypes", "accessType", "type", "internal",
        "enabled", "strongAuthSupported", "claimsSupported", "scope"
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
    def from_json(cls, json_str: str) -> CreateOAuthClientRequest:
        """Create an instance of CreateOAuthClientRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if business_name (nullable) is None
        # and __fields_set__ contains the field
        if self.business_name is None and "business_name" in self.__fields_set__:
            _dict['businessName'] = None

        # set to None if homepage_url (nullable) is None
        # and __fields_set__ contains the field
        if self.homepage_url is None and "homepage_url" in self.__fields_set__:
            _dict['homepageUrl'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if redirect_uris (nullable) is None
        # and __fields_set__ contains the field
        if self.redirect_uris is None and "redirect_uris" in self.__fields_set__:
            _dict['redirectUris'] = None

        # set to None if grant_types (nullable) is None
        # and __fields_set__ contains the field
        if self.grant_types is None and "grant_types" in self.__fields_set__:
            _dict['grantTypes'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateOAuthClientRequest:
        """Create an instance of CreateOAuthClientRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateOAuthClientRequest.parse_obj(obj)

        _obj = CreateOAuthClientRequest.parse_obj({
            "business_name":
            obj.get("businessName"),
            "homepage_url":
            obj.get("homepageUrl"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "access_token_validity_seconds":
            obj.get("accessTokenValiditySeconds"),
            "refresh_token_validity_seconds":
            obj.get("refreshTokenValiditySeconds"),
            "redirect_uris":
            obj.get("redirectUris"),
            "grant_types":
            obj.get("grantTypes"),
            "access_type":
            obj.get("accessType"),
            "type":
            obj.get("type"),
            "internal":
            obj.get("internal"),
            "enabled":
            obj.get("enabled"),
            "strong_auth_supported":
            obj.get("strongAuthSupported"),
            "claims_supported":
            obj.get("claimsSupported"),
            "scope":
            obj.get("scope")
        })
        return _obj
