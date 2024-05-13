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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Split(BaseModel):
    """
    Split
    """ # noqa: E501
    delimiter: StrictStr = Field(description="This can be either a single character or a regex expression, and is used by the transform to identify the break point between two substrings in the incoming data")
    index: StrictStr = Field(description="An integer value for the desired array element after the incoming data has been split into a list; the array is a 0-based object, so the first array element would be index 0, the second element would be index 1, etc.")
    throws: Optional[StrictBool] = Field(default=False, description="A boolean (true/false) value which indicates whether an exception should be thrown and returned as an output when an index is out of bounds with the resultant array (i.e., the provided index value is larger than the size of the array)   `true` - The transform should return \"IndexOutOfBoundsException\"   `false` - The transform should return null   If not provided, the transform will default to false and return a null ")
    requires_periodic_refresh: Optional[StrictBool] = Field(default=False, description="A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process", alias="requiresPeriodicRefresh")
    input: Optional[Dict[str, Any]] = Field(default=None, description="This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI.")
    __properties: ClassVar[List[str]] = ["delimiter", "index", "throws", "requiresPeriodicRefresh", "input"]

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
        """Create an instance of Split from a JSON string"""
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
        """Create an instance of Split from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delimiter": obj.get("delimiter"),
            "index": obj.get("index"),
            "throws": obj.get("throws") if obj.get("throws") is not None else False,
            "requiresPeriodicRefresh": obj.get("requiresPeriodicRefresh") if obj.get("requiresPeriodicRefresh") is not None else False,
            "input": obj.get("input")
        })
        return _obj


