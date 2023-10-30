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
from beta.models.campaign_reference import CampaignReference
from beta.models.certification_phase import CertificationPhase
from beta.models.reassignment import Reassignment
from beta.models.reviewer import Reviewer

class CertificationDto(BaseModel):
    """
    CertificationDto
    """
    campaign_ref: CampaignReference = Field(..., alias="campaignRef")
    phase: CertificationPhase = Field(...)
    due: datetime = Field(..., description="The due date of the certification.")
    signed: datetime = Field(..., description="The date the reviewer signed off on the certification.")
    reviewer: Reviewer = Field(...)
    reassignment: Optional[Reassignment] = None
    has_errors: StrictBool = Field(..., alias="hasErrors", description="Indicates it the certification has any errors.")
    error_message: Optional[StrictStr] = Field(None, alias="errorMessage", description="A message indicating what the error is.")
    completed: StrictBool = Field(..., description="Indicates if all certification decisions have been made.")
    decisions_made: StrictInt = Field(..., alias="decisionsMade", description="The number of approve/revoke/acknowledge decisions that have been made by the reviewer.")
    decisions_total: StrictInt = Field(..., alias="decisionsTotal", description="The total number of approve/revoke/acknowledge decisions for the certification.")
    entities_completed: StrictInt = Field(..., alias="entitiesCompleted", description="The number of entities (identities, access profiles, roles, etc.) for which all decisions have been made and are complete.")
    entities_total: StrictInt = Field(..., alias="entitiesTotal", description="The total number of entities (identities, access profiles, roles, etc.) in the certification, both complete and incomplete.")
    __properties = ["campaignRef", "phase", "due", "signed", "reviewer", "reassignment", "hasErrors", "errorMessage", "completed", "decisionsMade", "decisionsTotal", "entitiesCompleted", "entitiesTotal"]

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
    def from_json(cls, json_str: str) -> CertificationDto:
        """Create an instance of CertificationDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of campaign_ref
        if self.campaign_ref:
            _dict['campaignRef'] = self.campaign_ref.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reviewer
        if self.reviewer:
            _dict['reviewer'] = self.reviewer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reassignment
        if self.reassignment:
            _dict['reassignment'] = self.reassignment.to_dict()
        # set to None if error_message (nullable) is None
        # and __fields_set__ contains the field
        if self.error_message is None and "error_message" in self.__fields_set__:
            _dict['errorMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CertificationDto:
        """Create an instance of CertificationDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CertificationDto.parse_obj(obj)

        _obj = CertificationDto.parse_obj({
            "campaign_ref": CampaignReference.from_dict(obj.get("campaignRef")) if obj.get("campaignRef") is not None else None,
            "phase": obj.get("phase"),
            "due": obj.get("due"),
            "signed": obj.get("signed"),
            "reviewer": Reviewer.from_dict(obj.get("reviewer")) if obj.get("reviewer") is not None else None,
            "reassignment": Reassignment.from_dict(obj.get("reassignment")) if obj.get("reassignment") is not None else None,
            "has_errors": obj.get("hasErrors"),
            "error_message": obj.get("errorMessage"),
            "completed": obj.get("completed"),
            "decisions_made": obj.get("decisionsMade"),
            "decisions_total": obj.get("decisionsTotal"),
            "entities_completed": obj.get("entitiesCompleted"),
            "entities_total": obj.get("entitiesTotal")
        })
        return _obj


