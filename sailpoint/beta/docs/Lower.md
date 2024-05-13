# Lower


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.beta.models.lower import Lower

# TODO update the JSON string below
json = "{}"
# create an instance of Lower from a JSON string
lower_instance = Lower.from_json(json)
# print the JSON string representation of the object
print Lower.to_json()

# convert the object into a dict
lower_dict = lower_instance.to_dict()
# create an instance of Lower from a dict
lower_form_dict = lower.from_dict(lower_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


