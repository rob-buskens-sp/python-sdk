# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from sailpoint.beta.models.campaign import Campaign
from sailpoint.beta.models.slimcampaign import Slimcampaign
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

GETACTIVECAMPAIGNS200RESPONSEINNER_ONE_OF_SCHEMAS = [
    "Campaign", "Slimcampaign"
]


class GetActiveCampaigns200ResponseInner(BaseModel):
    """
    GetActiveCampaigns200ResponseInner
    """
    # data type: Slimcampaign
    oneof_schema_1_validator: Optional[Slimcampaign] = None
    # data type: Campaign
    oneof_schema_2_validator: Optional[Campaign] = None
    actual_instance: Optional[Union[Campaign, Slimcampaign]] = None
    one_of_schemas: List[str] = Literal["Campaign", "Slimcampaign"]

    model_config = {"validate_assignment": True}

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError(
                    "If a position argument is used, only 1 is allowed to set `actual_instance`"
                )
            if kwargs:
                raise ValueError(
                    "If a position argument is used, keyword arguments cannot be used."
                )
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetActiveCampaigns200ResponseInner.model_construct()
        error_messages = []
        match = 0
        # validate data type: Slimcampaign
        if not isinstance(v, Slimcampaign):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `Slimcampaign`")
        else:
            match += 1
        # validate data type: Campaign
        if not isinstance(v, Campaign):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `Campaign`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when setting `actual_instance` in GetActiveCampaigns200ResponseInner with oneOf schemas: Campaign, Slimcampaign. Details: "
                + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when setting `actual_instance` in GetActiveCampaigns200ResponseInner with oneOf schemas: Campaign, Slimcampaign. Details: "
                + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into Slimcampaign
        try:
            instance.actual_instance = Slimcampaign.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Campaign
        try:
            instance.actual_instance = Campaign.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when deserializing the JSON string into GetActiveCampaigns200ResponseInner with oneOf schemas: Campaign, Slimcampaign. Details: "
                + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into GetActiveCampaigns200ResponseInner with oneOf schemas: Campaign, Slimcampaign. Details: "
                + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
