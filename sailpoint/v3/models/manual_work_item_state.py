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


class ManualWorkItemState(str, Enum):
    """
    Indicates the state of the request processing for this item: * PENDING: The request for this item is awaiting processing. * APPROVED: The request for this item has been approved. * REJECTED: The request for this item was rejected. * EXPIRED: The request for this item expired with no action taken. * CANCELLED: The request for this item was cancelled with no user action. * ARCHIVED: The request for this item has been archived after completion.
    """
    """
    allowed enum values
    """
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    REJECTED = 'REJECTED'
    EXPIRED = 'EXPIRED'
    CANCELLED = 'CANCELLED'
    ARCHIVED = 'ARCHIVED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManualWorkItemState from a JSON string"""
        return cls(json.loads(json_str))
