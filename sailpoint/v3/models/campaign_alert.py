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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from v3.models.error_message_dto import ErrorMessageDto

class CampaignAlert(BaseModel):
    """
    CampaignAlert
    """
    level: Optional[StrictStr] = Field(None, description="Denotes the level of the message")
    localizations: Optional[conlist(ErrorMessageDto)] = None
    __properties = ["level", "localizations"]

    @validator('level')
    def level_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ERROR', 'WARN', 'INFO'):
            raise ValueError("must be one of enum values ('ERROR', 'WARN', 'INFO')")
        return value

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
    def from_json(cls, json_str: str) -> CampaignAlert:
        """Create an instance of CampaignAlert from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in localizations (list)
        _items = []
        if self.localizations:
            for _item in self.localizations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['localizations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CampaignAlert:
        """Create an instance of CampaignAlert from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CampaignAlert.parse_obj(obj)

        _obj = CampaignAlert.parse_obj({
            "level": obj.get("level"),
            "localizations": [ErrorMessageDto.from_dict(_item) for _item in obj.get("localizations")] if obj.get("localizations") is not None else None
        })
        return _obj


