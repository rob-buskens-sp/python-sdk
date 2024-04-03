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
from sailpoint.v3.models.reassignment_type import ReassignmentType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApprovalForwardHistory(BaseModel):
    """
    ApprovalForwardHistory
    """ # noqa: E501
    old_approver_name: Optional[StrictStr] = Field(default=None, description="Display name of approver from whom the approval was forwarded.", alias="oldApproverName")
    new_approver_name: Optional[StrictStr] = Field(default=None, description="Display name of approver to whom the approval was forwarded.", alias="newApproverName")
    comment: Optional[StrictStr] = Field(default=None, description="Comment made while forwarding.")
    modified: Optional[datetime] = Field(default=None, description="Time at which approval was forwarded.")
    forwarder_name: Optional[StrictStr] = Field(default=None, description="Display name of forwarder who forwarded the approval.", alias="forwarderName")
    reassignment_type: Optional[ReassignmentType] = Field(default=None, alias="reassignmentType")
    __properties: ClassVar[List[str]] = ["oldApproverName", "newApproverName", "comment", "modified", "forwarderName", "reassignmentType"]

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
        """Create an instance of ApprovalForwardHistory from a JSON string"""
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
        # set to None if comment (nullable) is None
        # and model_fields_set contains the field
        if self.comment is None and "comment" in self.model_fields_set:
            _dict['comment'] = None

        # set to None if forwarder_name (nullable) is None
        # and model_fields_set contains the field
        if self.forwarder_name is None and "forwarder_name" in self.model_fields_set:
            _dict['forwarderName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApprovalForwardHistory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "oldApproverName": obj.get("oldApproverName"),
            "newApproverName": obj.get("newApproverName"),
            "comment": obj.get("comment"),
            "modified": obj.get("modified"),
            "forwarderName": obj.get("forwarderName"),
            "reassignmentType": obj.get("reassignmentType")
        })
        return _obj


