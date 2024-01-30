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

from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TextQuery(BaseModel):
    """
    Query parameters used to construct an Elasticsearch text query object.
    """ # noqa: E501
    terms: List[StrictStr] = Field(
        description=
        "Words or characters that specify a particular thing to be searched for."
    )
    fields: List[StrictStr] = Field(description="The fields to be searched.")
    match_any: Optional[StrictBool] = Field(
        default=False,
        description=
        "Indicates that at least one of the terms must be found in the specified fields;  otherwise, all terms must be found.",
        alias="matchAny")
    contains: Optional[StrictBool] = Field(
        default=False,
        description=
        "Indicates that the terms can be located anywhere in the specified fields;  otherwise, the fields must begin with the terms."
    )
    __properties: ClassVar[List[str]] = [
        "terms", "fields", "matchAny", "contains"
    ]

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
        """Create an instance of TextQuery from a JSON string"""
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
        """Create an instance of TextQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "terms":
            obj.get("terms"),
            "fields":
            obj.get("fields"),
            "matchAny":
            obj.get("matchAny") if obj.get("matchAny") is not None else False,
            "contains":
            obj.get("contains") if obj.get("contains") is not None else False
        })
        return _obj
