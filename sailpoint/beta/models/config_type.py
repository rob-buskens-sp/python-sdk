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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.config_type_enum import ConfigTypeEnum
from sailpoint.beta.models.config_type_enum_camel import ConfigTypeEnumCamel
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ConfigType(BaseModel):
    """
    Type of Reassignment Configuration.
    """ # noqa: E501
    priority: Optional[StrictInt] = None
    internal_name: Optional[ConfigTypeEnumCamel] = Field(default=None, alias="internalName")
    internal_name_camel: Optional[ConfigTypeEnum] = Field(default=None, alias="internalNameCamel")
    display_name: Optional[StrictStr] = Field(default=None, description="Human readable display name of the type to be shown on UI", alias="displayName")
    description: Optional[StrictStr] = Field(default=None, description="Description of the type of work to be reassigned, displayed by the UI.")
    __properties: ClassVar[List[str]] = ["priority", "internalName", "internalNameCamel", "displayName", "description"]

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
        """Create an instance of ConfigType from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ConfigType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "priority": obj.get("priority"),
            "internalName": obj.get("internalName"),
            "internalNameCamel": obj.get("internalNameCamel"),
            "displayName": obj.get("displayName"),
            "description": obj.get("description")
        })
        return _obj


