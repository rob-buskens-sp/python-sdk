# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.completed_approval_state import CompletedApprovalState
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class CompletedApprovalPreApprovalTriggerResult(BaseModel):
    """
    If the access request submitted event trigger is configured and this access request was intercepted by it, then this is the result of the trigger's decision to either approve or deny the request.
    """ # noqa: E501
    comment: Optional[StrictStr] = Field(default=None, description="The comment from the trigger")
    decision: Optional[CompletedApprovalState] = None
    reviewer: Optional[StrictStr] = Field(default=None, description="The name of the approver")
    var_date: Optional[datetime] = Field(default=None, description="The date and time the trigger decided on the request", alias="date")
    __properties: ClassVar[List[str]] = ["comment", "decision", "reviewer", "date"]

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
        """Create an instance of CompletedApprovalPreApprovalTriggerResult from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of CompletedApprovalPreApprovalTriggerResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "comment": obj.get("comment"),
            "decision": obj.get("decision"),
            "reviewer": obj.get("reviewer"),
            "date": obj.get("date")
        })
        return _obj


