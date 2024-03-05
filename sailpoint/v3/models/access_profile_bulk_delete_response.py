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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.access_profile_usage import AccessProfileUsage
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AccessProfileBulkDeleteResponse(BaseModel):
    """
    AccessProfileBulkDeleteResponse
    """ # noqa: E501
    task_id: Optional[StrictStr] = Field(default=None, description="ID of the task which is executing the bulk deletion. This can be passed to the **/task-status** API to track status.", alias="taskId")
    pending: Optional[List[StrictStr]] = Field(default=None, description="List of IDs of Access Profiles which are pending deletion.")
    in_use: Optional[List[AccessProfileUsage]] = Field(default=None, description="List of usages of Access Profiles targeted for deletion.", alias="inUse")
    __properties: ClassVar[List[str]] = ["taskId", "pending", "inUse"]

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
        """Create an instance of AccessProfileBulkDeleteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in in_use (list)
        _items = []
        if self.in_use:
            for _item in self.in_use:
                if _item:
                    _items.append(_item.to_dict())
            _dict['inUse'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccessProfileBulkDeleteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taskId": obj.get("taskId"),
            "pending": obj.get("pending"),
            "inUse": [AccessProfileUsage.from_dict(_item) for _item in obj.get("inUse")] if obj.get("inUse") is not None else None
        })
        return _obj


