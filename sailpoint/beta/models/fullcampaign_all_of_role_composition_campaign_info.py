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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from beta.models.fullcampaign_all_of_role_composition_campaign_info_remediator_ref import FullcampaignAllOfRoleCompositionCampaignInfoRemediatorRef
from beta.models.fullcampaign_all_of_search_campaign_info_reviewer import FullcampaignAllOfSearchCampaignInfoReviewer

class FullcampaignAllOfRoleCompositionCampaignInfo(BaseModel):
    """
    Optional configuration options for role composition campaigns.  # noqa: E501
    """
    reviewer: Optional[FullcampaignAllOfSearchCampaignInfoReviewer] = None
    role_ids: Optional[conlist(StrictStr)] = Field(None, alias="roleIds", description="Optional list of roles to include in this campaign. Only one of `roleIds` and `query` may be set; if neither are set, all roles are included.")
    remediator_ref: FullcampaignAllOfRoleCompositionCampaignInfoRemediatorRef = Field(..., alias="remediatorRef")
    query: Optional[StrictStr] = Field(None, description="Optional search query to scope this campaign to a set of roles. Only one of `roleIds` and `query` may be set; if neither are set, all roles are included.")
    description: Optional[StrictStr] = Field(None, description="Describes this role composition campaign. Intended for storing the query used, and possibly the number of roles selected/available.")
    __properties = ["reviewer", "roleIds", "remediatorRef", "query", "description"]

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
    def from_json(cls, json_str: str) -> FullcampaignAllOfRoleCompositionCampaignInfo:
        """Create an instance of FullcampaignAllOfRoleCompositionCampaignInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of reviewer
        if self.reviewer:
            _dict['reviewer'] = self.reviewer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remediator_ref
        if self.remediator_ref:
            _dict['remediatorRef'] = self.remediator_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FullcampaignAllOfRoleCompositionCampaignInfo:
        """Create an instance of FullcampaignAllOfRoleCompositionCampaignInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FullcampaignAllOfRoleCompositionCampaignInfo.parse_obj(obj)

        _obj = FullcampaignAllOfRoleCompositionCampaignInfo.parse_obj({
            "reviewer": FullcampaignAllOfSearchCampaignInfoReviewer.from_dict(obj.get("reviewer")) if obj.get("reviewer") is not None else None,
            "role_ids": obj.get("roleIds"),
            "remediator_ref": FullcampaignAllOfRoleCompositionCampaignInfoRemediatorRef.from_dict(obj.get("remediatorRef")) if obj.get("remediatorRef") is not None else None,
            "query": obj.get("query"),
            "description": obj.get("description")
        })
        return _obj


