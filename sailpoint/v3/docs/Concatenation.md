# Concatenation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[object]** | An array of items to join together | 
**requires_periodic_refresh** | **bool** | A value that indicates whether the transform logic should be re-evaluated every evening as part of the identity refresh process | [optional] [default to False]
**input** | **Dict[str, object]** | This is an optional attribute that can explicitly define the input data which will be fed into the transform logic. If input is not provided, the transform will take its input from the source and attribute combination configured via the UI. | [optional] 

## Example

```python
from sailpoint.v3.models.concatenation import Concatenation

# TODO update the JSON string below
json = "{}"
# create an instance of Concatenation from a JSON string
concatenation_instance = Concatenation.from_json(json)
# print the JSON string representation of the object
print Concatenation.to_json()

# convert the object into a dict
concatenation_dict = concatenation_instance.to_dict()
# create an instance of Concatenation from a dict
concatenation_form_dict = concatenation.from_dict(concatenation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


