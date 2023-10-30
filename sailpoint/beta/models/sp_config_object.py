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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from beta.models.sp_config_url import SpConfigUrl

class SpConfigObject(BaseModel):
    """
    Response model for get object configuration.  # noqa: E501
    """
    object_type: Optional[StrictStr] = Field(None, alias="objectType", description="The object type this configuration is for.")
    resolve_by_id_url: Optional[SpConfigUrl] = Field(None, alias="resolveByIdUrl")
    resolve_by_name_url: Optional[conlist(SpConfigUrl)] = Field(None, alias="resolveByNameUrl", description="Url and query parameters to be used to resolve this type of object by name.")
    export_url: Optional[SpConfigUrl] = Field(None, alias="exportUrl")
    export_right: Optional[StrictStr] = Field(None, alias="exportRight", description="Rights needed by the invoker of sp-config/export in order to export this type of object.")
    export_limit: Optional[StrictInt] = Field(None, alias="exportLimit", description="Pagination limit imposed by the target service for this object type.")
    import_url: Optional[SpConfigUrl] = Field(None, alias="importUrl")
    import_right: Optional[StrictStr] = Field(None, alias="importRight", description="Rights needed by the invoker of sp-config/import in order to import this type of object.")
    import_limit: Optional[StrictInt] = Field(None, alias="importLimit", description="Pagination limit imposed by the target service for this object type.")
    reference_extractors: Optional[conlist(StrictStr)] = Field(None, alias="referenceExtractors", description="List of json paths within an exported object of this type that represent references that need to be resolved.")
    signature_required: Optional[StrictBool] = Field(False, alias="signatureRequired", description="If true, this type of object will be JWS signed and cannot be modified before import.")
    __properties = ["objectType", "resolveByIdUrl", "resolveByNameUrl", "exportUrl", "exportRight", "exportLimit", "importUrl", "importRight", "importLimit", "referenceExtractors", "signatureRequired"]

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
    def from_json(cls, json_str: str) -> SpConfigObject:
        """Create an instance of SpConfigObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
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
        # and __fields_set__ contains the field
        if self.reference_extractors is None and "reference_extractors" in self.__fields_set__:
            _dict['referenceExtractors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpConfigObject:
        """Create an instance of SpConfigObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpConfigObject.parse_obj(obj)

        _obj = SpConfigObject.parse_obj({
            "object_type": obj.get("objectType"),
            "resolve_by_id_url": SpConfigUrl.from_dict(obj.get("resolveByIdUrl")) if obj.get("resolveByIdUrl") is not None else None,
            "resolve_by_name_url": [SpConfigUrl.from_dict(_item) for _item in obj.get("resolveByNameUrl")] if obj.get("resolveByNameUrl") is not None else None,
            "export_url": SpConfigUrl.from_dict(obj.get("exportUrl")) if obj.get("exportUrl") is not None else None,
            "export_right": obj.get("exportRight"),
            "export_limit": obj.get("exportLimit"),
            "import_url": SpConfigUrl.from_dict(obj.get("importUrl")) if obj.get("importUrl") is not None else None,
            "import_right": obj.get("importRight"),
            "import_limit": obj.get("importLimit"),
            "reference_extractors": obj.get("referenceExtractors"),
            "signature_required": obj.get("signatureRequired") if obj.get("signatureRequired") is not None else False
        })
        return _obj


