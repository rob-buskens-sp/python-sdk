# SearchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | 
**name** | **str** | The human readable name of the referenced object. | 
**description** | **str** | Access item&#39;s description. | [optional] 
**created** | **datetime** | ISO-8601 date-time referring to the time when the object was created. | [optional] 
**modified** | **datetime** | ISO-8601 date-time referring to the time when the object was last modified. | [optional] 
**synced** | **datetime** | ISO-8601 date-time referring to the date-time when object was queued to be synced into search database for use in the search API.   This date-time changes anytime there is an update to the object, which triggers a synchronization event being sent to the search database.  There may be some delay between the &#x60;synced&#x60; time and the time when the updated data is actually available in the search API.  | [optional] 
**enabled** | **bool** | Indicates whether the access item is currently enabled. | [optional] [default to False]
**requestable** | **bool** | Indicates whether the access item can be requested. | [optional] [default to True]
**request_comments_required** | **bool** | Indicates whether comments are required for requests to access the item. | [optional] [default to False]
**owner** | [**BaseAccessAllOfOwner**](BaseAccessAllOfOwner.md) |  | [optional] 
**type** | [**DocumentType**](DocumentType.md) |  | 
**source** | [**IdentityDocumentAllOfSource**](IdentityDocumentAllOfSource.md) |  | [optional] 
**entitlements** | [**List[BaseEntitlement]**](BaseEntitlement.md) | Entitlements included with the role. | [optional] 
**entitlement_count** | **int** | Number of entitlements included with the role. | [optional] 
**tags** | **List[str]** | Tags that have been applied to the object. | [optional] 
**action** | **str** | Name of the event as it&#39;s displayed in audit reports. | [optional] 
**stage** | **str** | Activity&#39;s current stage. | [optional] 
**origin** | **str** | Activity&#39;s origin. | [optional] 
**status** | **str** | Identity&#39;s status in SailPoint. | [optional] 
**requester** | [**AccountSource**](AccountSource.md) |  | [optional] 
**recipient** | [**AccountSource**](AccountSource.md) |  | [optional] 
**tracking_number** | **str** | ID of the group of events. | [optional] 
**errors** | **List[str]** | Errors provided by the source while completing account actions. | [optional] 
**warnings** | **List[str]** | Warnings provided by the source while completing account actions. | [optional] 
**approvals** | [**List[Approval]**](Approval.md) | Approvals performed on an item during activity. | [optional] 
**original_requests** | [**List[OriginalRequest]**](OriginalRequest.md) | Original actions that triggered all individual source actions related to the account action. | [optional] 
**expansion_items** | [**List[ExpansionItem]**](ExpansionItem.md) | Controls that translated the attribute requests into actual provisioning actions on the source. | [optional] 
**account_requests** | [**List[AccountRequest]**](AccountRequest.md) | Account data for each individual source action triggered by the original requests. | [optional] 
**sources** | **str** | Sources involved in the account activity. | [optional] 
**display_name** | **str** | Identity&#39;s display name. | [optional] 
**segments** | [**List[BaseSegment]**](BaseSegment.md) | Segments with the role. | [optional] 
**segment_count** | **int** | Number of segments with the role. | [optional] 
**cloud_governed** | **bool** | Indicates whether the entitlement is cloud governed. | [optional] [default to False]
**privileged** | **bool** | Indicates whether the entitlement is privileged. | [optional] [default to False]
**identity_count** | **int** | Number of identities who have access to the entitlement. | [optional] 
**type** | **str** | Event type. Refer to [Event Types](https://documentation.sailpoint.com/saas/help/search/index.html#event-types) for a list of event types and their meanings. | [optional] 
**actor** | [**ActorType**](ActorType.md) |  | [optional] 
**target** | [**TargetType**](TargetType.md) |  | [optional] 
**stack** | **str** | The event&#39;s stack. | [optional] 
**ip_address** | **str** | Target system&#39;s IP address. | [optional] 
**details** | **str** | ID of event&#39;s details. | [optional] 
**attributes** | **Dict[str, object]** | Map or dictionary of key/value pairs. | [optional] 
**objects** | **List[str]** | Objects the event is happening to. | [optional] 
**operation** | **str** | Operation, or action, performed during the event. | [optional] 
**technical_name** | **str** | Event&#39;s normalized name. This normalized name always follows the pattern of &#39;objects_operation_status&#39;. | [optional] 
**first_name** | **str** | Identity&#39;s first name. | [optional] 
**last_name** | **str** | Identity&#39;s last name. | [optional] 
**email** | **str** | Identity&#39;s primary email address. | [optional] 
**phone** | **str** | Identity&#39;s phone number. | [optional] 
**inactive** | **bool** | Indicates whether the identity is inactive. | [optional] [default to False]
**protected** | **bool** | Indicates whether the identity is protected. | [optional] [default to False]
**employee_number** | **str** | Identity&#39;s employee number. | [optional] 
**manager** | [**IdentityDocumentAllOfManager**](IdentityDocumentAllOfManager.md) |  | [optional] 
**is_manager** | **bool** | Indicates whether the identity is a manager of other identities. | [optional] 
**identity_profile** | [**IdentityDocumentAllOfIdentityProfile**](IdentityDocumentAllOfIdentityProfile.md) |  | [optional] 
**processing_state** | **str** | Identity&#39;s processing state. | [optional] 
**processing_details** | [**ProcessingDetails**](ProcessingDetails.md) |  | [optional] 
**accounts** | [**List[BaseAccount]**](BaseAccount.md) | List of accounts associated with the identity. | [optional] 
**account_count** | **int** | Number of accounts associated with the identity. | [optional] 
**apps** | [**List[App]**](App.md) | List of applications the identity has access to. | [optional] 
**app_count** | **int** | Number of applications the identity has access to. | [optional] 
**access** | [**List[IdentityAccess]**](IdentityAccess.md) | List of access items assigned to the identity. | [optional] 
**access_count** | **int** | Number of access items assigned to the identity. | [optional] 
**role_count** | **int** | Number of roles assigned to the identity. | [optional] 
**access_profile_count** | **int** | Number of access profiles included with the role. | [optional] 
**owns** | [**List[Owns]**](Owns.md) | Access items the identity owns. | [optional] 
**owns_count** | **int** | Number of access items the identity owns. | [optional] 
**access_profiles** | [**List[BaseAccessProfile]**](BaseAccessProfile.md) | Access profiles included with the role. | [optional] 

## Example

```python
from sailpoint.v3.models.search_document import SearchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDocument from a JSON string
search_document_instance = SearchDocument.from_json(json)
# print the JSON string representation of the object
print SearchDocument.to_json()

# convert the object into a dict
search_document_dict = search_document_instance.to_dict()
# create an instance of SearchDocument from a dict
search_document_form_dict = search_document.from_dict(search_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


