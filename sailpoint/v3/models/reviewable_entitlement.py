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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.v3.models.data_access import DataAccess
from sailpoint.v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
from sailpoint.v3.models.reviewable_entitlement_account import ReviewableEntitlementAccount
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ReviewableEntitlement(BaseModel):
    """
    ReviewableEntitlement
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The id for the entitlement")
    name: Optional[StrictStr] = Field(default=None, description="The name of the entitlement")
    description: Optional[StrictStr] = Field(default=None, description="Information about the entitlement")
    privileged: Optional[StrictBool] = Field(default=False, description="Indicates if the entitlement is a privileged entitlement")
    owner: Optional[IdentityReferenceWithNameAndEmail] = None
    attribute_name: Optional[StrictStr] = Field(default=None, description="The name of the attribute on the source", alias="attributeName")
    attribute_value: Optional[StrictStr] = Field(default=None, description="The value of the attribute on the source", alias="attributeValue")
    source_schema_object_type: Optional[StrictStr] = Field(default=None, description="The schema object type on the source used to represent the entitlement and its attributes", alias="sourceSchemaObjectType")
    source_name: Optional[StrictStr] = Field(default=None, description="The name of the source for which this entitlement belongs", alias="sourceName")
    source_type: Optional[StrictStr] = Field(default=None, description="The type of the source for which the entitlement belongs", alias="sourceType")
    source_id: Optional[StrictStr] = Field(default=None, description="The ID of the source for which the entitlement belongs", alias="sourceId")
    has_permissions: Optional[StrictBool] = Field(default=False, description="Indicates if the entitlement has permissions", alias="hasPermissions")
    is_permission: Optional[StrictBool] = Field(default=False, description="Indicates if the entitlement is a representation of an account permission", alias="isPermission")
    revocable: Optional[StrictBool] = Field(default=False, description="Indicates whether the entitlement can be revoked")
    cloud_governed: Optional[StrictBool] = Field(default=False, description="True if the entitlement is cloud governed", alias="cloudGoverned")
    contains_data_access: Optional[StrictBool] = Field(default=False, description="True if the entitlement has DAS data", alias="containsDataAccess")
    data_access: Optional[DataAccess] = Field(default=None, alias="dataAccess")
    account: Optional[ReviewableEntitlementAccount] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "privileged", "owner", "attributeName", "attributeValue", "sourceSchemaObjectType", "sourceName", "sourceType", "sourceId", "hasPermissions", "isPermission", "revocable", "cloudGoverned", "containsDataAccess", "dataAccess", "account"]

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
        """Create an instance of ReviewableEntitlement from a JSON string"""
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
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if owner (nullable) is None
        # and model_fields_set contains the field
        if self.owner is None and "owner" in self.model_fields_set:
            _dict['owner'] = None

        # set to None if data_access (nullable) is None
        # and model_fields_set contains the field
        if self.data_access is None and "data_access" in self.model_fields_set:
            _dict['dataAccess'] = None

        # set to None if account (nullable) is None
        # and model_fields_set contains the field
        if self.account is None and "account" in self.model_fields_set:
            _dict['account'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ReviewableEntitlement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "privileged": obj.get("privileged") if obj.get("privileged") is not None else False,
            "owner": IdentityReferenceWithNameAndEmail.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "attributeName": obj.get("attributeName"),
            "attributeValue": obj.get("attributeValue"),
            "sourceSchemaObjectType": obj.get("sourceSchemaObjectType"),
            "sourceName": obj.get("sourceName"),
            "sourceType": obj.get("sourceType"),
            "sourceId": obj.get("sourceId"),
            "hasPermissions": obj.get("hasPermissions") if obj.get("hasPermissions") is not None else False,
            "isPermission": obj.get("isPermission") if obj.get("isPermission") is not None else False,
            "revocable": obj.get("revocable") if obj.get("revocable") is not None else False,
            "cloudGoverned": obj.get("cloudGoverned") if obj.get("cloudGoverned") is not None else False,
            "containsDataAccess": obj.get("containsDataAccess") if obj.get("containsDataAccess") is not None else False,
            "dataAccess": DataAccess.from_dict(obj.get("dataAccess")) if obj.get("dataAccess") is not None else None,
            "account": ReviewableEntitlementAccount.from_dict(obj.get("account")) if obj.get("account") is not None else None
        })
        return _obj


