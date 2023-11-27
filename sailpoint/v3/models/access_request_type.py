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


class AccessRequestType(str, Enum):
    """
    Access request type. Defaults to GRANT_ACCESS. REVOKE_ACCESS type can only have a single Identity ID in the requestedFor field.
    """
    """
    allowed enum values
    """
    GRANT_ACCESS = 'GRANT_ACCESS'
    REVOKE_ACCESS = 'REVOKE_ACCESS'

    @classmethod
    def from_json(cls, json_str: str) -> AccessRequestType:
        """Create an instance of AccessRequestType from a JSON string"""
        return AccessRequestType(json.loads(json_str))
