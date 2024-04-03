# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field

from sailpoint.beta.models.object_export_import_options import ObjectExportImportOptions
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ExportPayload(BaseModel):
    """
    ExportPayload
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Optional user defined description/name for export job.")
    exclude_types: Optional[List[StrictStr]] = Field(default=None, description="Object type names to be excluded from an sp-config export command.", alias="excludeTypes")
    include_types: Optional[List[StrictStr]] = Field(default=None, description="Object type names to be included in an sp-config export command. IncludeTypes takes precedence over excludeTypes.", alias="includeTypes")
    object_options: Optional[Dict[str, ObjectExportImportOptions]] = Field(default=None, description="Additional options targeting specific objects related to each item in the includeTypes field", alias="objectOptions")
    __properties: ClassVar[List[str]] = ["excludeTypes", "includeTypes", "objectOptions"]

    @field_validator('exclude_types')
    def exclude_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW'):
                raise ValueError("each list item must be one of ('ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW')")
        return value

    @field_validator('include_types')
    def include_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW'):
                raise ValueError("each list item must be one of ('ACCESS_PROFILE', 'ACCESS_REQUEST_CONFIG', 'ATTR_SYNC_SOURCE_CONFIG', 'AUTH_ORG', 'CAMPAIGN_FILTER', 'FORM_DEFINITION', 'GOVERNANCE_GROUP', 'IDENTITY_OBJECT_CONFIG', 'IDENTITY_PROFILE', 'LIFECYCLE_STATE', 'NOTIFICATION_TEMPLATE', 'PASSWORD_POLICY', 'PASSWORD_SYNC_GROUP', 'PUBLIC_IDENTITIES_CONFIG', 'ROLE', 'RULE', 'SEGMENT', 'SERVICE_DESK_INTEGRATION', 'SOD_POLICY', 'SOURCE', 'TAG', 'TRANSFORM', 'TRIGGER_SUBSCRIPTION', 'WORKFLOW')")
        return value

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
        """Create an instance of ExportPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in object_options (dict)
        _field_dict = {}
        if self.object_options:
            for _key in self.object_options:
                if self.object_options[_key]:
                    _field_dict[_key] = self.object_options[_key].to_dict()
            _dict['objectOptions'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ExportPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludeTypes": obj.get("excludeTypes"),
            "includeTypes": obj.get("includeTypes"),
            "objectOptions": dict(
                (_k, ObjectExportImportOptions.from_dict(_v))
                for _k, _v in obj.get("objectOptions").items()
            )
            if obj.get("objectOptions") is not None
            else None
        })
        return _obj


