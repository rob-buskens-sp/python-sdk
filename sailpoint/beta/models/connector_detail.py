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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ConnectorDetail(BaseModel):
    """
    ConnectorDetail
    """

  # noqa: E501
    name: Optional[StrictStr] = Field(default=None,
                                      description="The connector name")
    source_config_xml: Optional[StrictStr] = Field(
        default=None,
        description="XML representation of the source config data",
        alias="sourceConfigXml")
    source_config: Optional[StrictStr] = Field(
        default=None,
        description="JSON representation of the source config data",
        alias="sourceConfig")
    direct_connect: Optional[StrictBool] = Field(
        default=None,
        description="true if the source is a direct connect source",
        alias="directConnect")
    file_upload: Optional[StrictBool] = Field(
        default=None,
        description=
        "Connector config's file upload attribute, false if not there",
        alias="fileUpload")
    uploaded_files: Optional[StrictStr] = Field(
        default=None,
        description="List of uploaded file strings for the connector",
        alias="uploadedFiles")
    connector_metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Object containing metadata pertinent to the UI to be used",
        alias="connectorMetadata")
    __properties: ClassVar[List[str]] = [
        "name", "sourceConfigXml", "sourceConfig", "directConnect",
        "fileUpload", "uploadedFiles", "connectorMetadata"
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
        """Create an instance of ConnectorDetail from a JSON string"""
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
        """Create an instance of ConnectorDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name":
            obj.get("name"),
            "sourceConfigXml":
            obj.get("sourceConfigXml"),
            "sourceConfig":
            obj.get("sourceConfig"),
            "directConnect":
            obj.get("directConnect"),
            "fileUpload":
            obj.get("fileUpload"),
            "uploadedFiles":
            obj.get("uploadedFiles"),
            "connectorMetadata":
            obj.get("connectorMetadata")
        })
        return _obj
