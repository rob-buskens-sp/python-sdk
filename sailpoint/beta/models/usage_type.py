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





class UsageType(str, Enum):
    """
    The type of provisioning policy usage.  In IdentityNow, a source can support various provisioning operations. For example, when a joiner is added to a source, this may trigger both CREATE and UPDATE provisioning operations.  Each usage type is considered a provisioning policy.  A source can have any number of these provisioning policies defined.  These are the common usage types:  CREATE - This usage type relates to 'Create Account Profile', the provisioning template for the account to be created. For example, this would be used for a joiner on a source.   UPDATE - This usage type relates to 'Update Account Profile', the provisioning template for the 'Update' connector operations. For example, this would be used for an attribute sync on a source. ENABLE - This usage type relates to 'Enable Account Profile', the provisioning template for the account to be enabled. For example, this could be used for a joiner on a source once the joiner's account is created.  DISABLE - This usage type relates to 'Disable Account Profile', the provisioning template for the account to be disabled. For example, this could be used when a leaver is removed temporarily from a source.  You can use these four usage types for all your provisioning policy needs. 
    """

    """
    allowed enum values
    """
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    ENABLE = 'ENABLE'
    DISABLE = 'DISABLE'
    DELETE = 'DELETE'
    ASSIGN = 'ASSIGN'
    UNASSIGN = 'UNASSIGN'
    CREATE_GROUP = 'CREATE_GROUP'
    UPDATE_GROUP = 'UPDATE_GROUP'
    DELETE_GROUP = 'DELETE_GROUP'
    REGISTER = 'REGISTER'
    CREATE_IDENTITY = 'CREATE_IDENTITY'
    UPDATE_IDENTITY = 'UPDATE_IDENTITY'
    EDIT_GROUP = 'EDIT_GROUP'
    UNLOCK = 'UNLOCK'
    CHANGE_PASSWORD = 'CHANGE_PASSWORD'

    @classmethod
    def from_json(cls, json_str: str) -> UsageType:
        """Create an instance of UsageType from a JSON string"""
        return UsageType(json.loads(json_str))


