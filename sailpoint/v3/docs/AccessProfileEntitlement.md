# AccessProfileEntitlement

EntitlementReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 
**display_name** | **str** |  | [optional] 
**type** | [**DtoType**](DtoType.md) |  | [optional] 
**description** | **str** |  | [optional] 
**source** | [**Reference1**](Reference1.md) |  | [optional] 
**privileged** | **bool** |  | [optional] 
**attribute** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**standalone** | **bool** |  | [optional] 

## Example

```python
from sailpoint.v3.models.access_profile_entitlement import AccessProfileEntitlement

# TODO update the JSON string below
json = "{}"
# create an instance of AccessProfileEntitlement from a JSON string
access_profile_entitlement_instance = AccessProfileEntitlement.from_json(json)
# print the JSON string representation of the object
print AccessProfileEntitlement.to_json()

# convert the object into a dict
access_profile_entitlement_dict = access_profile_entitlement_instance.to_dict()
# create an instance of AccessProfileEntitlement from a dict
access_profile_entitlement_form_dict = access_profile_entitlement.from_dict(access_profile_entitlement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


