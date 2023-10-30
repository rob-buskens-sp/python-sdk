# coding: utf-8

"""
    IdentityNow V3 API

    Use these APIs to interact with the IdentityNow platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class AttributeDefinitionType(str, Enum):
    """
    The underlying type of the value which an AttributeDefinition represents.
    """

    """
    allowed enum values
    """
    STRING = 'STRING'
    LONG = 'LONG'
    INT = 'INT'
    BOOLEAN = 'BOOLEAN'

    @classmethod
    def from_json(cls, json_str: str) -> AttributeDefinitionType:
        """Create an instance of AttributeDefinitionType from a JSON string"""
        return AttributeDefinitionType(json.loads(json_str))


