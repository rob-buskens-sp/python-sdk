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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from sailpoint.v3.models.certification_decision import CertificationDecision
from sailpoint.v3.models.review_recommendation import ReviewRecommendation
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class ReviewDecision(BaseModel):
    """
    ReviewDecision
    """

  # noqa: E501
    id: StrictStr = Field(description="The id of the review decision")
    decision: CertificationDecision
    proposed_end_date: Optional[datetime] = Field(
        default=None,
        description=
        "The date at which a user's access should be taken away. Should only be set for `REVOKE` decisions.",
        alias="proposedEndDate")
    bulk: StrictBool = Field(
        description=
        "Indicates whether decision should be marked as part of a larger bulk decision"
    )
    recommendation: Optional[ReviewRecommendation] = None
    comments: Optional[StrictStr] = Field(
        default=None,
        description="Comments recorded when the decision was made")
    __properties: ClassVar[List[str]] = [
        "id", "decision", "proposedEndDate", "bulk", "recommendation",
        "comments"
    ]

    model_config = {"populate_by_name": True, "validate_assignment": True}

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReviewDecision from a JSON string"""
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
            exclude={},
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of recommendation
        if self.recommendation:
            _dict['recommendation'] = self.recommendation.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ReviewDecision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "decision":
            obj.get("decision"),
            "proposedEndDate":
            obj.get("proposedEndDate"),
            "bulk":
            obj.get("bulk"),
            "recommendation":
            ReviewRecommendation.from_dict(obj.get("recommendation"))
            if obj.get("recommendation") is not None else None,
            "comments":
            obj.get("comments")
        })
        return _obj
