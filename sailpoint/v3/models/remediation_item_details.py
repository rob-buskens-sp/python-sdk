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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class RemediationItemDetails(BaseModel):
    """
    RemediationItemDetails
    """
    id: Optional[StrictStr] = Field(None, description="The ID of the certification")
    target_id: Optional[StrictStr] = Field(None, alias="targetId", description="The ID of the certification target")
    target_name: Optional[StrictStr] = Field(None, alias="targetName", description="The name of the certification target")
    target_display_name: Optional[StrictStr] = Field(None, alias="targetDisplayName", description="The display name of the certification target")
    application_name: Optional[StrictStr] = Field(None, alias="applicationName", description="The name of the application/source")
    attribute_name: Optional[StrictStr] = Field(None, alias="attributeName", description="The name of the attribute being certified")
    attribute_operation: Optional[StrictStr] = Field(None, alias="attributeOperation", description="The operation of the certification on the attribute")
    attribute_value: Optional[StrictStr] = Field(None, alias="attributeValue", description="The value of the attribute being certified")
    native_identity: Optional[StrictStr] = Field(None, alias="nativeIdentity", description="The native identity of the target")
    __properties = ["id", "targetId", "targetName", "targetDisplayName", "applicationName", "attributeName", "attributeOperation", "attributeValue", "nativeIdentity"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RemediationItemDetails:
        """Create an instance of RemediationItemDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RemediationItemDetails:
        """Create an instance of RemediationItemDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RemediationItemDetails.parse_obj(obj)

        _obj = RemediationItemDetails.parse_obj({
            "id": obj.get("id"),
            "target_id": obj.get("targetId"),
            "target_name": obj.get("targetName"),
            "target_display_name": obj.get("targetDisplayName"),
            "application_name": obj.get("applicationName"),
            "attribute_name": obj.get("attributeName"),
            "attribute_operation": obj.get("attributeOperation"),
            "attribute_value": obj.get("attributeValue"),
            "native_identity": obj.get("nativeIdentity")
        })
        return _obj


