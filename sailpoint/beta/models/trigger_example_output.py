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
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from sailpoint.beta.models.access_request_dynamic_approver1 import AccessRequestDynamicApprover1
from sailpoint.beta.models.access_request_pre_approval1 import AccessRequestPreApproval1
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

TRIGGEREXAMPLEOUTPUT_ONE_OF_SCHEMAS = [
    "AccessRequestDynamicApprover1", "AccessRequestPreApproval1"
]


class TriggerExampleOutput(BaseModel):
    """
    An example of the JSON payload that will be sent by the subscribed service to the trigger in response to an event.
    """
    # data type: AccessRequestDynamicApprover1
    oneof_schema_1_validator: Optional[AccessRequestDynamicApprover1] = None
    # data type: AccessRequestPreApproval1
    oneof_schema_2_validator: Optional[AccessRequestPreApproval1] = None
    if TYPE_CHECKING:
        actual_instance: Union[AccessRequestDynamicApprover1,
                               AccessRequestPreApproval1]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(TRIGGEREXAMPLEOUTPUT_ONE_OF_SCHEMAS,
                                      const=True)

    class Config:
        validate_assignment = True

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

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = TriggerExampleOutput.construct()
        error_messages = []
        match = 0
        # validate data type: AccessRequestDynamicApprover1
        if not isinstance(v, AccessRequestDynamicApprover1):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `AccessRequestDynamicApprover1`"
            )
        else:
            match += 1
        # validate data type: AccessRequestPreApproval1
        if not isinstance(v, AccessRequestPreApproval1):
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `AccessRequestPreApproval1`"
            )
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when setting `actual_instance` in TriggerExampleOutput with oneOf schemas: AccessRequestDynamicApprover1, AccessRequestPreApproval1. Details: "
                + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when setting `actual_instance` in TriggerExampleOutput with oneOf schemas: AccessRequestDynamicApprover1, AccessRequestPreApproval1. Details: "
                + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TriggerExampleOutput:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TriggerExampleOutput:
        """Returns the object represented by the json string"""
        instance = TriggerExampleOutput.construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into AccessRequestDynamicApprover1
        try:
            instance.actual_instance = AccessRequestDynamicApprover1.from_json(
                json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AccessRequestPreApproval1
        try:
            instance.actual_instance = AccessRequestPreApproval1.from_json(
                json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError(
                "Multiple matches found when deserializing the JSON string into TriggerExampleOutput with oneOf schemas: AccessRequestDynamicApprover1, AccessRequestPreApproval1. Details: "
                + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into TriggerExampleOutput with oneOf schemas: AccessRequestDynamicApprover1, AccessRequestPreApproval1. Details: "
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

    def to_dict(self) -> dict:
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
        return pprint.pformat(self.dict())
