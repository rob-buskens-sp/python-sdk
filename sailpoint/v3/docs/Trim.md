# Trim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.trim import Trim

# TODO update the JSON string below
json = "{}"
# create an instance of Trim from a JSON string
trim_instance = Trim.from_json(json)
# print the JSON string representation of the object
print Trim.to_json()

# convert the object into a dict
trim_dict = trim_instance.to_dict()
# create an instance of Trim from a dict
trim_form_dict = trim.from_dict(trim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


