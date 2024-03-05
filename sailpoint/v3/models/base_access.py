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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.v3.models.base_access_all_of_owner import BaseAccessAllOfOwner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BaseAccess(BaseModel):
    """
    BaseAccess
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique ID of the referenced object.")
    name: Optional[StrictStr] = Field(default=None, description="The human readable name of the referenced object.")
    description: Optional[StrictStr] = Field(default=None, description="Access item's description.")
    created: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the time when the object was created.")
    modified: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the time when the object was last modified.")
    synced: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the `synced` time and the time when the updated data is actually available in the search API. ")
    enabled: Optional[StrictBool] = Field(default=False, description="Indicates whether the access item is currently enabled.")
    requestable: Optional[StrictBool] = Field(default=True, description="Indicates whether the access item can be requested.")
    request_comments_required: Optional[StrictBool] = Field(default=False, description="Indicates whether comments are required for requests to access the item.", alias="requestCommentsRequired")
    owner: Optional[BaseAccessAllOfOwner] = None
    __properties: ClassVar[List[str]] = ["id", "name", "description", "created", "modified", "synced", "enabled", "requestable", "requestCommentsRequired", "owner"]

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
        """Create an instance of BaseAccess from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if modified (nullable) is None
        # and model_fields_set contains the field
        if self.modified is None and "modified" in self.model_fields_set:
            _dict['modified'] = None

        # set to None if synced (nullable) is None
        # and model_fields_set contains the field
        if self.synced is None and "synced" in self.model_fields_set:
            _dict['synced'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BaseAccess from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created": obj.get("created"),
            "modified": obj.get("modified"),
            "synced": obj.get("synced"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "requestable": obj.get("requestable") if obj.get("requestable") is not None else True,
            "requestCommentsRequired": obj.get("requestCommentsRequired") if obj.get("requestCommentsRequired") is not None else False,
            "owner": BaseAccessAllOfOwner.from_dict(obj.get("owner")) if obj.get("owner") is not None else None
        })
        return _obj


