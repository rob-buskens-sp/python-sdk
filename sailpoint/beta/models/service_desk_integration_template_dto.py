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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.provisioning_config import ProvisioningConfig
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServiceDeskIntegrationTemplateDto(BaseModel):
    """
    ServiceDeskIntegrationTemplateDto
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="System-generated unique ID of the Object")
    name: StrictStr = Field(description="Name of the Object")
    created: Optional[datetime] = Field(default=None, description="Creation date of the Object")
    modified: Optional[datetime] = Field(default=None, description="Last modification date of the Object")
    type: StrictStr = Field(description="The 'type' property specifies the type of the Service Desk integration template.")
    attributes: Dict[str, Any] = Field(description="The 'attributes' property value is a map of attributes available for integrations using this Service Desk integration template.")
    provisioning_config: ProvisioningConfig = Field(alias="provisioningConfig")
    __properties: ClassVar[List[str]] = ["id", "name", "created", "modified", "type", "attributes", "provisioningConfig"]

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
        """Create an instance of ServiceDeskIntegrationTemplateDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "created",
                "modified",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of provisioning_config
        if self.provisioning_config:
            _dict['provisioningConfig'] = self.provisioning_config.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServiceDeskIntegrationTemplateDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "type": obj.get("type") if obj.get("type") is not None else 'Web Service SDIM',
            "attributes": obj.get("attributes"),
            "provisioningConfig": ProvisioningConfig.from_dict(obj.get("provisioningConfig")) if obj.get("provisioningConfig") is not None else None
        })
        return _obj


