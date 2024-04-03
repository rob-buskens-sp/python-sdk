# coding: utf-8

"""
    Identity Security Cloud Beta API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
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


class ManagedClientType(str, Enum):
    """
    Managed Client type
    """

    """
    allowed enum values
    """
    CCG = 'CCG'
    VA = 'VA'
    INTERNAL = 'INTERNAL'
    IIQ_HARVESTER = 'IIQ_HARVESTER'
    NULL = 'null'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ManagedClientType from a JSON string"""
        return cls(json.loads(json_str))


