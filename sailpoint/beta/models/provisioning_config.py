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
from pydantic import BaseModel, StrictBool, StrictInt
from pydantic import Field
from sailpoint.beta.models.provisioning_config_managed_resource_refs_inner import ProvisioningConfigManagedResourceRefsInner
from sailpoint.beta.models.provisioning_config_plan_initializer_script import ProvisioningConfigPlanInitializerScript
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProvisioningConfig(BaseModel):
    """
    Specification of a Service Desk integration provisioning configuration.
    """ # noqa: E501
    universal_manager: Optional[StrictBool] = Field(default=False, description="Specifies whether this configuration is used to manage provisioning requests for all sources from the org.  If true, no managedResourceRefs are allowed.", alias="universalManager")
    managed_resource_refs: Optional[List[ProvisioningConfigManagedResourceRefsInner]] = Field(default=None, description="References to sources for the Service Desk integration template.  May only be specified if universalManager is false.", alias="managedResourceRefs")
    plan_initializer_script: Optional[ProvisioningConfigPlanInitializerScript] = Field(default=None, alias="planInitializerScript")
    no_provisioning_requests: Optional[StrictBool] = Field(default=False, description="Name of an attribute that when true disables the saving of ProvisioningRequest objects whenever plans are sent through this integration.", alias="noProvisioningRequests")
    provisioning_request_expiration: Optional[StrictInt] = Field(default=None, description="When saving pending requests is enabled, this defines the number of hours the request is allowed to live before it is considered expired and no longer affects plan compilation.", alias="provisioningRequestExpiration")
    __properties: ClassVar[List[str]] = ["universalManager", "managedResourceRefs", "planInitializerScript", "noProvisioningRequests", "provisioningRequestExpiration"]

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
        """Create an instance of ProvisioningConfig from a JSON string"""
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
                "universal_manager",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in managed_resource_refs (list)
        _items = []
        if self.managed_resource_refs:
            for _item in self.managed_resource_refs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['managedResourceRefs'] = _items
        # override the default output from pydantic by calling `to_dict()` of plan_initializer_script
        if self.plan_initializer_script:
            _dict['planInitializerScript'] = self.plan_initializer_script.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProvisioningConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "universalManager": obj.get("universalManager") if obj.get("universalManager") is not None else False,
            "managedResourceRefs": [ProvisioningConfigManagedResourceRefsInner.from_dict(_item) for _item in obj.get("managedResourceRefs")] if obj.get("managedResourceRefs") is not None else None,
            "planInitializerScript": ProvisioningConfigPlanInitializerScript.from_dict(obj.get("planInitializerScript")) if obj.get("planInitializerScript") is not None else None,
            "noProvisioningRequests": obj.get("noProvisioningRequests") if obj.get("noProvisioningRequests") is not None else False,
            "provisioningRequestExpiration": obj.get("provisioningRequestExpiration")
        })
        return _obj


