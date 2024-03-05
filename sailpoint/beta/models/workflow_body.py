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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.beta.models.workflow_body_owner import WorkflowBodyOwner
from sailpoint.beta.models.workflow_definition import WorkflowDefinition
from sailpoint.beta.models.workflow_trigger import WorkflowTrigger
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowBody(BaseModel):
    """
    WorkflowBody
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="The name of the workflow")
    owner: Optional[WorkflowBodyOwner] = None
    description: Optional[StrictStr] = Field(default=None, description="Description of what the workflow accomplishes")
    definition: Optional[WorkflowDefinition] = None
    enabled: Optional[StrictBool] = Field(default=False, description="Enable or disable the workflow.  Workflows cannot be created in an enabled state.")
    trigger: Optional[WorkflowTrigger] = None
    __properties: ClassVar[List[str]] = ["name", "owner", "description", "definition", "enabled", "trigger"]

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
        """Create an instance of WorkflowBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trigger
        if self.trigger:
            _dict['trigger'] = self.trigger.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkflowBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "owner": WorkflowBodyOwner.from_dict(obj.get("owner")) if obj.get("owner") is not None else None,
            "description": obj.get("description"),
            "definition": WorkflowDefinition.from_dict(obj.get("definition")) if obj.get("definition") is not None else None,
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "trigger": WorkflowTrigger.from_dict(obj.get("trigger")) if obj.get("trigger") is not None else None
        })
        return _obj


