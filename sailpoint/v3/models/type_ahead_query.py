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
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class TypeAheadQuery(BaseModel):
    """
    Query parameters used to construct an Elasticsearch type ahead query object.  The typeAheadQuery performs a search for top values beginning with the typed values. For example, typing \"Jo\" results in top hits matching \"Jo.\" Typing \"Job\" results in top hits matching \"Job.\" 
    """ # noqa: E501
    query: StrictStr = Field(description="The type ahead query string used to construct a phrase prefix match query.")
    field: StrictStr = Field(description="The field on which to perform the type ahead search.")
    nested_type: Optional[StrictStr] = Field(default=None, description="The nested type.", alias="nestedType")
    max_expansions: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = Field(default=10, description="The number of suffixes the last term will be expanded into. Influences the performance of the query and the number results returned. Valid values: 1 to 1000.", alias="maxExpansions")
    size: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=100, description="The max amount of records the search will return.")
    sort: Optional[StrictStr] = Field(default='desc', description="The sort order of the returned records.")
    sort_by_value: Optional[StrictBool] = Field(default=False, description="The flag that defines the sort type, by count or value.", alias="sortByValue")
    __properties: ClassVar[List[str]] = ["query", "field", "nestedType", "maxExpansions", "size", "sort", "sortByValue"]

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
        """Create an instance of TypeAheadQuery from a JSON string"""
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
        """Create an instance of TypeAheadQuery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "query": obj.get("query"),
            "field": obj.get("field"),
            "nestedType": obj.get("nestedType"),
            "maxExpansions": obj.get("maxExpansions") if obj.get("maxExpansions") is not None else 10,
            "size": obj.get("size") if obj.get("size") is not None else 100,
            "sort": obj.get("sort") if obj.get("sort") is not None else 'desc',
            "sortByValue": obj.get("sortByValue") if obj.get("sortByValue") is not None else False
        })
        return _obj


