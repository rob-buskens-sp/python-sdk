# ActorType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | the actor or target name | [optional] 

## Example

```python
from sailpoint.v3.models.actor_type import ActorType

# TODO update the JSON string below
json = "{}"
# create an instance of ActorType from a JSON string
actor_type_instance = ActorType.from_json(json)
# print the JSON string representation of the object
print ActorType.to_json()

# convert the object into a dict
actor_type_dict = actor_type_instance.to_dict()
# create an instance of ActorType from a dict
actor_type_form_dict = actor_type.from_dict(actor_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


