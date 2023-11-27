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


class RoleMiningPotentialRoleProvisionState(str, Enum):
    """
    Provision state
    """
    """
    allowed enum values
    """
    POTENTIAL = 'POTENTIAL'
    PENDING = 'PENDING'
    COMPLETE = 'COMPLETE'
    FAILED = 'FAILED'

    @classmethod
    def from_json(cls, json_str: str) -> RoleMiningPotentialRoleProvisionState:
        """Create an instance of RoleMiningPotentialRoleProvisionState from a JSON string"""
        return RoleMiningPotentialRoleProvisionState(json.loads(json_str))
