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
from sailpoint.v3.models.data_access import DataAccess
from sailpoint.v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
from sailpoint.v3.models.reviewable_entitlement_account import ReviewableEntitlementAccount


class ReviewableEntitlement(BaseModel):
    """
    ReviewableEntitlement
    """
    id: Optional[StrictStr] = Field(None,
                                    description="The id for the entitlement")
    name: Optional[StrictStr] = Field(
        None, description="The name of the entitlement")
    description: Optional[StrictStr] = Field(
        None, description="Information about the entitlement")
    privileged: Optional[StrictBool] = Field(
        False,
        description="Indicates if the entitlement is a privileged entitlement")
    owner: Optional[IdentityReferenceWithNameAndEmail] = None
    attribute_name: Optional[StrictStr] = Field(
        None,
        alias="attributeName",
        description="The name of the attribute on the source")
    attribute_value: Optional[StrictStr] = Field(
        None,
        alias="attributeValue",
        description="The value of the attribute on the source")
    source_schema_object_type: Optional[StrictStr] = Field(
        None,
        alias="sourceSchemaObjectType",
        description=
        "The schema object type on the source used to represent the entitlement and its attributes"
    )
    source_name: Optional[StrictStr] = Field(
        None,
        alias="sourceName",
        description="The name of the source for which this entitlement belongs"
    )
    source_type: Optional[StrictStr] = Field(
        None,
        alias="sourceType",
        description="The type of the source for which the entitlement belongs")
    source_id: Optional[StrictStr] = Field(
        None,
        alias="sourceId",
        description="The ID of the source for which the entitlement belongs")
    has_permissions: Optional[StrictBool] = Field(
        False,
        alias="hasPermissions",
        description="Indicates if the entitlement has permissions")
    is_permission: Optional[StrictBool] = Field(
        False,
        alias="isPermission",
        description=
        "Indicates if the entitlement is a representation of an account permission"
    )
    revocable: Optional[StrictBool] = Field(
        False, description="Indicates whether the entitlement can be revoked")
    cloud_governed: Optional[StrictBool] = Field(
        False,
        alias="cloudGoverned",
        description="True if the entitlement is cloud governed")
    contains_data_access: Optional[StrictBool] = Field(
        False,
        alias="containsDataAccess",
        description="True if the entitlement has DAS data")
    data_access: Optional[DataAccess] = Field(None, alias="dataAccess")
    account: Optional[ReviewableEntitlementAccount] = None
    __properties = [
        "id", "name", "description", "privileged", "owner", "attributeName",
        "attributeValue", "sourceSchemaObjectType", "sourceName", "sourceType",
        "sourceId", "hasPermissions", "isPermission", "revocable",
        "cloudGoverned", "containsDataAccess", "dataAccess", "account"
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
    def from_json(cls, json_str: str) -> ReviewableEntitlement:
        """Create an instance of ReviewableEntitlement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_access
        if self.data_access:
            _dict['dataAccess'] = self.data_access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if owner (nullable) is None
        # and __fields_set__ contains the field
        if self.owner is None and "owner" in self.__fields_set__:
            _dict['owner'] = None

        # set to None if data_access (nullable) is None
        # and __fields_set__ contains the field
        if self.data_access is None and "data_access" in self.__fields_set__:
            _dict['dataAccess'] = None

        # set to None if account (nullable) is None
        # and __fields_set__ contains the field
        if self.account is None and "account" in self.__fields_set__:
            _dict['account'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReviewableEntitlement:
        """Create an instance of ReviewableEntitlement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ReviewableEntitlement.parse_obj(obj)

        _obj = ReviewableEntitlement.parse_obj({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "privileged":
            obj.get("privileged")
            if obj.get("privileged") is not None else False,
            "owner":
            IdentityReferenceWithNameAndEmail.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "attribute_name":
            obj.get("attributeName"),
            "attribute_value":
            obj.get("attributeValue"),
            "source_schema_object_type":
            obj.get("sourceSchemaObjectType"),
            "source_name":
            obj.get("sourceName"),
            "source_type":
            obj.get("sourceType"),
            "source_id":
            obj.get("sourceId"),
            "has_permissions":
            obj.get("hasPermissions")
            if obj.get("hasPermissions") is not None else False,
            "is_permission":
            obj.get("isPermission")
            if obj.get("isPermission") is not None else False,
            "revocable":
            obj.get("revocable")
            if obj.get("revocable") is not None else False,
            "cloud_governed":
            obj.get("cloudGoverned")
            if obj.get("cloudGoverned") is not None else False,
            "contains_data_access":
            obj.get("containsDataAccess")
            if obj.get("containsDataAccess") is not None else False,
            "data_access":
            DataAccess.from_dict(obj.get("dataAccess"))
            if obj.get("dataAccess") is not None else None,
            "account":
            ReviewableEntitlementAccount.from_dict(obj.get("account"))
            if obj.get("account") is not None else None
        })
        return _obj
