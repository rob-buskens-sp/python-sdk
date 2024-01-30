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
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CampaignReference(BaseModel):
    """
    CampaignReference
    """

  # noqa: E501
    id: StrictStr = Field(description="The unique ID of the campaign.")
    name: StrictStr = Field(description="The name of the campaign.")
    type: StrictStr = Field(
        description="The type of object that is being referenced.")
    campaign_type: StrictStr = Field(description="The type of the campaign.",
                                     alias="campaignType")
    description: Optional[StrictStr] = Field(
        description=
        "The description of the campaign set by the admin who created it.")
    correlated_status: Dict[str, Any] = Field(
        description=
        "The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source).",
        alias="correlatedStatus")
    mandatory_comment_requirement: StrictStr = Field(
        description=
        "Determines whether comments are required for decisions during certification reviews. You can require comments for all decisions, revoke-only decisions, or no decisions. By default, comments are not required for decisions.",
        alias="mandatoryCommentRequirement")
    __properties: ClassVar[List[str]] = [
        "id", "name", "type", "campaignType", "description",
        "correlatedStatus", "mandatoryCommentRequirement"
    ]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CAMPAIGN'):
            raise ValueError("must be one of enum values ('CAMPAIGN')")
        return value

    @field_validator('campaign_type')
    def campaign_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MANAGER', 'SOURCE_OWNER', 'SEARCH'):
            raise ValueError(
                "must be one of enum values ('MANAGER', 'SOURCE_OWNER', 'SEARCH')"
            )
        return value

    @field_validator('correlated_status')
    def correlated_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CORRELATED', 'UNCORRELATED'):
            raise ValueError(
                "must be one of enum values ('CORRELATED', 'UNCORRELATED')")
        return value

    @field_validator('mandatory_comment_requirement')
    def mandatory_comment_requirement_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('ALL_DECISIONS', 'REVOKE_ONLY_DECISIONS',
                         'NO_DECISIONS'):
            raise ValueError(
                "must be one of enum values ('ALL_DECISIONS', 'REVOKE_ONLY_DECISIONS', 'NO_DECISIONS')"
            )
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
        """Create an instance of CampaignReference from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "type":
            obj.get("type"),
            "campaignType":
            obj.get("campaignType"),
            "description":
            obj.get("description"),
            "correlatedStatus":
            obj.get("correlatedStatus"),
            "mandatoryCommentRequirement":
            obj.get("mandatoryCommentRequirement")
        })
        return _obj
