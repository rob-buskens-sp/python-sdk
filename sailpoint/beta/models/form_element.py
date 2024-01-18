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

from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class FormElement(BaseModel):
    """
    FormElement
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="Form element identifier.")
    element_type: Optional[StrictStr] = Field(
        default=None,
        description=
        "FormElementType value.  TEXT FormElementTypeText TOGGLE FormElementTypeToggle TEXTAREA FormElementTypeTextArea HIDDEN FormElementTypeHidden PHONE FormElementTypePhone EMAIL FormElementTypeEmail SELECT FormElementTypeSelect DATE FormElementTypeDate SECTION FormElementTypeSection COLUMNS FormElementTypeColumns",
        alias="elementType")
    config: Optional[Dict[str,
                          Union[str,
                                Any]]] = Field(default=None,
                                               description="Config object.")
    key: Optional[StrictStr] = Field(default=None,
                                     description="Technical key.")
    validations: Optional[Union[str, Any]] = Field(
        default=None, description="Set of FormElementValidation items.")
    __properties: ClassVar[List[str]] = [
        "id", "elementType", "config", "key", "validations"
    ]

    @field_validator('element_type')
    def element_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('TEXT', 'TOGGLE', 'TEXTAREA', 'HIDDEN', 'PHONE',
                         'EMAIL', 'SELECT', 'DATE', 'SECTION', 'COLUMNS'):
            raise ValueError(
                "must be one of enum values ('TEXT', 'TOGGLE', 'TEXTAREA', 'HIDDEN', 'PHONE', 'EMAIL', 'SELECT', 'DATE', 'SECTION', 'COLUMNS')"
            )
        return value

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FormElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={},
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FormElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "elementType": obj.get("elementType"),
            "config": obj.get("config"),
            "key": obj.get("key"),
            "validations": obj.get("validations")
        })
        return _obj
