# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from sailpoint.v3.models.workflow_library_action import WorkflowLibraryAction
from sailpoint.v3.models.workflow_library_operator import WorkflowLibraryOperator
from sailpoint.v3.models.workflow_library_trigger import WorkflowLibraryTrigger
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

LISTCOMPLETEWORKFLOWLIBRARY200RESPONSEINNER_ANY_OF_SCHEMAS = ["WorkflowLibraryAction", "WorkflowLibraryOperator", "WorkflowLibraryTrigger"]

class ListCompleteWorkflowLibrary200ResponseInner(BaseModel):
    """
    ListCompleteWorkflowLibrary200ResponseInner
    """

    # data type: WorkflowLibraryAction
    anyof_schema_1_validator: Optional[WorkflowLibraryAction] = None
    # data type: WorkflowLibraryTrigger
    anyof_schema_2_validator: Optional[WorkflowLibraryTrigger] = None
    # data type: WorkflowLibraryOperator
    anyof_schema_3_validator: Optional[WorkflowLibraryOperator] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[WorkflowLibraryAction, WorkflowLibraryOperator, WorkflowLibraryTrigger]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: List[str] = Literal[LISTCOMPLETEWORKFLOWLIBRARY200RESPONSEINNER_ANY_OF_SCHEMAS]

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ListCompleteWorkflowLibrary200ResponseInner.model_construct()
        error_messages = []
        # validate data type: WorkflowLibraryAction
        if not isinstance(v, WorkflowLibraryAction):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WorkflowLibraryAction`")
        else:
            return v

        # validate data type: WorkflowLibraryTrigger
        if not isinstance(v, WorkflowLibraryTrigger):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WorkflowLibraryTrigger`")
        else:
            return v

        # validate data type: WorkflowLibraryOperator
        if not isinstance(v, WorkflowLibraryOperator):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WorkflowLibraryOperator`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ListCompleteWorkflowLibrary200ResponseInner with anyOf schemas: WorkflowLibraryAction, WorkflowLibraryOperator, WorkflowLibraryTrigger. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[WorkflowLibraryAction] = None
        try:
            instance.actual_instance = WorkflowLibraryAction.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[WorkflowLibraryTrigger] = None
        try:
            instance.actual_instance = WorkflowLibraryTrigger.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[WorkflowLibraryOperator] = None
        try:
            instance.actual_instance = WorkflowLibraryOperator.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListCompleteWorkflowLibrary200ResponseInner with anyOf schemas: WorkflowLibraryAction, WorkflowLibraryOperator, WorkflowLibraryTrigger. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


