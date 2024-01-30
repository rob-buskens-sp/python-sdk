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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.beta.models.campaign_template_owner_ref import CampaignTemplateOwnerRef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class CampaignTemplate(BaseModel):
    """
    Campaign Template
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="Id of the campaign template")
    name: StrictStr = Field(
        description=
        "This template's name. Has no bearing on generated campaigns' names.")
    description: StrictStr = Field(
        description=
        "This template's description. Has no bearing on generated campaigns' descriptions."
    )
    created: datetime = Field(description="Creation date of Campaign Template")
    modified: datetime = Field(
        description="Modification date of Campaign Template")
    scheduled: Optional[StrictBool] = Field(
        default=False,
        description="Indicates if this campaign template has been scheduled.")
    owner_ref: Optional[CampaignTemplateOwnerRef] = Field(default=None,
                                                          alias="ownerRef")
    deadline_duration: Optional[StrictStr] = Field(
        default=None,
        description=
        "The time period during which the campaign should be completed, formatted as an ISO-8601 Duration. When this template generates a campaign, the campaign's deadline will be the current date plus this duration. For example, if generation occurred on 2020-01-01 and this field was \"P2W\" (two weeks), the resulting campaign's deadline would be 2020-01-15 (the current date plus 14 days).",
        alias="deadlineDuration")
    campaign: Dict[str, Any] = Field(
        description=
        "This will hold campaign related information like name, description etc."
    )
    __properties: ClassVar[List[str]] = [
        "id", "name", "description", "created", "modified", "scheduled",
        "ownerRef", "deadlineDuration", "campaign"
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
        """Create an instance of CampaignTemplate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created",
                "modified",
                "scheduled",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of owner_ref
        if self.owner_ref:
            _dict['ownerRef'] = self.owner_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CampaignTemplate from a dict"""
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
            "scheduled":
            obj.get("scheduled")
            if obj.get("scheduled") is not None else False,
            "ownerRef":
            CampaignTemplateOwnerRef.from_dict(obj.get("ownerRef"))
            if obj.get("ownerRef") is not None else None,
            "deadlineDuration":
            obj.get("deadlineDuration"),
            "campaign":
            Campaign.from_dict(obj.get("campaign"))
            if obj.get("campaign") is not None else None
        })
        return _obj
