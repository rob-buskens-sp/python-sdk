# Reference1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique ID of the referenced object. | [optional] 
**name** | **str** | The human readable name of the referenced object. | [optional] 

## Example

```python
from sailpoint.v3.models.reference1 import Reference1

# TODO update the JSON string below
json = "{}"
# create an instance of Reference1 from a JSON string
reference1_instance = Reference1.from_json(json)
# print the JSON string representation of the object
print Reference1.to_json()

# convert the object into a dict
reference1_dict = reference1_instance.to_dict()
# create an instance of Reference1 from a dict
reference1_form_dict = reference1.from_dict(reference1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


