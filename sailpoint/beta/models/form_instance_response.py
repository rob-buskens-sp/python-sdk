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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from sailpoint.beta.models.form_condition import FormCondition
from sailpoint.beta.models.form_element import FormElement
from sailpoint.beta.models.form_error import FormError
from sailpoint.beta.models.form_instance_created_by import FormInstanceCreatedBy
from sailpoint.beta.models.form_instance_recipient import FormInstanceRecipient
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class FormInstanceResponse(BaseModel):
    """
    FormInstanceResponse
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="Created is the date the form instance was assigned")
    created_by: Optional[FormInstanceCreatedBy] = Field(default=None, alias="createdBy")
    expire: Optional[StrictStr] = Field(default=None, description="Expire is the maximum amount of time that a form can be in progress. After this time is reached then the form will be moved to a CANCELED state automatically. The user will no longer be able to complete the submission. When a form instance is expires an audit log will be generated for that record")
    form_conditions: Optional[List[FormCondition]] = Field(default=None, description="FormConditions is the conditional logic that modify the form dynamically modify the form as the recipient is interacting out the form", alias="formConditions")
    form_data: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="FormData is the data provided by the form on submit. The data is in a key -> value map", alias="formData")
    form_definition_id: Optional[StrictStr] = Field(default=None, description="FormDefinitionID is the id of the form definition that created this form", alias="formDefinitionId")
    form_elements: Optional[List[FormElement]] = Field(default=None, description="FormElements is the configuration of the form, this would be a repeat of the fields from the form-config", alias="formElements")
    form_errors: Optional[List[FormError]] = Field(default=None, description="FormErrors is an array of form validation errors from the last time the form instance was transitioned to the SUBMITTED state. If the form instance had validation errors then it would be moved to the IN PROGRESS state where the client can retrieve these errors", alias="formErrors")
    form_input: Optional[Dict[str, Dict[str, Any]]] = Field(default=None, description="FormInput is an object of form input labels to value", alias="formInput")
    id: Optional[StrictStr] = Field(default=None, description="FormInstanceID is a unique guid identifying this form instance")
    modified: Optional[datetime] = Field(default=None, description="Modified is the last date the form instance was modified")
    recipients: Optional[List[FormInstanceRecipient]] = Field(default=None, description="Recipients references to the recipient of a form. The recipients are those who are responsible for filling out a form and completing it")
    stand_alone_form: Optional[StrictBool] = Field(default=False, description="StandAloneForm is a boolean flag to indicate if this form should be available for users to complete via the standalone form UI or should this only be available to be completed by as an embedded form", alias="standAloneForm")
    stand_alone_form_url: Optional[StrictStr] = Field(default=None, description="StandAloneFormURL is the URL where this form may be completed by the designated recipients using the standalone form UI", alias="standAloneFormUrl")
    state: Optional[StrictStr] = Field(default=None, description="State the state of the form instance ASSIGNED FormInstanceStateAssigned IN_PROGRESS FormInstanceStateInProgress SUBMITTED FormInstanceStateSubmitted COMPLETED FormInstanceStateCompleted CANCELLED FormInstanceStateCancelled")
    __properties: ClassVar[List[str]] = ["created", "createdBy", "expire", "formConditions", "formData", "formDefinitionId", "formElements", "formErrors", "formInput", "id", "modified", "recipients", "standAloneForm", "standAloneFormUrl", "state"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ASSIGNED', 'IN_PROGRESS', 'SUBMITTED', 'COMPLETED', 'CANCELLED'):
            raise ValueError("must be one of enum values ('ASSIGNED', 'IN_PROGRESS', 'SUBMITTED', 'COMPLETED', 'CANCELLED')")
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
        """Create an instance of FormInstanceResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in form_conditions (list)
        _items = []
        if self.form_conditions:
            for _item in self.form_conditions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formConditions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_elements (list)
        _items = []
        if self.form_elements:
            for _item in self.form_elements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formElements'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in form_errors (list)
        _items = []
        if self.form_errors:
            for _item in self.form_errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['formErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in recipients (list)
        _items = []
        if self.recipients:
            for _item in self.recipients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['recipients'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of FormInstanceResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "createdBy": FormInstanceCreatedBy.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "expire": obj.get("expire"),
            "formConditions": [FormCondition.from_dict(_item) for _item in obj.get("formConditions")] if obj.get("formConditions") is not None else None,
            "formData": obj.get("formData"),
            "formDefinitionId": obj.get("formDefinitionId"),
            "formElements": [FormElement.from_dict(_item) for _item in obj.get("formElements")] if obj.get("formElements") is not None else None,
            "formErrors": [FormError.from_dict(_item) for _item in obj.get("formErrors")] if obj.get("formErrors") is not None else None,
            "formInput": obj.get("formInput"),
            "id": obj.get("id"),
            "modified": obj.get("modified"),
            "recipients": [FormInstanceRecipient.from_dict(_item) for _item in obj.get("recipients")] if obj.get("recipients") is not None else None,
            "standAloneForm": obj.get("standAloneForm") if obj.get("standAloneForm") is not None else False,
            "standAloneFormUrl": obj.get("standAloneFormUrl"),
            "state": obj.get("state")
        })
        return _obj


