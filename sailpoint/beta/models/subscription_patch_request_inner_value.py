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

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, ValidationError, field_validator
from sailpoint.beta.models.subscription_patch_request_inner_value_any_of_inner import SubscriptionPatchRequestInnerValueAnyOfInner
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

SUBSCRIPTIONPATCHREQUESTINNERVALUE_ANY_OF_SCHEMAS = ["List[SubscriptionPatchRequestInnerValueAnyOfInner]", "int", "object", "str"]

class SubscriptionPatchRequestInnerValue(BaseModel):
    """
    The value to be used for the operation, required for \"add\" and \"replace\" operations
    """

    # data type: str
    anyof_schema_1_validator: Optional[StrictStr] = None
    # data type: int
    anyof_schema_2_validator: Optional[StrictInt] = None
    # data type: object
    anyof_schema_3_validator: Optional[Dict[str, Any]] = None
    # data type: List[SubscriptionPatchRequestInnerValueAnyOfInner]
    anyof_schema_4_validator: Optional[List[SubscriptionPatchRequestInnerValueAnyOfInner]] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[List[SubscriptionPatchRequestInnerValueAnyOfInner], int, object, str]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[SUBSCRIPTIONPATCHREQUESTINNERVALUE_ANY_OF_SCHEMAS]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = SubscriptionPatchRequestInnerValue.model_construct()
        error_messages = []
        # validate data type: str
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: int
        try:
            instance.anyof_schema_2_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: object
        try:
            instance.anyof_schema_3_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[SubscriptionPatchRequestInnerValueAnyOfInner]
        try:
            instance.anyof_schema_4_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in SubscriptionPatchRequestInnerValue with anyOf schemas: List[SubscriptionPatchRequestInnerValueAnyOfInner], int, object, str. Details: " + ", ".join(error_messages))
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
        # deserialize data into str
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into int
        try:
            # validation
            instance.anyof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_2_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into object
        try:
            # validation
            instance.anyof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_3_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[SubscriptionPatchRequestInnerValueAnyOfInner]
        try:
            # validation
            instance.anyof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_4_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SubscriptionPatchRequestInnerValue with anyOf schemas: List[SubscriptionPatchRequestInnerValueAnyOfInner], int, object, str. Details: " + ", ".join(error_messages))
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
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


