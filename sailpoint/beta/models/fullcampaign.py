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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.campaign_alert import CampaignAlert
from sailpoint.beta.models.fullcampaign_all_of_filter import FullcampaignAllOfFilter
from sailpoint.beta.models.fullcampaign_all_of_role_composition_campaign_info import FullcampaignAllOfRoleCompositionCampaignInfo
from sailpoint.beta.models.fullcampaign_all_of_search_campaign_info import FullcampaignAllOfSearchCampaignInfo
from sailpoint.beta.models.fullcampaign_all_of_source_owner_campaign_info import FullcampaignAllOfSourceOwnerCampaignInfo
from sailpoint.beta.models.fullcampaign_all_of_sources_with_orphan_entitlements import FullcampaignAllOfSourcesWithOrphanEntitlements
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Fullcampaign(BaseModel):
    """
    Fullcampaign
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Id of the campaign")
    name: StrictStr = Field(description="The campaign name. If this object is part of a template, special formatting applies; see the `/campaign-templates/{id}/generate` endpoint documentation for details.")
    description: StrictStr = Field(description="The campaign description. If this object is part of a template, special formatting applies; see the `/campaign-templates/{id}/generate` endpoint documentation for details.")
    deadline: Optional[datetime] = Field(default=None, description="The campaign's completion deadline.  This date must be in the future in order to activate the campaign.  If you try to activate a campaign with a deadline of today or in the past, you will receive a 400 error response.")
    type: StrictStr = Field(description="The type of campaign. Could be extended in the future.")
    email_notification_enabled: Optional[StrictBool] = Field(default=False, description="Enables email notification for this campaign", alias="emailNotificationEnabled")
    auto_revoke_allowed: Optional[StrictBool] = Field(default=False, description="Allows auto revoke for this campaign", alias="autoRevokeAllowed")
    recommendations_enabled: Optional[StrictBool] = Field(default=False, description="Enables IAI for this campaign. Accepts true even if the IAI product feature is off. If IAI is turned off then campaigns generated from this template will indicate false. The real value will then be returned if IAI is ever enabled for the org in the future.", alias="recommendationsEnabled")
    status: Optional[StrictStr] = Field(default=None, description="The campaign's current status.")
    correlated_status: Optional[Dict[str, Any]] = Field(default=None, description="The correlatedStatus of the campaign. Only SOURCE_OWNER campaigns can be Uncorrelated. An Uncorrelated certification campaign only includes Uncorrelated identities (An identity is uncorrelated if it has no accounts on an authoritative source).", alias="correlatedStatus")
    created: Optional[datetime] = Field(default=None, description="Created time of the campaign")
    total_certifications: Optional[StrictInt] = Field(default=None, description="The total number of certifications in this campaign.", alias="totalCertifications")
    completed_certifications: Optional[StrictInt] = Field(default=None, description="The number of completed certifications in this campaign.", alias="completedCertifications")
    alerts: Optional[List[CampaignAlert]] = Field(default=None, description="A list of errors and warnings that have accumulated.")
    modified: Optional[datetime] = Field(default=None, description="Modified time of the campaign")
    filter: Optional[FullcampaignAllOfFilter] = None
    sunset_comments_required: Optional[StrictBool] = Field(default=True, description="Determines if comments on sunset date changes are required.", alias="sunsetCommentsRequired")
    source_owner_campaign_info: Optional[FullcampaignAllOfSourceOwnerCampaignInfo] = Field(default=None, alias="sourceOwnerCampaignInfo")
    search_campaign_info: Optional[FullcampaignAllOfSearchCampaignInfo] = Field(default=None, alias="searchCampaignInfo")
    role_composition_campaign_info: Optional[FullcampaignAllOfRoleCompositionCampaignInfo] = Field(default=None, alias="roleCompositionCampaignInfo")
    sources_with_orphan_entitlements: Optional[List[FullcampaignAllOfSourcesWithOrphanEntitlements]] = Field(default=None, description="A list of sources in the campaign that contain \\\"orphan entitlements\\\" (entitlements without a corresponding Managed Attribute). An empty list indicates the campaign has no orphan entitlements. Null indicates there may be unknown orphan entitlements in the campaign (the campaign was created before this feature was implemented).", alias="sourcesWithOrphanEntitlements")
    mandatory_comment_requirement: Optional[StrictStr] = Field(default=None, description="Determines whether comments are required for decisions during certification reviews. You can require comments for all decisions, revoke-only decisions, or no decisions. By default, comments are not required for decisions.", alias="mandatoryCommentRequirement")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "deadline", "type", "emailNotificationEnabled", "autoRevokeAllowed", "recommendationsEnabled", "status", "correlatedStatus", "created", "totalCertifications", "completedCertifications", "alerts", "modified", "filter", "sunsetCommentsRequired", "sourceOwnerCampaignInfo", "searchCampaignInfo", "roleCompositionCampaignInfo", "sourcesWithOrphanEntitlements", "mandatoryCommentRequirement"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION'):
            raise ValueError("must be one of enum values ('MANAGER', 'SOURCE_OWNER', 'SEARCH', 'ROLE_COMPOSITION')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('PENDING', 'STAGED', 'CANCELING', 'ACTIVATING', 'ACTIVE', 'COMPLETING', 'COMPLETED', 'ERROR', 'ARCHIVED'):
            raise ValueError("must be one of enum values ('PENDING', 'STAGED', 'CANCELING', 'ACTIVATING', 'ACTIVE', 'COMPLETING', 'COMPLETED', 'ERROR', 'ARCHIVED')")
        return value

    @field_validator('correlated_status')
    def correlated_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CORRELATED', 'UNCORRELATED'):
            raise ValueError("must be one of enum values ('CORRELATED', 'UNCORRELATED')")
        return value

    @field_validator('mandatory_comment_requirement')
    def mandatory_comment_requirement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ALL_DECISIONS', 'REVOKE_ONLY_DECISIONS', 'NO_DECISIONS'):
            raise ValueError("must be one of enum values ('ALL_DECISIONS', 'REVOKE_ONLY_DECISIONS', 'NO_DECISIONS')")
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
        """Create an instance of Fullcampaign from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "status",
                "created",
                "total_certifications",
                "completed_certifications",
                "alerts",
                "modified",
                "sources_with_orphan_entitlements",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item in self.alerts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alerts'] = _items
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source_owner_campaign_info
        if self.source_owner_campaign_info:
            _dict['sourceOwnerCampaignInfo'] = self.source_owner_campaign_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_campaign_info
        if self.search_campaign_info:
            _dict['searchCampaignInfo'] = self.search_campaign_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role_composition_campaign_info
        if self.role_composition_campaign_info:
            _dict['roleCompositionCampaignInfo'] = self.role_composition_campaign_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sources_with_orphan_entitlements (list)
        _items = []
        if self.sources_with_orphan_entitlements:
            for _item in self.sources_with_orphan_entitlements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sourcesWithOrphanEntitlements'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Fullcampaign from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "deadline": obj.get("deadline"),
            "type": obj.get("type"),
            "emailNotificationEnabled": obj.get("emailNotificationEnabled") if obj.get("emailNotificationEnabled") is not None else False,
            "autoRevokeAllowed": obj.get("autoRevokeAllowed") if obj.get("autoRevokeAllowed") is not None else False,
            "recommendationsEnabled": obj.get("recommendationsEnabled") if obj.get("recommendationsEnabled") is not None else False,
            "status": obj.get("status"),
            "correlatedStatus": obj.get("correlatedStatus"),
            "created": obj.get("created"),
            "totalCertifications": obj.get("totalCertifications"),
            "completedCertifications": obj.get("completedCertifications"),
            "alerts": [CampaignAlert.from_dict(_item) for _item in obj.get("alerts")] if obj.get("alerts") is not None else None,
            "modified": obj.get("modified"),
            "filter": FullcampaignAllOfFilter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "sunsetCommentsRequired": obj.get("sunsetCommentsRequired") if obj.get("sunsetCommentsRequired") is not None else True,
            "sourceOwnerCampaignInfo": FullcampaignAllOfSourceOwnerCampaignInfo.from_dict(obj.get("sourceOwnerCampaignInfo")) if obj.get("sourceOwnerCampaignInfo") is not None else None,
            "searchCampaignInfo": FullcampaignAllOfSearchCampaignInfo.from_dict(obj.get("searchCampaignInfo")) if obj.get("searchCampaignInfo") is not None else None,
            "roleCompositionCampaignInfo": FullcampaignAllOfRoleCompositionCampaignInfo.from_dict(obj.get("roleCompositionCampaignInfo")) if obj.get("roleCompositionCampaignInfo") is not None else None,
            "sourcesWithOrphanEntitlements": [FullcampaignAllOfSourcesWithOrphanEntitlements.from_dict(_item) for _item in obj.get("sourcesWithOrphanEntitlements")] if obj.get("sourcesWithOrphanEntitlements") is not None else None,
            "mandatoryCommentRequirement": obj.get("mandatoryCommentRequirement")
        })
        return _obj


