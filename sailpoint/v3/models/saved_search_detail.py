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

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from sailpoint.v3.models.column import Column
from sailpoint.v3.models.index import Index
from sailpoint.v3.models.saved_search_detail_filters import SavedSearchDetailFilters


class SavedSearchDetail(BaseModel):
    """
    SavedSearchDetail
    """
    public: Optional[StrictBool] = Field(
        False, description="Indicates if the saved search is public. ")
    created: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    modified: Optional[datetime] = Field(
        None, description="A date-time in ISO-8601 format")
    indices: conlist(Index) = Field(
        ...,
        description=
        "The names of the Elasticsearch indices in which to search. ")
    columns: Optional[Dict[str, conlist(Column)]] = Field(
        None,
        description=
        "The columns to be returned (specifies the order in which they will be presented) for each document type.  The currently supported document types are: _accessprofile_, _accountactivity_, _account_, _aggregation_, _entitlement_, _event_, _identity_, and _role_. "
    )
    query: StrictStr = Field(
        ...,
        description=
        "The search query using Elasticsearch [Query String Query](https://www.elastic.co/guide/en/elasticsearch/reference/5.2/query-dsl-query-string-query.html#query-string) syntax from the Query DSL. "
    )
    fields: Optional[conlist(StrictStr)] = Field(
        None,
        description="The fields to be searched against in a multi-field query. "
    )
    sort: Optional[conlist(StrictStr)] = Field(
        None, description="The fields to be used to sort the search results. ")
    filters: Optional[SavedSearchDetailFilters] = None
    __properties = [
        "public", "created", "modified", "indices", "columns", "query",
        "fields", "sort", "filters"
    ]

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
    def from_json(cls, json_str: str) -> SavedSearchDetail:
        """Create an instance of SavedSearchDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each value in columns (dict of array)
        _field_dict_of_array = {}
        if self.columns:
            for _key in self.columns:
                if self.columns[_key]:
                    _field_dict_of_array[_key] = [
                        _item.to_dict() for _item in self.columns[_key]
                    ]
            _dict['columns'] = _field_dict_of_array
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if modified (nullable) is None
        # and __fields_set__ contains the field
        if self.modified is None and "modified" in self.__fields_set__:
            _dict['modified'] = None

        # set to None if fields (nullable) is None
        # and __fields_set__ contains the field
        if self.fields is None and "fields" in self.__fields_set__:
            _dict['fields'] = None

        # set to None if filters (nullable) is None
        # and __fields_set__ contains the field
        if self.filters is None and "filters" in self.__fields_set__:
            _dict['filters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SavedSearchDetail:
        """Create an instance of SavedSearchDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SavedSearchDetail.parse_obj(obj)

        _obj = SavedSearchDetail.parse_obj({
            "public":
            obj.get("public") if obj.get("public") is not None else False,
            "created":
            obj.get("created"),
            "modified":
            obj.get("modified"),
            "indices":
            obj.get("indices"),
            "columns":
            dict((_k, [Column.from_dict(_item)
                       for _item in _v] if _v is not None else None)
                 for _k, _v in obj.get("columns").items()),
            "query":
            obj.get("query"),
            "fields":
            obj.get("fields"),
            "sort":
            obj.get("sort"),
            "filters":
            SavedSearchDetailFilters.from_dict(obj.get("filters"))
            if obj.get("filters") is not None else None
        })
        return _obj
