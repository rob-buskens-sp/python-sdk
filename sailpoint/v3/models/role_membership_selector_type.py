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


class RoleMembershipSelectorType(str, Enum):
    """
    This enum characterizes the type of a Role's membership selector. Only the following two are fully supported:  STANDARD: Indicates that Role membership is defined in terms of a criteria expression  IDENTITY_LIST: Indicates that Role membership is conferred on the specific identities listed
    """
    """
    allowed enum values
    """
    STANDARD = 'STANDARD'
    IDENTITY_LIST = 'IDENTITY_LIST'

    @classmethod
    def from_json(cls, json_str: str) -> RoleMembershipSelectorType:
        """Create an instance of RoleMembershipSelectorType from a JSON string"""
        return RoleMembershipSelectorType(json.loads(json_str))
