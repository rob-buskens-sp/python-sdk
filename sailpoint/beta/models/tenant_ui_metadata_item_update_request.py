# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TenantUiMetadataItemUpdateRequest(BaseModel):
    """
    TenantUiMetadataItemUpdateRequest
    """ # noqa: E501
    iframe_white_list: Optional[StrictStr] = Field(default=None, description="Parameter that organizational administrators can adjust to permit another domain to encapsulate IDN within an iframe. If you would like to reset the value use \"null\". It will only allow include into iframe non authenticated portions of the product, such as password reset.", alias="iframeWhiteList")
    username_label: Optional[StrictStr] = Field(default=None, description="Descriptor for the username input field. If you would like to reset the value use \"null\".", alias="usernameLabel")
    username_empty_text: Optional[StrictStr] = Field(default=None, description="Placeholder text displayed in the username input field. If you would like to reset the value use \"null\".", alias="usernameEmptyText")
    __properties: ClassVar[List[str]] = ["iframeWhiteList", "usernameLabel", "usernameEmptyText"]

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
        """Create an instance of TenantUiMetadataItemUpdateRequest from a JSON string"""
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
        # set to None if iframe_white_list (nullable) is None
        # and model_fields_set contains the field
        if self.iframe_white_list is None and "iframe_white_list" in self.model_fields_set:
            _dict['iframeWhiteList'] = None

        # set to None if username_label (nullable) is None
        # and model_fields_set contains the field
        if self.username_label is None and "username_label" in self.model_fields_set:
            _dict['usernameLabel'] = None

        # set to None if username_empty_text (nullable) is None
        # and model_fields_set contains the field
        if self.username_empty_text is None and "username_empty_text" in self.model_fields_set:
            _dict['usernameEmptyText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of TenantUiMetadataItemUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iframeWhiteList": obj.get("iframeWhiteList"),
            "usernameLabel": obj.get("usernameLabel"),
            "usernameEmptyText": obj.get("usernameEmptyText")
        })
        return _obj


