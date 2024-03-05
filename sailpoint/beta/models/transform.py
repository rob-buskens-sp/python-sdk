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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Transform(BaseModel):
    """
    The representation of an internally- or customer-defined transform.
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=50)] = Field(description="Unique name of this transform")
    type: StrictStr = Field(description="The type of transform operation")
    attributes: Optional[Dict[str, Any]] = Field(description="Meta-data about the transform. Values in this list are specific to the type of transform to be executed.")
    __properties: ClassVar[List[str]] = ["name", "type", "attributes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('accountAttribute', 'base64Decode', 'base64Encode', 'concat', 'conditional', 'dateCompare', 'dateFormat', 'dateMath', 'decomposeDiacriticalMarks', 'e164phone', 'firstValid', 'rule', 'identityAttribute', 'indexOf', 'iso3166', 'lastIndexOf', 'leftPad', 'lookup', 'lower', 'normalizeNames', 'randomAlphaNumeric', 'randomNumeric', 'reference', 'replaceAll', 'replace', 'rightPad', 'split', 'static', 'substring', 'trim', 'upper', 'usernameGenerator', 'uuid'):
            raise ValueError("must be one of enum values ('accountAttribute', 'base64Decode', 'base64Encode', 'concat', 'conditional', 'dateCompare', 'dateFormat', 'dateMath', 'decomposeDiacriticalMarks', 'e164phone', 'firstValid', 'rule', 'identityAttribute', 'indexOf', 'iso3166', 'lastIndexOf', 'leftPad', 'lookup', 'lower', 'normalizeNames', 'randomAlphaNumeric', 'randomNumeric', 'reference', 'replaceAll', 'replace', 'rightPad', 'split', 'static', 'substring', 'trim', 'upper', 'usernameGenerator', 'uuid')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Transform from a JSON string"""
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
            exclude={
            },
            exclude_none=True,
        )
        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Transform from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "type": obj.get("type"),
            "attributes": obj.get("attributes")
        })
        return _obj


