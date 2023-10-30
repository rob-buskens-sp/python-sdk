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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from beta.models.entitlement_source import EntitlementSource
from beta.models.manually_updated_fields_dto import ManuallyUpdatedFieldsDTO
from beta.models.owner_reference_dto import OwnerReferenceDto
from beta.models.permission_dto import PermissionDto

class Entitlement(BaseModel):
    """
    Entitlement
    """
    id: Optional[StrictStr] = Field(None, description="The entitlement id")
    name: Optional[StrictStr] = Field(None, description="The entitlement name")
    created: Optional[datetime] = Field(None, description="Time when the entitlement was created")
    modified: Optional[datetime] = Field(None, description="Time when the entitlement was last modified")
    attribute: Optional[StrictStr] = Field(None, description="The entitlement attribute name")
    value: Optional[StrictStr] = Field(None, description="The value of the entitlement")
    source_schema_object_type: Optional[StrictStr] = Field(None, alias="sourceSchemaObjectType", description="The object type of the entitlement from the source schema")
    privileged: Optional[StrictBool] = Field(False, description="True if the entitlement is privileged")
    cloud_governed: Optional[StrictBool] = Field(False, alias="cloudGoverned", description="True if the entitlement is cloud governed")
    description: Optional[StrictStr] = Field(None, description="The description of the entitlement")
    requestable: Optional[StrictBool] = Field(False, description="True if the entitlement is requestable")
    attributes: Optional[Dict[str, Any]] = Field(None, description="A map of free-form key-value pairs from the source system")
    source: Optional[EntitlementSource] = None
    owner: Optional[OwnerReferenceDto] = None
    direct_permissions: Optional[conlist(PermissionDto)] = Field(None, alias="directPermissions")
    segments: Optional[conlist(StrictStr)] = Field(None, description="List of IDs of segments, if any, to which this Entitlement is assigned.")
    manually_updated_fields: Optional[ManuallyUpdatedFieldsDTO] = Field(None, alias="manuallyUpdatedFields")
    __properties = ["id", "name", "created", "modified", "attribute", "value", "sourceSchemaObjectType", "privileged", "cloudGoverned", "description", "requestable", "attributes", "source", "owner", "directPermissions", "segments", "manuallyUpdatedFields"]

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
    def from_json(cls, json_str: str) -> Entitlement:
        """Create an instance of Entitlement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in direct_permissions (list)
        _items = []
        if self.direct_permissions:
            for _item in self.direct_permissions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['directPermissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of manually_updated_fields
        if self.manually_updated_fields:
            _dict['manuallyUpdatedFields'] = self.manually_updated_fields.to_dict()
        # set to None if segments (nullable) is None
        # and __fields_set__ contains the field
        if self.segments is None and "segments" in self.__fields_set__:
            _dict['segments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Entitlement:
        """Create an instance of Entitlement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Entitlement.parse_obj(obj)

        _obj = Entitlement.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "attribute": obj.get("attribute"),
            "value": obj.get("value"),
            "source_schema_object_type": obj.get("sourceSchemaObjectType"),
            "privileged": obj.get("privileged") if obj.get("privileged") is not None else False,
            "cloud_governed": obj.get("cloudGoverned") if obj.get("cloudGoverned") is not None else False,
            "description": obj.get("description"),
            "requestable": obj.get("requestable") if obj.get("requestable") is not None else False,
            "attributes": obj.get("attributes"),
            "source": EntitlementSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "owner": OwnerReferenceDto.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "direct_permissions": [PermissionDto.from_dict(_item) for _item in obj.get("directPermissions")] if obj.get("directPermissions") is not None else None,
            "segments": obj.get("segments"),
            "manually_updated_fields": ManuallyUpdatedFieldsDTO.from_dict(obj.get("manuallyUpdatedFields")) if obj.get("manuallyUpdatedFields") is not None else None
        })
        return _obj


