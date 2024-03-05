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
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.beta.models.product import Product
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Tenant(BaseModel):
    """
    Tenant
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for the Tenant")
    name: Optional[StrictStr] = Field(default=None, description="Abbreviated name of the Tenant")
    full_name: Optional[StrictStr] = Field(default=None, description="Human-readable name of the Tenant", alias="fullName")
    pod: Optional[StrictStr] = Field(default=None, description="Deployment pod for the Tenant")
    region: Optional[StrictStr] = Field(default=None, description="Deployment region for the Tenant")
    description: Optional[StrictStr] = Field(default=None, description="Description of the Tenant")
    products: Optional[List[Product]] = None
    __properties: ClassVar[List[str]] = ["id", "name", "fullName", "pod", "region", "description", "products"]

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
        """Create an instance of Tenant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in products (list)
        _items = []
        if self.products:
            for _item in self.products:
                if _item:
                    _items.append(_item.to_dict())
            _dict['products'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Tenant from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fullName": obj.get("fullName"),
            "pod": obj.get("pod"),
            "region": obj.get("region"),
            "description": obj.get("description"),
            "products": [Product.from_dict(_item) for _item in obj.get("products")] if obj.get("products") is not None else None
        })
        return _obj


