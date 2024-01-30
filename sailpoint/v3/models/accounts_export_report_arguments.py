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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AccountsExportReportArguments(BaseModel):
    """
    Arguments for Account Export (ACCOUNTS)
    """

  # noqa: E501
    application: StrictStr = Field(
        description=
        "Id of the authoritative source to export related accounts e.g. identities"
    )
    source_name: StrictStr = Field(
        description="Name of the authoritative source for accounts export",
        alias="sourceName")
    default_s3_bucket: StrictBool = Field(
        description=
        "Use it to set default s3 bucket where generated report will be saved.  In case this argument is false and 's3Bucket' argument is null or absent there will be default s3Bucket assigned to the report.",
        alias="defaultS3Bucket")
    s3_bucket: Optional[StrictStr] = Field(
        default=None,
        description=
        "If you want to be specific you could use this argument with defaultS3Bucket = false.",
        alias="s3Bucket")
    __properties: ClassVar[List[str]] = [
        "application", "sourceName", "defaultS3Bucket", "s3Bucket"
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
        """Create an instance of AccountsExportReportArguments from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AccountsExportReportArguments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "application": obj.get("application"),
            "sourceName": obj.get("sourceName"),
            "defaultS3Bucket": obj.get("defaultS3Bucket"),
            "s3Bucket": obj.get("s3Bucket")
        })
        return _obj
