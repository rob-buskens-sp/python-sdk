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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SedBatchStats(BaseModel):
    """
    Sed Batch Stats
    """ # noqa: E501
    batch_complete: Optional[StrictBool] = Field(default=False, description="batch complete", alias="batchComplete")
    batch_id: Optional[StrictStr] = Field(default=None, description="batch Id", alias="batchId")
    discovered_count: Optional[StrictInt] = Field(default=None, description="discovered count", alias="discoveredCount")
    discovery_complete: Optional[StrictBool] = Field(default=False, description="discovery complete", alias="discoveryComplete")
    processed_count: Optional[StrictInt] = Field(default=None, description="processed count", alias="processedCount")
    __properties: ClassVar[List[str]] = ["batchComplete", "batchId", "discoveredCount", "discoveryComplete", "processedCount"]

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
        """Create an instance of SedBatchStats from a JSON string"""
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
        """Create an instance of SedBatchStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batchComplete": obj.get("batchComplete") if obj.get("batchComplete") is not None else False,
            "batchId": obj.get("batchId"),
            "discoveredCount": obj.get("discoveredCount"),
            "discoveryComplete": obj.get("discoveryComplete") if obj.get("discoveryComplete") is not None else False,
            "processedCount": obj.get("processedCount")
        })
        return _obj


