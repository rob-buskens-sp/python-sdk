# coding: utf-8

"""
    Identity Security Cloud V3 API

    Use these APIs to interact with the Identity Security Cloud platform to achieve repeatable, automated processes with greater scalability. We encourage you to join the SailPoint Developer Community forum at https://developer.sailpoint.com/discuss to connect with other developers using our APIs.

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from sailpoint.v3.models.document_type import DocumentType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EventDocument(BaseModel):
    """
    Event
    """ # noqa: E501
    id: StrictStr
    name: StrictStr
    type: DocumentType = Field(alias="_type")
    created: Optional[datetime] = Field(default=None, description="ISO-8601 date-time referring to the time when the object was created.")
    synced: Optional[StrictStr] = Field(default=None, description="ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the `synced` time and the time when the updated data is actually available in the search API. ")
    action: Optional[StrictStr] = Field(default=None, description="Name of the event as it's displayed in audit reports.")
    type: Optional[StrictStr] = Field(default=None, description="Event type. Refer to [Event Types](https://documentation.sailpoint.com/saas/help/search/index.html#event-types) for a list of event types and their meanings.")
    actor: Optional[StrictStr] = Field(default=None, description="Name of the actor that generated the event.")
    target: Optional[StrictStr] = Field(default=None, description="Name of the target, or recipient, of the event.")
    stack: Optional[StrictStr] = Field(default=None, description="The event's stack.")
    tracking_number: Optional[StrictStr] = Field(default=None, description="ID of the group of events.", alias="trackingNumber")
    ip_address: Optional[StrictStr] = Field(default=None, description="Target system's IP address.", alias="ipAddress")
    details: Optional[StrictStr] = Field(default=None, description="ID of event's details.")
    attributes: Optional[Dict[str, Any]] = Field(default=None, description="Attributes involved in the event.")
    objects: Optional[List[StrictStr]] = Field(default=None, description="Objects the event is happening to.")
    operation: Optional[StrictStr] = Field(default=None, description="Operation, or action, performed during the event.")
    status: Optional[StrictStr] = Field(default=None, description="Event status. Refer to [Event Statuses](https://documentation.sailpoint.com/saas/help/search/index.html#event-statuses) for a list of event statuses and their meanings.")
    technical_name: Optional[StrictStr] = Field(default=None, description="Event's normalized name. This normalized name always follows the pattern of 'objects_operation_status'.", alias="technicalName")
    __properties: ClassVar[List[str]] = ["id", "name", "_type", "created", "synced", "action", "type", "actor", "target", "stack", "trackingNumber", "ipAddress", "details", "attributes", "objects", "operation", "status", "technicalName"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventDocument from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EventDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "_type": obj.get("_type"),
            "created": obj.get("created"),
            "synced": obj.get("synced"),
            "action": obj.get("action"),
            "type": obj.get("type"),
            "actor": obj.get("actor"),
            "target": obj.get("target"),
            "stack": obj.get("stack"),
            "trackingNumber": obj.get("trackingNumber"),
            "ipAddress": obj.get("ipAddress"),
            "details": obj.get("details"),
            "attributes": obj.get("attributes"),
            "objects": obj.get("objects"),
            "operation": obj.get("operation"),
            "status": obj.get("status"),
            "technicalName": obj.get("technicalName")
        })
        return _obj


