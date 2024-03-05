# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class WorkItemStateManualWorkItems(str, Enum):
    """
    The state of a work item
    """

    """
    allowed enum values
    """
    FINISHED = 'Finished'
    REJECTED = 'Rejected'
    RETURNED = 'Returned'
    EXPIRED = 'Expired'
    PENDING = 'Pending'
    CANCELED = 'Canceled'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WorkItemStateManualWorkItems from a JSON string"""
        return cls(json.loads(json_str))


