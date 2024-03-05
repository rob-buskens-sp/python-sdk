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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from sailpoint.v3.models.workflow_library_form_fields import WorkflowLibraryFormFields
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WorkflowLibraryTrigger(BaseModel):
    """
    WorkflowLibraryTrigger
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Trigger ID. This is a static namespaced ID for the trigger.")
    type: Optional[Dict[str, Any]] = Field(default=None, description="Trigger type")
    name: Optional[StrictStr] = Field(default=None, description="Trigger Name")
    description: Optional[StrictStr] = Field(default=None, description="Trigger Description")
    is_dynamic_schema: Optional[StrictBool] = Field(default=False, description="Determines whether the dynamic output schema is returned in place of the action's output schema. The dynamic schema lists non-static properties, like properties of a workflow form where each form has different fields. These will be provided dynamically based on available form fields.", alias="isDynamicSchema")
    input_example: Optional[Dict[str, Any]] = Field(default=None, description="Example trigger payload if applicable", alias="inputExample")
    form_fields: Optional[List[WorkflowLibraryFormFields]] = Field(default=None, description="One or more inputs that the trigger accepts", alias="formFields")
    __properties: ClassVar[List[str]] = ["id", "type", "name", "description", "isDynamicSchema", "inputExample", "formFields"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('EVENT', 'SCHEDULED', 'EXTERNAL'):
            raise ValueError("must be one of enum values ('EVENT', 'SCHEDULED', 'EXTERNAL')")
        return value

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
        """Create an instance of WorkflowLibraryTrigger from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in form_fields (list)
        _items = []
        if self.form_fields:
            for _item in self.form_fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formFields'] = _items
        # set to None if input_example (nullable) is None
        # and model_fields_set contains the field
        if self.input_example is None and "input_example" in self.model_fields_set:
            _dict['inputExample'] = None

        # set to None if form_fields (nullable) is None
        # and model_fields_set contains the field
        if self.form_fields is None and "form_fields" in self.model_fields_set:
            _dict['formFields'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WorkflowLibraryTrigger from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "isDynamicSchema": obj.get("isDynamicSchema") if obj.get("isDynamicSchema") is not None else False,
            "inputExample": obj.get("inputExample"),
            "formFields": [WorkflowLibraryFormFields.from_dict(_item) for _item in obj.get("formFields")] if obj.get("formFields") is not None else None
        })
        return _obj


