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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class SourceHealthDto(BaseModel):
    """
    Dto for source health data
    """

  # noqa: E501
    id: Optional[StrictStr] = Field(default=None,
                                    description="the id of the Source")
    type: Optional[StrictStr] = Field(
        default=None,
        description=
        "Specifies the type of system being managed e.g. Active Directory, Workday, etc.. If you are creating a Delimited File source, you must set the `provisionasCsv` query parameter to `true`. "
    )
    name: Optional[StrictStr] = Field(default=None,
                                      description="the name of the source")
    org: Optional[StrictStr] = Field(default=None, description="source's org")
    is_authoritative: Optional[StrictBool] = Field(
        default=None,
        description="Is the source authoritative",
        alias="isAuthoritative")
    is_cluster: Optional[StrictBool] = Field(
        default=None,
        description="Is the source in a cluster",
        alias="isCluster")
    hostname: Optional[StrictStr] = Field(default=None,
                                          description="source's hostname")
    pod: Optional[StrictStr] = Field(default=None, description="source's pod")
    iq_service_version: Optional[StrictStr] = Field(
        default=None,
        description="The version of the iqService",
        alias="iqServiceVersion")
    status: Optional[StrictStr] = Field(default=None,
                                        description="connection test result")
    __properties: ClassVar[List[str]] = [
        "id", "type", "name", "org", "isAuthoritative", "isCluster",
        "hostname", "pod", "iqServiceVersion", "status"
    ]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SOURCE_STATE_ERROR_CLUSTER',
                         'SOURCE_STATE_ERROR_SOURCE', 'SOURCE_STATE_ERROR_VA',
                         'SOURCE_STATE_FAILURE_CLUSTER',
                         'SOURCE_STATE_FAILURE_SOURCE', 'SOURCE_STATE_HEALTHY',
                         'SOURCE_STATE_UNCHECKED_CLUSTER',
                         'SOURCE_STATE_UNCHECKED_CLUSTER_NO_SOURCES',
                         'SOURCE_STATE_UNCHECKED_SOURCE',
                         'SOURCE_STATE_UNCHECKED_SOURCE_NO_ACCOUNTS'):
            raise ValueError(
                "must be one of enum values ('SOURCE_STATE_ERROR_CLUSTER', 'SOURCE_STATE_ERROR_SOURCE', 'SOURCE_STATE_ERROR_VA', 'SOURCE_STATE_FAILURE_CLUSTER', 'SOURCE_STATE_FAILURE_SOURCE', 'SOURCE_STATE_HEALTHY', 'SOURCE_STATE_UNCHECKED_CLUSTER', 'SOURCE_STATE_UNCHECKED_CLUSTER_NO_SOURCES', 'SOURCE_STATE_UNCHECKED_SOURCE', 'SOURCE_STATE_UNCHECKED_SOURCE_NO_ACCOUNTS')"
            )
        return value

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
        """Create an instance of SourceHealthDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SourceHealthDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id":
            obj.get("id"),
            "type":
            obj.get("type"),
            "name":
            obj.get("name"),
            "org":
            obj.get("org"),
            "isAuthoritative":
            obj.get("isAuthoritative"),
            "isCluster":
            obj.get("isCluster"),
            "hostname":
            obj.get("hostname"),
            "pod":
            obj.get("pod"),
            "iqServiceVersion":
            obj.get("iqServiceVersion"),
            "status":
            obj.get("status")
        })
        return _obj
