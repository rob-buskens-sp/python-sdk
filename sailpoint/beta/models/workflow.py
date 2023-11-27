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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from sailpoint.beta.models.workflow_all_of_creator import WorkflowAllOfCreator
from sailpoint.beta.models.workflow_body_owner import WorkflowBodyOwner
from sailpoint.beta.models.workflow_definition import WorkflowDefinition
from sailpoint.beta.models.workflow_trigger import WorkflowTrigger


class Workflow(BaseModel):
    """
    Workflow
    """
    name: Optional[StrictStr] = Field(None,
                                      description="The name of the workflow")
    owner: Optional[WorkflowBodyOwner] = None
    description: Optional[StrictStr] = Field(
        None, description="Description of what the workflow accomplishes")
    definition: Optional[WorkflowDefinition] = None
    enabled: Optional[StrictBool] = Field(
        False,
        description=
        "Enable or disable the workflow.  Workflows cannot be created in an enabled state."
    )
    trigger: Optional[WorkflowTrigger] = None
    id: Optional[StrictStr] = Field(
        None,
        description="Workflow ID. This is a UUID generated upon creation.")
    execution_count: Optional[StrictInt] = Field(
        None,
        alias="executionCount",
        description="The number of times this workflow has been executed.")
    failure_count: Optional[StrictInt] = Field(
        None,
        alias="failureCount",
        description=
        "The number of times this workflow has failed during execution.")
    created: Optional[datetime] = Field(
        None, description="The date and time the workflow was created.")
    creator: Optional[WorkflowAllOfCreator] = None
    __properties = [
        "name", "owner", "description", "definition", "enabled", "trigger",
        "id", "executionCount", "failureCount", "created", "creator"
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
    def from_json(cls, json_str: str) -> Workflow:
        """Create an instance of Workflow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of owner
        if self.owner:
            _dict['owner'] = self.owner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trigger
        if self.trigger:
            _dict['trigger'] = self.trigger.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Workflow:
        """Create an instance of Workflow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Workflow.parse_obj(obj)

        _obj = Workflow.parse_obj({
            "name":
            obj.get("name"),
            "owner":
            WorkflowBodyOwner.from_dict(obj.get("owner"))
            if obj.get("owner") is not None else None,
            "description":
            obj.get("description"),
            "definition":
            WorkflowDefinition.from_dict(obj.get("definition"))
            if obj.get("definition") is not None else None,
            "enabled":
            obj.get("enabled") if obj.get("enabled") is not None else False,
            "trigger":
            WorkflowTrigger.from_dict(obj.get("trigger"))
            if obj.get("trigger") is not None else None,
            "id":
            obj.get("id"),
            "execution_count":
            obj.get("executionCount"),
            "failure_count":
            obj.get("failureCount"),
            "created":
            obj.get("created"),
            "creator":
            WorkflowAllOfCreator.from_dict(obj.get("creator"))
            if obj.get("creator") is not None else None
        })
        return _obj
