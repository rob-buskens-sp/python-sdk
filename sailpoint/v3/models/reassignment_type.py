# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

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


class ReassignmentType(str, Enum):
    """
    The approval reassignment type.  * MANUAL_REASSIGNMENT: An approval with this reassignment type has been specifically reassigned by the approval task's owner, from their queue to someone else's.  * AUTOMATIC_REASSIGNMENT: An approval with this reassignment type has been automatically reassigned from another approver's queue, according to that approver's reassignment configuration. The approver's reassignment configuration may be set up to automatically reassign approval tasks for a defined (or possibly open-ended) period of time. * AUTO_ESCALATION: An approval with this reassignment type has been automatically reassigned from another approver's queue, according to the request's escalation configuration. For more information about escalation configuration, refer to [Setting Global Reminders and Escalation Policies](https://documentation.sailpoint.com/saas/help/requests/config_emails.html). * SELF_REVIEW_DELEGATION: An approval with this reassignment type has been automatically reassigned by the system to prevent self-review. This helps prevent situations like a requester being tasked with approving their own request. For more information about preventing self-review, refer to [Self-review Prevention](https://documentation.sailpoint.com/saas/help/users/work_reassignment.html#self-review-prevention) and [Preventing Self-approval](https://documentation.sailpoint.com/saas/help/requests/config_ap_roles.html#preventing-self-approval).
    """

    """
    allowed enum values
    """
    MANUAL_REASSIGNMENT = 'MANUAL_REASSIGNMENT'
    AUTOMATIC_REASSIGNMENT = 'AUTOMATIC_REASSIGNMENT'
    AUTO_ESCALATION = 'AUTO_ESCALATION'
    SELF_REVIEW_DELEGATION = 'SELF_REVIEW_DELEGATION'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ReassignmentType from a JSON string"""
        return cls(json.loads(json_str))


