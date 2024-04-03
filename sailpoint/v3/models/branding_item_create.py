# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBytes, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BrandingItemCreate(BaseModel):
    """
    BrandingItemCreate
    """ # noqa: E501
    name: StrictStr = Field(description="name of branding item")
    product_name: Optional[StrictStr] = Field(description="product name", alias="productName")
    action_button_color: Optional[StrictStr] = Field(default=None, description="hex value of color for action button", alias="actionButtonColor")
    active_link_color: Optional[StrictStr] = Field(default=None, description="hex value of color for link", alias="activeLinkColor")
    navigation_color: Optional[StrictStr] = Field(default=None, description="hex value of color for navigation bar", alias="navigationColor")
    email_from_address: Optional[StrictStr] = Field(default=None, description="email from address", alias="emailFromAddress")
    login_informational_message: Optional[StrictStr] = Field(default=None, description="login information message", alias="loginInformationalMessage")
    file_standard: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="png file with logo", alias="fileStandard")
    __properties: ClassVar[List[str]] = ["name", "productName", "actionButtonColor", "activeLinkColor", "navigationColor", "emailFromAddress", "loginInformationalMessage", "fileStandard"]

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
        """Create an instance of BrandingItemCreate from a JSON string"""
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
        # set to None if product_name (nullable) is None
        # and model_fields_set contains the field
        if self.product_name is None and "product_name" in self.model_fields_set:
            _dict['productName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BrandingItemCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "productName": obj.get("productName"),
            "actionButtonColor": obj.get("actionButtonColor"),
            "activeLinkColor": obj.get("activeLinkColor"),
            "navigationColor": obj.get("navigationColor"),
            "emailFromAddress": obj.get("emailFromAddress"),
            "loginInformationalMessage": obj.get("loginInformationalMessage"),
            "fileStandard": obj.get("fileStandard")
        })
        return _obj


