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

from pydantic import BaseModel, Field, StrictStr
from sailpoint.beta.models.saved_search_complete_search_results import SavedSearchCompleteSearchResults


class SavedSearchComplete(BaseModel):
    """
    SavedSearchComplete
    """
    file_name: StrictStr = Field(...,
                                 alias="fileName",
                                 description="A name for the report file.")
    owner_email: StrictStr = Field(
        ...,
        alias="ownerEmail",
        description=
        "The email address of the identity that owns the saved search.")
    owner_name: StrictStr = Field(
        ...,
        alias="ownerName",
        description="The name of the identity that owns the saved search.")
    query: StrictStr = Field(
        ...,
        description="The search query that was used to generate the report.")
    search_name: StrictStr = Field(...,
                                   alias="searchName",
                                   description="The name of the saved search.")
    search_results: SavedSearchCompleteSearchResults = Field(
        ..., alias="searchResults")
    signed_s3_url: StrictStr = Field(
        ...,
        alias="signedS3Url",
        description="The Amazon S3 URL to download the report from.")
    __properties = [
        "fileName", "ownerEmail", "ownerName", "query", "searchName",
        "searchResults", "signedS3Url"
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
    def from_json(cls, json_str: str) -> SavedSearchComplete:
        """Create an instance of SavedSearchComplete from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of search_results
        if self.search_results:
            _dict['searchResults'] = self.search_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SavedSearchComplete:
        """Create an instance of SavedSearchComplete from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SavedSearchComplete.parse_obj(obj)

        _obj = SavedSearchComplete.parse_obj({
            "file_name":
            obj.get("fileName"),
            "owner_email":
            obj.get("ownerEmail"),
            "owner_name":
            obj.get("ownerName"),
            "query":
            obj.get("query"),
            "search_name":
            obj.get("searchName"),
            "search_results":
            SavedSearchCompleteSearchResults.from_dict(
                obj.get("searchResults"))
            if obj.get("searchResults") is not None else None,
            "signed_s3_url":
            obj.get("signedS3Url")
        })
        return _obj
