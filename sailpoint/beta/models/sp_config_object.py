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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from sailpoint.beta.models.sp_config_url import SpConfigUrl
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SpConfigObject(BaseModel):
    """
    Response model for get object configuration.
    """

  # noqa: E501
    object_type: Optional[StrictStr] = Field(
        default=None,
        description="The object type this configuration is for.",
        alias="objectType")
    resolve_by_id_url: Optional[SpConfigUrl] = Field(default=None,
                                                     alias="resolveByIdUrl")
    resolve_by_name_url: Optional[List[SpConfigUrl]] = Field(
        default=None,
        description=
        "Url and query parameters to be used to resolve this type of object by name.",
        alias="resolveByNameUrl")
    export_url: Optional[SpConfigUrl] = Field(default=None, alias="exportUrl")
    export_right: Optional[StrictStr] = Field(
        default=None,
        description=
        "Rights needed by the invoker of sp-config/export in order to export this type of object.",
        alias="exportRight")
    export_limit: Optional[StrictInt] = Field(
        default=None,
        description=
        "Pagination limit imposed by the target service for this object type.",
        alias="exportLimit")
    import_url: Optional[SpConfigUrl] = Field(default=None, alias="importUrl")
    import_right: Optional[StrictStr] = Field(
        default=None,
        description=
        "Rights needed by the invoker of sp-config/import in order to import this type of object.",
        alias="importRight")
    import_limit: Optional[StrictInt] = Field(
        default=None,
        description=
        "Pagination limit imposed by the target service for this object type.",
        alias="importLimit")
    reference_extractors: Optional[List[StrictStr]] = Field(
        default=None,
        description=
        "List of json paths within an exported object of this type that represent references that need to be resolved.",
        alias="referenceExtractors")
    signature_required: Optional[StrictBool] = Field(
        default=False,
        description=
        "If true, this type of object will be JWS signed and cannot be modified before import.",
        alias="signatureRequired")
    __properties: ClassVar[List[str]] = [
        "objectType", "resolveByIdUrl", "resolveByNameUrl", "exportUrl",
        "exportRight", "exportLimit", "importUrl", "importRight",
        "importLimit", "referenceExtractors", "signatureRequired"
    ]

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
        """Create an instance of SpConfigObject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resolve_by_id_url
        if self.resolve_by_id_url:
            _dict['resolveByIdUrl'] = self.resolve_by_id_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resolve_by_name_url (list)
        _items = []
        if self.resolve_by_name_url:
            for _item in self.resolve_by_name_url:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resolveByNameUrl'] = _items
        # override the default output from pydantic by calling `to_dict()` of export_url
        if self.export_url:
            _dict['exportUrl'] = self.export_url.to_dict()
        # override the default output from pydantic by calling `to_dict()` of import_url
        if self.import_url:
            _dict['importUrl'] = self.import_url.to_dict()
        # set to None if reference_extractors (nullable) is None
        # and model_fields_set contains the field
        if self.reference_extractors is None and "reference_extractors" in self.model_fields_set:
            _dict['referenceExtractors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SpConfigObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "objectType":
            obj.get("objectType"),
            "resolveByIdUrl":
            SpConfigUrl.from_dict(obj.get("resolveByIdUrl"))
            if obj.get("resolveByIdUrl") is not None else None,
            "resolveByNameUrl": [
                SpConfigUrl.from_dict(_item)
                for _item in obj.get("resolveByNameUrl")
            ] if obj.get("resolveByNameUrl") is not None else None,
            "exportUrl":
            SpConfigUrl.from_dict(obj.get("exportUrl"))
            if obj.get("exportUrl") is not None else None,
            "exportRight":
            obj.get("exportRight"),
            "exportLimit":
            obj.get("exportLimit"),
            "importUrl":
            SpConfigUrl.from_dict(obj.get("importUrl"))
            if obj.get("importUrl") is not None else None,
            "importRight":
            obj.get("importRight"),
            "importLimit":
            obj.get("importLimit"),
            "referenceExtractors":
            obj.get("referenceExtractors"),
            "signatureRequired":
            obj.get("signatureRequired")
            if obj.get("signatureRequired") is not None else False
        })
        return _obj
