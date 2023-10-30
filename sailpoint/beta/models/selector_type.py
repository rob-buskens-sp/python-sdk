# coding: utf-8

"""
    IdentityNow Beta API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. These APIs are in beta and are subject to change. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.1.0-beta
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class SelectorType(str, Enum):
    """
    Enum representing the currently supported selector types.  LIST - the *values* array contains one or more distinct values.  RANGE - the *values* array contains two values: the start and end of the range, inclusive.  Additional values may be added in the future without notice. 
    """

    """
    allowed enum values
    """
    LIST = 'LIST'
    RANGE = 'RANGE'

    @classmethod
    def from_json(cls, json_str: str) -> SelectorType:
        """Create an instance of SelectorType from a JSON string"""
        return SelectorType(json.loads(json_str))


