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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from beta.models.event_bridge_config import EventBridgeConfig
from beta.models.http_config import HttpConfig
from beta.models.subscription_type import SubscriptionType

class SubscriptionPostRequest(BaseModel):
    """
    SubscriptionPostRequest
    """
    name: StrictStr = Field(..., description="Subscription name.")
    description: Optional[StrictStr] = Field(None, description="Subscription description.")
    trigger_id: StrictStr = Field(..., alias="triggerId", description="ID of trigger subscribed to.")
    type: SubscriptionType = Field(...)
    response_deadline: Optional[StrictStr] = Field('PT1H', alias="responseDeadline", description="Deadline for completing REQUEST_RESPONSE trigger invocation, represented in ISO-8601 duration format.")
    http_config: Optional[HttpConfig] = Field(None, alias="httpConfig")
    event_bridge_config: Optional[EventBridgeConfig] = Field(None, alias="eventBridgeConfig")
    enabled: Optional[StrictBool] = Field(True, description="Whether subscription should receive real-time trigger invocations or not.  Test trigger invocations are always enabled regardless of this option.")
    filter: Optional[StrictStr] = Field(None, description="JSONPath filter to conditionally invoke trigger when expression evaluates to true.")
    __properties = ["name", "description", "triggerId", "type", "responseDeadline", "httpConfig", "eventBridgeConfig", "enabled", "filter"]

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
    def from_json(cls, json_str: str) -> SubscriptionPostRequest:
        """Create an instance of SubscriptionPostRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of http_config
        if self.http_config:
            _dict['httpConfig'] = self.http_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event_bridge_config
        if self.event_bridge_config:
            _dict['eventBridgeConfig'] = self.event_bridge_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SubscriptionPostRequest:
        """Create an instance of SubscriptionPostRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SubscriptionPostRequest.parse_obj(obj)

        _obj = SubscriptionPostRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "trigger_id": obj.get("triggerId"),
            "type": obj.get("type"),
            "response_deadline": obj.get("responseDeadline") if obj.get("responseDeadline") is not None else 'PT1H',
            "http_config": HttpConfig.from_dict(obj.get("httpConfig")) if obj.get("httpConfig") is not None else None,
            "event_bridge_config": EventBridgeConfig.from_dict(obj.get("eventBridgeConfig")) if obj.get("eventBridgeConfig") is not None else None,
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "filter": obj.get("filter")
        })
        return _obj


