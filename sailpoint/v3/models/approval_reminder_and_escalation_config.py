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
from pydantic import BaseModel, StrictInt
from pydantic import Field
from typing_extensions import Annotated
from sailpoint.v3.models.identity_reference_with_name_and_email import IdentityReferenceWithNameAndEmail
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApprovalReminderAndEscalationConfig(BaseModel):
    """
    ApprovalReminderAndEscalationConfig
    """ # noqa: E501
    days_until_escalation: Optional[StrictInt] = Field(default=None, description="Number of days to wait before the first reminder. If no reminders are configured, then this is the number of days to wait before escalation.", alias="daysUntilEscalation")
    days_between_reminders: Optional[StrictInt] = Field(default=None, description="Number of days to wait between reminder notifications.", alias="daysBetweenReminders")
    max_reminders: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="Maximum number of reminder notification to send to the reviewer before approval escalation.", alias="maxReminders")
    fallback_approver_ref: Optional[IdentityReferenceWithNameAndEmail] = Field(default=None, alias="fallbackApproverRef")
    __properties: ClassVar[List[str]] = ["daysUntilEscalation", "daysBetweenReminders", "maxReminders", "fallbackApproverRef"]

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
        """Create an instance of ApprovalReminderAndEscalationConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fallback_approver_ref
        if self.fallback_approver_ref:
            _dict['fallbackApproverRef'] = self.fallback_approver_ref.to_dict()
        # set to None if days_until_escalation (nullable) is None
        # and model_fields_set contains the field
        if self.days_until_escalation is None and "days_until_escalation" in self.model_fields_set:
            _dict['daysUntilEscalation'] = None

        # set to None if days_between_reminders (nullable) is None
        # and model_fields_set contains the field
        if self.days_between_reminders is None and "days_between_reminders" in self.model_fields_set:
            _dict['daysBetweenReminders'] = None

        # set to None if max_reminders (nullable) is None
        # and model_fields_set contains the field
        if self.max_reminders is None and "max_reminders" in self.model_fields_set:
            _dict['maxReminders'] = None

        # set to None if fallback_approver_ref (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_approver_ref is None and "fallback_approver_ref" in self.model_fields_set:
            _dict['fallbackApproverRef'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApprovalReminderAndEscalationConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "daysUntilEscalation": obj.get("daysUntilEscalation"),
            "daysBetweenReminders": obj.get("daysBetweenReminders"),
            "maxReminders": obj.get("maxReminders"),
            "fallbackApproverRef": IdentityReferenceWithNameAndEmail.from_dict(obj.get("fallbackApproverRef")) if obj.get("fallbackApproverRef") is not None else None
        })
        return _obj


