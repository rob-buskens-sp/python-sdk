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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TemplateDtoDefault(BaseModel):
    """
    TemplateDtoDefault
    """

  # noqa: E501
    key: Optional[StrictStr] = Field(
        default=None, description="The key of the default template")
    name: Optional[StrictStr] = Field(
        default=None, description="The name of the default template")
    medium: Optional[StrictStr] = Field(
        default=None,
        description=
        "The message medium. More mediums may be added in the future.")
    locale: Optional[StrictStr] = Field(
        default=None,
        description="The locale for the message text, a BCP 47 language tag.")
    subject: Optional[StrictStr] = Field(
        default=None, description="The subject of the default template")
    header: Optional[StrictStr] = Field(
        default=None,
        description=
        "The header value is now located within the body field. If included with non-null values, will result in a 400."
    )
    body: Optional[StrictStr] = Field(
        default=None, description="The body of the default template")
    footer: Optional[StrictStr] = Field(
        default=None,
        description=
        "The footer value is now located within the body field. If included with non-null values, will result in a 400."
    )
    var_from: Optional[StrictStr] = Field(
        default=None,
        description="The \"From:\" address of the default template",
        alias="from")
    reply_to: Optional[StrictStr] = Field(
        default=None,
        description="The \"Reply To\" field of the default template",
        alias="replyTo")
    description: Optional[StrictStr] = Field(
        default=None, description="The description of the default template")
    __properties: ClassVar[List[str]] = [
        "key", "name", "medium", "locale", "subject", "header", "body",
        "footer", "from", "replyTo", "description"
    ]

    @field_validator('medium')
    def medium_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EMAIL', 'PHONE', 'SMS', 'SLACK', 'TEAMS'):
            raise ValueError(
                "must be one of enum values ('EMAIL', 'PHONE', 'SMS', 'SLACK', 'TEAMS')"
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
        """Create an instance of TemplateDtoDefault from a JSON string"""
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
        # set to None if header (nullable) is None
        # and model_fields_set contains the field
        if self.header is None and "header" in self.model_fields_set:
            _dict['header'] = None

        # set to None if footer (nullable) is None
        # and model_fields_set contains the field
        if self.footer is None and "footer" in self.model_fields_set:
            _dict['footer'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TemplateDtoDefault from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "key": obj.get("key"),
            "name": obj.get("name"),
            "medium": obj.get("medium"),
            "locale": obj.get("locale"),
            "subject": obj.get("subject"),
            "header": obj.get("header"),
            "body": obj.get("body"),
            "footer": obj.get("footer"),
            "from": obj.get("from"),
            "replyTo": obj.get("replyTo"),
            "description": obj.get("description")
        })
        return _obj
