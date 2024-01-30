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

from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class TokenAuthRequest(BaseModel):
    """
    TokenAuthRequest
    """

  # noqa: E501
    token: StrictStr = Field(description="Token value")
    user_alias: StrictStr = Field(
        description="User alias from table spt_identity field named 'name'",
        alias="userAlias")
    delivery_type: StrictStr = Field(description="Token delivery type",
                                     alias="deliveryType")
    __properties: ClassVar[List[str]] = ["token", "userAlias", "deliveryType"]

    @field_validator('delivery_type')
    def delivery_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('SMS_PERSONAL', 'VOICE_PERSONAL', 'SMS_WORK',
                         'VOICE_WORK', 'EMAIL_WORK', 'EMAIL_PERSONAL'):
            raise ValueError(
                "must be one of enum values ('SMS_PERSONAL', 'VOICE_PERSONAL', 'SMS_WORK', 'VOICE_WORK', 'EMAIL_WORK', 'EMAIL_PERSONAL')"
            )
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
        """Create an instance of TokenAuthRequest from a JSON string"""
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
        """Create an instance of TokenAuthRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "token": obj.get("token"),
            "userAlias": obj.get("userAlias"),
            "deliveryType": obj.get("deliveryType")
        })
        return _obj
