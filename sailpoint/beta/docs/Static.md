# Static


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **str** | This must evaluate to a JSON string, either through a fixed value or through conditional logic using the Apache Velocity Template Language. | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]

## Example

```python
from sailpoint.beta.models.static import Static

# TODO update the JSON string below
json = "{}"
# create an instance of Static from a JSON string
static_instance = Static.from_json(json)
# print the JSON string representation of the object
print Static.to_json()

# convert the object into a dict
static_dict = static_instance.to_dict()
# create an instance of Static from a dict
static_form_dict = static.from_dict(static_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


