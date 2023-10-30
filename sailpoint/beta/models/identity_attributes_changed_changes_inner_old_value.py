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
from pydantic import BaseModel, Field, StrictBool, StrictStr, ValidationError, conlist, validator
from beta.models.identity_attributes_changed_changes_inner_old_value_one_of_value import IdentityAttributesChangedChangesInnerOldValueOneOfValue
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

IDENTITYATTRIBUTESCHANGEDCHANGESINNEROLDVALUE_ONE_OF_SCHEMAS = ["Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue]", "List[str]", "bool", "str"]

class IdentityAttributesChangedChangesInnerOldValue(BaseModel):
    """
    The value of the identity attribute before it changed.
    """
    # data type: str
    oneof_schema_1_validator: Optional[StrictStr] = None
    # data type: bool
    oneof_schema_2_validator: Optional[StrictBool] = None
    # data type: List[str]
    oneof_schema_3_validator: Optional[conlist(StrictStr)] = None
    # data type: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue]
    oneof_schema_4_validator: Optional[Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue]] = None
    if TYPE_CHECKING:
        actual_instance: Union[Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue], List[str], bool, str]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(IDENTITYATTRIBUTESCHANGEDCHANGESINNEROLDVALUE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = IdentityAttributesChangedChangesInnerOldValue.construct()
        error_messages = []
        match = 0
        # validate data type: str
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: bool
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: List[str]
        try:
            instance.oneof_schema_3_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue]
        try:
            instance.oneof_schema_4_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in IdentityAttributesChangedChangesInnerOldValue with oneOf schemas: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue], List[str], bool, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in IdentityAttributesChangedChangesInnerOldValue with oneOf schemas: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue], List[str], bool, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityAttributesChangedChangesInnerOldValue:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> IdentityAttributesChangedChangesInnerOldValue:
        """Returns the object represented by the json string"""
        instance = IdentityAttributesChangedChangesInnerOldValue.construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into bool
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into List[str]
        try:
            # validation
            instance.oneof_schema_3_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_3_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue]
        try:
            # validation
            instance.oneof_schema_4_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_4_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into IdentityAttributesChangedChangesInnerOldValue with oneOf schemas: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue], List[str], bool, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IdentityAttributesChangedChangesInnerOldValue with oneOf schemas: Dict[str, IdentityAttributesChangedChangesInnerOldValueOneOfValue], List[str], bool, str. Details: " + ", ".join(error_messages))
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


