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
from sailpoint.v3.models.account_source import AccountSource
from sailpoint.v3.models.attribute_request import AttributeRequest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OriginalRequest(BaseModel):
    """
    OriginalRequest
    """ # noqa: E501
    account_id: Optional[StrictStr] = Field(default=None, description="Account ID.", alias="accountId")
    attribute_requests: Optional[List[AttributeRequest]] = Field(default=None, description="Attribute changes requested for account.", alias="attributeRequests")
    op: Optional[StrictStr] = Field(default=None, description="Operation used.")
    source: Optional[AccountSource] = None
    __properties: ClassVar[List[str]] = ["accountId", "attributeRequests", "op", "source"]

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
        """Create an instance of OriginalRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attribute_requests (list)
        _items = []
        if self.attribute_requests:
            for _item in self.attribute_requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributeRequests'] = _items
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OriginalRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "attributeRequests": [AttributeRequest.from_dict(_item) for _item in obj.get("attributeRequests")] if obj.get("attributeRequests") is not None else None,
            "op": obj.get("op"),
            "source": AccountSource.from_dict(obj.get("source")) if obj.get("source") is not None else None
        })
        return _obj


