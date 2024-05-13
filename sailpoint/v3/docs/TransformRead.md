# TransformRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of this transform | 
**type** | **str** | The type of transform operation | 
**attributes** | [**TransformAttributes**](TransformAttributes.md) |  | 
**id** | **str** | Unique ID of this transform | 
**internal** | **bool** | Indicates whether this is an internal SailPoint-created transform or a customer-created transform | [default to False]

## Example

```python
from sailpoint.v3.models.transform_read import TransformRead

# TODO update the JSON string below
json = "{}"
# create an instance of TransformRead from a JSON string
transform_read_instance = TransformRead.from_json(json)
# print the JSON string representation of the object
print TransformRead.to_json()

# convert the object into a dict
transform_read_dict = transform_read_instance.to_dict()
# create an instance of TransformRead from a dict
transform_read_form_dict = transform_read.from_dict(transform_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


