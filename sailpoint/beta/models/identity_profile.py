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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from sailpoint.beta.models.identity_attribute_config import IdentityAttributeConfig
from sailpoint.beta.models.identity_exception_report_reference import IdentityExceptionReportReference
from sailpoint.beta.models.identity_profile_all_of_authoritative_source import IdentityProfileAllOfAuthoritativeSource
from sailpoint.beta.models.identity_profile_all_of_owner import IdentityProfileAllOfOwner


class IdentityProfile(BaseModel):
    """
    IdentityProfile
    """
    id: Optional[StrictStr] = Field(
        None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(..., description="Name of the Object")
    created: Optional[datetime] = Field(
        None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(
        None, description="Last modification date of the Object")
    description: Optional[StrictStr] = Field(
        None, description="The description of the Identity Profile.")
    owner: Optional[IdentityProfileAllOfOwner] = None
    priority: Optional[StrictInt] = Field(
        None, description="The priority for an Identity Profile.")
    authoritative_source: IdentityProfileAllOfAuthoritativeSource = Field(
        ..., alias="authoritativeSource")
    identity_refresh_required: Optional[StrictBool] = Field(
        False,
        alias="identityRefreshRequired",
        description=
        "True if a identity refresh is needed. Typically triggered when a change on the source has been made"
    )
    identity_count: Optional[StrictInt] = Field(
        None,
        alias="identityCount",
        description=
        "The number of identities that belong to the Identity Profile.")
    identity_attribute_config: Optional[IdentityAttributeConfig] = Field(
        None, alias="identityAttributeConfig")
    identity_exception_report_reference: Optional[
        IdentityExceptionReportReference] = Field(
            None, alias="identityExceptionReportReference")
    has_time_based_attr: Optional[StrictBool] = Field(
        True,
        alias="hasTimeBasedAttr",
        description=
        "Indicates the value of requiresPeriodicRefresh attribute for the Identity Profile."
    )
    __properties = [
        "id", "name", "created", "modified", "description", "owner",
        "priority", "authoritativeSource", "identityRefreshRequired",
        "identityCount", "identityAttributeConfig",
        "identityExceptionReportReference", "hasTimeBasedAttr"
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
    def from_json(cls, json_str: str) -> IdentityProfile:
        """Create an instance of IdentityProfile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                              "id",
                              "created",
                              "modified",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authoritative_source
        if self.authoritative_source:
            _dict['authoritativeSource'] = self.authoritative_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of identity_attribute_config
        if self.identity_attribute_config:
            _dict[
                'identityAttributeConfig'] = self.identity_attribute_config.to_dict(
                )
        # override the default output from pydantic by calling `to_dict()` of identity_exception_report_reference
        if self.identity_exception_report_reference:
            _dict[
                'identityExceptionReportReference'] = self.identity_exception_report_reference.to_dict(
                )
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if identity_exception_report_reference (nullable) is None
        # and __fields_set__ contains the field
        if self.identity_exception_report_reference is None and "identity_exception_report_reference" in self.__fields_set__:
            _dict['identityExceptionReportReference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityProfile:
        """Create an instance of IdentityProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdentityProfile.parse_obj(obj)

        _obj = IdentityProfile.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "description":
            obj.get("description"),
            "owner":
            IdentityProfileAllOfOwner.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "priority":
            obj.get("priority"),
            "authoritative_source":
            IdentityProfileAllOfAuthoritativeSource.from_dict(
                obj.get("authoritativeSource"))
            if obj.get("authoritativeSource") is not None else None,
            "identity_refresh_required":
            obj.get("identityRefreshRequired")
            if obj.get("identityRefreshRequired") is not None else False,
            "identity_count":
            obj.get("identityCount"),
            "identity_attribute_config":
            IdentityAttributeConfig.from_dict(
                obj.get("identityAttributeConfig"))
            if obj.get("identityAttributeConfig") is not None else None,
            "identity_exception_report_reference":
            IdentityExceptionReportReference.from_dict(
                obj.get("identityExceptionReportReference")) if
            obj.get("identityExceptionReportReference") is not None else None,
            "has_time_based_attr":
            obj.get("hasTimeBasedAttr")
            if obj.get("hasTimeBasedAttr") is not None else True
        })
        return _obj
