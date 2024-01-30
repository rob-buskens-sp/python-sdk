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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.campaign_generated_campaign_campaign_owner import CampaignGeneratedCampaignCampaignOwner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CampaignGeneratedCampaign(BaseModel):
    """
    Details about the campaign that was generated.
    """ # noqa: E501
    id: StrictStr = Field(description="The unique ID of the campaign.")
    name: StrictStr = Field(description="Human friendly name of the campaign.")
    description: StrictStr = Field(
        description="Extended description of the campaign.")
    created: datetime = Field(
        description="The date and time the campaign was created.")
    modified: Optional[StrictStr] = Field(
        default=None,
        description="The date and time the campaign was last modified.")
    deadline: Optional[StrictStr] = Field(
        default=None,
        description="The date and time when the campaign must be finished by.")
    type: Dict[str, Any] = Field(
        description="The type of campaign that was generated.")
    campaign_owner: CampaignGeneratedCampaignCampaignOwner = Field(
        alias="campaignOwner")
    status: Dict[str, Any] = Field(
        description="The current status of the campaign.")
    __properties: ClassVar[List[str]] = [
        "id", "name", "description", "created", "modified", "deadline", "type",
        "campaignOwner", "status"
    ]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MANAGER', 'SOURCE_OWNER', 'SEARCH',
                         'ROLE_COMPOSITION'):
            raise ValueError(
                "must be one of enum values ('MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION')"
            )
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('STAGED', 'ACTIVATING', 'ACTIVE'):
            raise ValueError(
                "must be one of enum values ('STAGED', 'ACTIVATING', 'ACTIVE')"
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
        """Create an instance of CampaignGeneratedCampaign from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of campaign_owner
        if self.campaign_owner:
            _dict['campaignOwner'] = self.campaign_owner.to_dict()
        # set to None if modified (nullable) is None
        # and model_fields_set contains the field
        if self.modified is None and "modified" in self.model_fields_set:
            _dict['modified'] = None

        # set to None if deadline (nullable) is None
        # and model_fields_set contains the field
        if self.deadline is None and "deadline" in self.model_fields_set:
            _dict['deadline'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignGeneratedCampaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "name":
            obj.get("name"),
            "description":
            obj.get("description"),
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "deadline":
            obj.get("deadline"),
            "type":
            obj.get("type"),
            "campaignOwner":
            CampaignGeneratedCampaignCampaignOwner.from_dict(
                obj.get("campaignOwner"))
            if obj.get("campaignOwner") is not None else None,
            "status":
            obj.get("status")
        })
        return _obj
