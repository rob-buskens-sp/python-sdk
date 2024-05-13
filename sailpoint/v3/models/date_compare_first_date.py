# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
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
from sailpoint.v3.models.account_attribute import AccountAttribute
from sailpoint.v3.models.date_format import DateFormat
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

DATECOMPAREFIRSTDATE_ONE_OF_SCHEMAS = ["AccountAttribute", "DateFormat"]

class DateCompareFirstDate(BaseModel):
    """
    This is the first date to consider (The date that would be on the left hand side of the comparison operation).
    """
    # data type: AccountAttribute
    oneof_schema_1_validator: Optional[AccountAttribute] = None
    # data type: DateFormat
    oneof_schema_2_validator: Optional[DateFormat] = None
    actual_instance: Optional[Union[AccountAttribute, DateFormat]] = None
    one_of_schemas: List[str] = Literal["AccountAttribute", "DateFormat"]

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
    def actual_instance_must_validate_oneof(cls, v):
        instance = DateCompareFirstDate.model_construct()
        error_messages = []
        match = 0
        # validate data type: AccountAttribute
        if not isinstance(v, AccountAttribute):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AccountAttribute`")
        else:
            match += 1
        # validate data type: DateFormat
        if not isinstance(v, DateFormat):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DateFormat`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in DateCompareFirstDate with oneOf schemas: AccountAttribute, DateFormat. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in DateCompareFirstDate with oneOf schemas: AccountAttribute, DateFormat. Details: " + ", ".join(error_messages))
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

        # deserialize data into AccountAttribute
        try:
            instance.actual_instance = AccountAttribute.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DateFormat
        try:
            instance.actual_instance = DateFormat.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DateCompareFirstDate with oneOf schemas: AccountAttribute, DateFormat. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DateCompareFirstDate with oneOf schemas: AccountAttribute, DateFormat. Details: " + ", ".join(error_messages))
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


