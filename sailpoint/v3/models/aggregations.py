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
from pydantic import BaseModel
from sailpoint.v3.models.bucket_aggregation import BucketAggregation
from sailpoint.v3.models.filter_aggregation import FilterAggregation
from sailpoint.v3.models.metric_aggregation import MetricAggregation
from sailpoint.v3.models.nested_aggregation import NestedAggregation
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class Aggregations(BaseModel):
    """
    Aggregations
    """

  # noqa: E501
    nested: Optional[NestedAggregation] = None
    metric: Optional[MetricAggregation] = None
    filter: Optional[FilterAggregation] = None
    bucket: Optional[BucketAggregation] = None
    __properties: ClassVar[List[str]] = [
        "nested", "metric", "filter", "bucket"
    ]

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
        """Create an instance of Aggregations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of nested
        if self.nested:
            _dict['nested'] = self.nested.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metric
        if self.metric:
            _dict['metric'] = self.metric.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bucket
        if self.bucket:
            _dict['bucket'] = self.bucket.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Aggregations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "nested":
            NestedAggregation.from_dict(obj.get("nested"))
            if obj.get("nested") is not None else None,
            "metric":
            MetricAggregation.from_dict(obj.get("metric"))
            if obj.get("metric") is not None else None,
            "filter":
            FilterAggregation.from_dict(obj.get("filter"))
            if obj.get("filter") is not None else None,
            "bucket":
            BucketAggregation.from_dict(obj.get("bucket"))
            if obj.get("bucket") is not None else None
        })
        return _obj
